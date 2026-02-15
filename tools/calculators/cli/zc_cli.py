#!/usr/bin/env python3
"""
Zc Calculator - Command Line Interface
CIM Pattern - Cognitive Impedance Measurement Tool

Usage:
    python zc_cli.py --vgen 45 --bsocial 30
    python zc_cli.py --interactive
    python zc_cli.py --monitor slack_export.json
"""

import sys
import json
import argparse
from datetime import datetime, timedelta
from typing import Dict, Tuple


class ZcCalculator:
    """Calculate and interpret Cognitive Impedance ratio"""
    
    # Thresholds
    GREEN_THRESHOLD = 0.7
    YELLOW_THRESHOLD = 1.0
    
    def __init__(self):
        self.history = []
    
    def calculate(self, v_generation: float, b_social: float) -> float:
        """Calculate Zc ratio"""
        if b_social <= 0:
            raise ValueError("B_social must be greater than 0")
        
        zc = v_generation / b_social
        self.history.append({
            'timestamp': datetime.now().isoformat(),
            'v_generation': v_generation,
            'b_social': b_social,
            'zc': zc
        })
        return zc
    
    def interpret(self, zc: float) -> Dict[str, str]:
        """Interpret Zc value and provide recommendations"""
        if zc < self.GREEN_THRESHOLD:
            return {
                'zone': 'GREEN',
                'mode': 'Mode A: Study Hall',
                'status': '✓ Healthy - Async-first working well',
                'action': 'Continue with async workflows. No forced sync needed.',
                'urgency': 'low'
            }
        elif zc < self.YELLOW_THRESHOLD:
            return {
                'zone': 'YELLOW',
                'mode': 'Mode B: GUSH',
                'status': '⚠ Warning - Approaching overload',
                'action': 'Schedule GUSH session within 48h to force convergence.',
                'urgency': 'medium'
            }
        else:
            return {
                'zone': 'RED',
                'mode': 'Mode C: The Jam',
                'status': '🚨 Critical - Standard consensus broken',
                'action': 'Activate The Jam immediately. Declare BHO forks. Implement BLUES rhythm.',
                'urgency': 'high'
            }
    
    def estimate_from_metrics(self, 
                            slack_messages: int = 0,
                            notion_updates: int = 0,
                            ai_outputs: int = 0,
                            emails: int = 0,
                            timeframe_hours: int = 24,
                            team_size: int = 10,
                            processing_hours_per_person: float = 3.0) -> Tuple[float, float]:
        """
        Estimate V_generation and B_social from real metrics
        
        Args:
            slack_messages: Number of Slack messages in timeframe
            notion_updates: Number of Notion page updates in timeframe
            ai_outputs: Number of AI-generated outputs in timeframe
            emails: Number of email threads in timeframe
            timeframe_hours: Measurement timeframe in hours
            team_size: Number of team members
            processing_hours_per_person: Effective processing hours per person per day
        
        Returns:
            Tuple of (v_generation, b_social)
        """
        total_items = slack_messages + notion_updates + ai_outputs + emails
        v_generation = total_items / timeframe_hours
        
        # B_social = team processing capacity per hour
        b_social = (team_size * processing_hours_per_person * 24) / timeframe_hours
        
        return v_generation, b_social
    
    def format_output(self, zc: float, interpretation: Dict[str, str], 
                     v_gen: float, b_social: float, verbose: bool = False) -> str:
        """Format calculation results for display"""
        zone_colors = {
            'GREEN': '\033[92m',    # Green
            'YELLOW': '\033[93m',   # Yellow
            'RED': '\033[91m',      # Red
        }
        reset = '\033[0m'
        bold = '\033[1m'
        
        color = zone_colors.get(interpretation['zone'], '')
        
        output = []
        output.append(f"\n{bold}{'=' * 60}{reset}")
        output.append(f"{bold}Cognitive Impedance Analysis{reset}")
        output.append(f"{'=' * 60}\n")
        
        output.append(f"{bold}Zc Ratio:{reset} {color}{zc:.2f}{reset}")
        output.append(f"{bold}Zone:{reset} {color}{interpretation['zone']}{reset}")
        output.append(f"{bold}Mode:{reset} {interpretation['mode']}")
        output.append(f"{bold}Status:{reset} {interpretation['status']}\n")
        
        if verbose:
            output.append(f"{bold}Input Values:{reset}")
            output.append(f"  V_generation: {v_gen:.2f} items/hour")
            output.append(f"  B_social: {b_social:.2f} capacity/hour\n")
        
        output.append(f"{bold}Recommended Action:{reset}")
        output.append(f"  {interpretation['action']}\n")
        
        output.append(f"{'=' * 60}\n")
        
        return '\n'.join(output)


