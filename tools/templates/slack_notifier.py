#!/usr/bin/env python3
"""
Slack Integration Template for CIM Pattern
Sends mode switching notifications to your Slack workspace

Setup:
1. Create Slack webhook: https://api.slack.com/messaging/webhooks
2. Set SLACK_WEBHOOK_URL environment variable
3. Run: python slack_notifier.py --mode GUSH --zc 0.85

Or integrate into your existing monitoring scripts.
"""

import os
import json
import sys
from urllib.request import Request, urlopen
from urllib.error import URLError


class SlackNotifier:
    """Send CIM Pattern notifications to Slack"""
    
    MODE_CONFIGS = {
        'STUDY_HALL': {
            'color': '#16a34a',  # Green
            'emoji': '🟢',
            'title': 'Mode A: Study Hall',
            'description': 'Green Zone - Async-first working well'
        },
        'GUSH': {
            'color': '#f59e0b',  # Yellow
            'emoji': '🟡',
            'title': 'Mode B: GUSH',
            'description': 'Warning Zone - Schedule convergence session'
        },
        'JAM': {
            'color': '#dc2626',  # Red
            'emoji': '🔴',
            'title': 'Mode C: The Jam',
            'description': 'Critical - Activate rhythm protocols'
        }
    }
    
    def __init__(self, webhook_url: str = None):
        self.webhook_url = webhook_url or os.environ.get('SLACK_WEBHOOK_URL')
        if not self.webhook_url:
            raise ValueError("Slack webhook URL not provided")
    
    def send_mode_switch(self, mode: str, zc: float, 
                        v_gen: float = None, b_social: float = None,
                        custom_message: str = None):
        """Send mode switch notification"""
        
        config = self.MODE_CONFIGS.get(mode.upper())
        if not config:
            raise ValueError(f"Unknown mode: {mode}")
        
        # Build message
        blocks = [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": f"{config['emoji']} CIM Pattern: {config['title']}",
                    "emoji": True
                }
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": f"*Zc Ratio:*\n`{zc:.2f}`"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"*Status:*\n{config['description']}"
                    }
                ]
            }
        ]
        
        # Add metrics if provided
        if v_gen is not None and b_social is not None:
            blocks.append({
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": f"*V_generation:*\n`{v_gen:.1f}` items/hour"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"*B_social:*\n`{b_social:.1f}` capacity/hour"
                    }
                ]
            })
        
        # Add action recommendations
        if mode.upper() == 'GUSH':
            blocks.append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Recommended Actions:*\n• Schedule GUSH session within 48h\n• Use forced convergence template\n• Reduce async noise before session"
                }
            })
        elif mode.upper() == 'JAM':
            blocks.append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Immediate Actions:*\n• Declare BHO (Cognitive Fork) for deep work\n• Implement BLUES (The Pulse) rhythm\n• Consider pausing new initiatives"
                }
            })
        
        # Add custom message if provided
        if custom_message:
            blocks.append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": custom_message
                }
            })
        
        # Add divider
        blocks.append({"type": "divider"})
        
        # Build payload
        payload = {
            "attachments": [
                {
                    "color": config['color'],
                    "blocks": blocks
                }
            ]
        }
        
        # Send to Slack
        self._send_webhook(payload)
    
    def send_gush_reminder(self, gush_time: str, agenda_items: list):
        """Send GUSH session reminder"""
        items_text = '\n'.join([f"• {item}" for item in agenda_items])
        
        payload = {
            "attachments": [
                {
                    "color": "#f59e0b",
                    "blocks": [
                        {
                            "type": "header",
                            "text": {
                                "type": "plain_text",
                                "text": "🔔 GUSH Session Starting Soon",
                                "emoji": True
                            }
                        },
                        {
                            "type": "section",
                            "fields": [
                                {
                                    "type": "mrkdwn",
                                    "text": f"*Time:*\n{gush_time}"
                                },
                                {
                                    "type": "mrkdwn",
                                    "text": f"*Duration:*\n60-90 minutes"
                                }
                            ]
                        },
                        {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": f"*Agenda Items:*\n{items_text}"
                            }
                        },
                        {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": "*Rules:*\n• Camera ON\n• No multitasking\n• Decisions must be made\n• Timer enforcement"
                            }
                        }
                    ]
                }
            ]
        }
        
        self._send_webhook(payload)
    
    def send_blues_pulse(self, pulse_number: int, week_theme: str, highlights: list):
        """Send BLUES pulse notification"""
        highlights_text = '\n'.join([f"• {item}" for item in highlights])
        
        payload = {
            "attachments": [
                {
                    "color": "#8b5cf6",
                    "blocks": [
                        {
                            "type": "header",
                            "text": {
                                "type": "plain_text",
                                "text": f"🟣 BLUES Pulse #{pulse_number}",
                                "emoji": True
                            }
                        },
                        {
                            "type": "section",
                            "fields": [
                                {
                                    "type": "mrkdwn",
                                    "text": f"*Theme:*\n{week_theme}"
                                }
                            ]
                        },
                        {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": f"*This Week's Highlights:*\n{highlights_text}"
                            }
                        }
                    ]
                }
            ]
        }
        
        self._send_webhook(payload)
    
    def _send_webhook(self, payload: dict):
        """Internal method to send webhook request"""
        try:
            req = Request(self.webhook_url)
            req.add_header('Content-Type', 'application/json')
            data = json.dumps(payload).encode('utf-8')
            
            response = urlopen(req, data)
            
            if response.status == 200:
                print("✓ Slack notification sent successfully")
            else:
                print(f"✗ Slack returned status {response.status}")
                
        except URLError as e:
            print(f"✗ Failed to send Slack notification: {e}")
        except Exception as e:
            print(f"✗ Error: {e}")


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Send CIM Pattern notifications to Slack')
    parser.add_argument('--mode', choices=['STUDY_HALL', 'GUSH', 'JAM'], 
                       help='Current mode')
    parser.add_argument('--zc', type=float, help='Zc ratio value')
    parser.add_argument('--vgen', type=float, help='V_generation value')
    parser.add_argument('--bsocial', type=float, help='B_social value')
    parser.add_argument('--message', type=str, help='Custom message')
    parser.add_argument('--webhook', type=str, help='Slack webhook URL (or set SLACK_WEBHOOK_URL env var)')
    
    args = parser.parse_args()
    
    if not args.mode or args.zc is None:
        parser.print_help()
        return
    
    try:
        notifier = SlackNotifier(webhook_url=args.webhook)
        notifier.send_mode_switch(
            mode=args.mode,
            zc=args.zc,
            v_gen=args.vgen,
            b_social=args.bsocial,
            custom_message=args.message
        )
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