def interactive_mode():
    """Run calculator in interactive mode"""
    calc = ZcCalculator()
    
    print("\n" + "=" * 60)
    print("Zc Calculator - Interactive Mode")
    print("=" * 60 + "\n")
    
    print("Choose input method:")
    print("1. Direct values (V_generation and B_social)")
    print("2. Estimate from metrics (Slack, Notion, etc.)")
    
    choice = input("\nEnter choice (1 or 2): ").strip()
    
    if choice == "1":
        try:
            v_gen = float(input("\nV_generation (items/hour): "))
            b_social = float(input("B_social (capacity/hour): "))
        except ValueError:
            print("Error: Please enter valid numbers")
            return
    
    elif choice == "2":
        print("\nEnter metrics from last 24 hours:")
        try:
            slack = int(input("Slack messages: "))
            notion = int(input("Notion updates: "))
            ai = int(input("AI outputs: "))
            emails = int(input("Email threads: "))
            team_size = int(input("\nTeam size: "))
            proc_hours = float(input("Processing hours/person/day (default 3.0): ") or "3.0")
            
            v_gen, b_social = calc.estimate_from_metrics(
                slack, notion, ai, emails,
                team_size=team_size,
                processing_hours_per_person=proc_hours
            )
            
            print(f"\n{'-' * 60}")
            print(f"Estimated values:")
            print(f"  V_generation: {v_gen:.2f} items/hour")
            print(f"  B_social: {b_social:.2f} capacity/hour")
            print(f"{'-' * 60}\n")
            
        except ValueError:
            print("Error: Please enter valid numbers")
            return
    else:
        print("Invalid choice")
        return
    
    zc = calc.calculate(v_gen, b_social)
    interpretation = calc.interpret(zc)
    print(calc.format_output(zc, interpretation, v_gen, b_social, verbose=True))


def monitor_mode(filepath: str):
    """Monitor Zc from JSON metrics file"""
    calc = ZcCalculator()
    
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        # Expecting format: {"slack_messages": 150, "notion_updates": 20, ...}
        v_gen, b_social = calc.estimate_from_metrics(
            slack_messages=data.get('slack_messages', 0),
            notion_updates=data.get('notion_updates', 0),
            ai_outputs=data.get('ai_outputs', 0),
            emails=data.get('emails', 0),
            timeframe_hours=data.get('timeframe_hours', 24),
            team_size=data.get('team_size', 10),
            processing_hours_per_person=data.get('processing_hours_per_person', 3.0)
        )
        
        zc = calc.calculate(v_gen, b_social)
        interpretation = calc.interpret(zc)
        print(calc.format_output(zc, interpretation, v_gen, b_social, verbose=True))
        
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in '{filepath}'")
    except Exception as e:
        print(f"Error: {e}")


def main():
    parser = argparse.ArgumentParser(
        description='Calculate Cognitive Impedance (Zc) ratio for your team',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --vgen 45 --bsocial 30
  %(prog)s --interactive
  %(prog)s --monitor metrics.json
  
  # Estimate from metrics
  %(prog)s --slack 150 --notion 20 --ai 30 --emails 40 --team-size 10

For more information: https://github.com/pyragogy/protocols
        """
    )
    
    parser.add_argument('--vgen', type=float, help='V_generation (items per hour)')
    parser.add_argument('--bsocial', type=float, help='B_social (processing capacity per hour)')
    parser.add_argument('--interactive', action='store_true', help='Run in interactive mode')
    parser.add_argument('--monitor', type=str, help='Monitor from JSON file')
    
    # Metric-based estimation
    parser.add_argument('--slack', type=int, help='Slack messages in last 24h')
    parser.add_argument('--notion', type=int, help='Notion updates in last 24h')
    parser.add_argument('--ai', type=int, help='AI outputs in last 24h')
    parser.add_argument('--emails', type=int, help='Email threads in last 24h')
    parser.add_argument('--team-size', type=int, default=10, help='Team size (default: 10)')
    parser.add_argument('--proc-hours', type=float, default=3.0, 
                       help='Processing hours per person per day (default: 3.0)')
    
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    
    args = parser.parse_args()
    
    calc = ZcCalculator()
    
    # Interactive mode
    if args.interactive:
        interactive_mode()
        return
    
    # Monitor mode
    if args.monitor:
        monitor_mode(args.monitor)
        return
    
    # Metric-based estimation
    if any([args.slack, args.notion, args.ai, args.emails]):
        v_gen, b_social = calc.estimate_from_metrics(
            slack_messages=args.slack or 0,
            notion_updates=args.notion or 0,
            ai_outputs=args.ai or 0,
            emails=args.emails or 0,
            team_size=args.team_size,
            processing_hours_per_person=args.proc_hours
        )
    # Direct values
    elif args.vgen is not None and args.bsocial is not None:
        v_gen = args.vgen
        b_social = args.bsocial
    else:
        parser.print_help()
        return
    
    zc = calc.calculate(v_gen, b_social)
    interpretation = calc.interpret(zc)
    print(calc.format_output(zc, interpretation, v_gen, b_social, verbose=args.verbose))


if __name__ == '__main__':
    main()
