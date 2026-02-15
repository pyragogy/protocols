"""
Curator AI - Monitoring Engine
Automated Zc calculation and mode detection for teams

This module monitors various data sources (Slack, Discord, Notion, etc.)
and calculates cognitive impedance in real-time.
"""

import time
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class TeamMetrics:
    """Team metrics snapshot"""
    timestamp: str
    slack_messages: int = 0
    discord_messages: int = 0
    notion_updates: int = 0
    github_events: int = 0
    linear_updates: int = 0
    ai_outputs: int = 0
    emails: int = 0
    
    def total_items(self) -> int:
        """Total information items generated"""
        return (self.slack_messages + self.discord_messages + 
                self.notion_updates + self.github_events + 
                self.linear_updates + self.ai_outputs + self.emails)


@dataclass
class ZcResult:
    """Zc calculation result with mode recommendation"""
    timestamp: str
    zc: float
    v_generation: float
    b_social: float
    zone: str  # GREEN, YELLOW, RED
    mode: str  # STUDY_HALL, GUSH, JAM
    confidence: float
    trend: str  # INCREASING, STABLE, DECREASING
    recommendation: str


class CuratorMonitor:
    """
    Curator AI Monitoring Engine
    
    Watches team activity across platforms and calculates Zc in real-time.
    """
    
    # Zone thresholds
    GREEN_THRESHOLD = 0.7
    YELLOW_THRESHOLD = 1.0
    
    # Trend detection window (hours)
    TREND_WINDOW = 24
    
    def __init__(self, team_size: int, processing_hours_per_person: float = 3.0):
        """
        Initialize monitor
        
        Args:
            team_size: Number of team members
            processing_hours_per_person: Effective processing capacity per person per day
        """
        self.team_size = team_size
        self.processing_hours_per_person = processing_hours_per_person
        self.history: List[ZcResult] = []
        
        logger.info(f"Curator Monitor initialized for team of {team_size}")
    
    def calculate_zc(self, metrics: TeamMetrics, 
                    timeframe_hours: int = 24) -> ZcResult:
        """
        Calculate Zc from team metrics
        
        Args:
            metrics: Team activity metrics
            timeframe_hours: Measurement window in hours
            
        Returns:
            ZcResult with full analysis
        """
        # Calculate V_generation (items per hour)
        total_items = metrics.total_items()
        v_generation = total_items / timeframe_hours
        
        # Calculate B_social (processing capacity per hour)
        # B_social = (team_size × processing_hours_per_person × 24) / timeframe_hours
        b_social = (self.team_size * self.processing_hours_per_person * 24) / timeframe_hours
        
        # Calculate Zc
        if b_social <= 0:
            raise ValueError("B_social must be greater than 0")
        
        zc = v_generation / b_social
        
        # Detect zone and mode
        zone, mode = self._detect_zone_and_mode(zc)
        
        # Analyze trend
        trend = self._analyze_trend()
        
        # Calculate confidence
        confidence = self._calculate_confidence(zc, trend)
        
        # Generate recommendation
        recommendation = self._generate_recommendation(zc, zone, mode, trend)
        
        # Create result
        result = ZcResult(
            timestamp=datetime.now().isoformat(),
            zc=round(zc, 2),
            v_generation=round(v_generation, 2),
            b_social=round(b_social, 2),
            zone=zone,
            mode=mode,
            confidence=confidence,
            trend=trend,
            recommendation=recommendation
        )
        
        # Store in history
        self.history.append(result)
        
        logger.info(f"Zc calculated: {zc:.2f} ({zone}) - {mode}")
        
        return result
    
    def _detect_zone_and_mode(self, zc: float) -> Tuple[str, str]:
        """Detect zone and recommend mode"""
        if zc < self.GREEN_THRESHOLD:
            return "GREEN", "STUDY_HALL"
        elif zc < self.YELLOW_THRESHOLD:
            return "YELLOW", "GUSH"
        else:
            return "RED", "JAM"
    
    def _analyze_trend(self) -> str:
        """Analyze Zc trend from recent history"""
        if len(self.history) < 3:
            return "STABLE"
        
        # Get recent results (last 3)
        recent = self.history[-3:]
        zc_values = [r.zc for r in recent]
        
        # Simple trend detection
        if zc_values[-1] > zc_values[-2] > zc_values[-3]:
            return "INCREASING"
        elif zc_values[-1] < zc_values[-2] < zc_values[-3]:
            return "DECREASING"
        else:
            return "STABLE"
    
    def _calculate_confidence(self, zc: float, trend: str) -> float:
        """
        Calculate confidence in the recommendation
        
        High confidence when:
        - Clear zone (far from thresholds)
        - Stable or decreasing trend
        
        Low confidence when:
        - Near threshold boundaries
        - Rapidly increasing trend
        """
        confidence = 0.8  # Base confidence
        
        # Adjust for zone clarity
        if self.GREEN_THRESHOLD - 0.1 <= zc <= self.GREEN_THRESHOLD + 0.1:
            confidence -= 0.2  # Near green/yellow boundary
        elif self.YELLOW_THRESHOLD - 0.1 <= zc <= self.YELLOW_THRESHOLD + 0.1:
            confidence -= 0.2  # Near yellow/red boundary
        
        # Adjust for trend
        if trend == "INCREASING":
            confidence -= 0.1
        elif trend == "DECREASING":
            confidence += 0.1
        
        return max(0.5, min(1.0, confidence))
    
    def _generate_recommendation(self, zc: float, zone: str, 
                                 mode: str, trend: str) -> str:
        """Generate actionable recommendation"""
        recommendations = {
            "GREEN": {
                "STABLE": "Continue with async-first workflows. Team is healthy.",
                "INCREASING": "Watch for early signs of overload. Monitor daily.",
                "DECREASING": "Great! Cognitive load is reducing. Keep current practices."
            },
            "YELLOW": {
                "STABLE": "Schedule GUSH session within 48h to force convergence on pending decisions.",
                "INCREASING": "URGENT: Schedule GUSH session within 24h. Zc is rising.",
                "DECREASING": "Good! Recent interventions working. One more GUSH to clear backlog."
            },
            "RED": {
                "STABLE": "Activate The Jam immediately. Declare BHO forks for deep work. Implement BLUES rhythm.",
                "INCREASING": "CRITICAL: Stop new initiatives. Emergency GUSH + immediate BHO declarations. Team at breaking point.",
                "DECREASING": "Progress! Continue The Jam protocols. Don't revert to async-only yet."
            }
        }
        
        return recommendations.get(zone, {}).get(trend, "Monitor closely and adjust mode as needed.")
    
    def get_history(self, hours: int = 168) -> List[ZcResult]:
        """
        Get historical Zc data
        
        Args:
            hours: How many hours of history to retrieve (default: 7 days)
            
        Returns:
            List of ZcResult objects
        """
        cutoff = datetime.now() - timedelta(hours=hours)
        return [
            r for r in self.history 
            if datetime.fromisoformat(r.timestamp) >= cutoff
        ]
    
    def export_history(self, filepath: str):
        """Export history to JSON file"""
        data = [asdict(r) for r in self.history]
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        logger.info(f"History exported to {filepath}")
    
    def import_history(self, filepath: str):
        """Import history from JSON file"""
        with open(filepath, 'r') as f:
            data = json.load(f)
        self.history = [ZcResult(**item) for item in data]
        logger.info(f"History imported from {filepath} ({len(data)} records)")


class MetricsCollector:
    """
    Collects metrics from various sources
    
    Currently supports:
    - Slack API
    - Discord API
    - Manual input (for other sources)
    """
    
    def __init__(self):
        self.collectors = {}
    
    def register_collector(self, name: str, collector_func):
        """Register a metrics collector function"""
        self.collectors[name] = collector_func
        logger.info(f"Registered collector: {name}")
    
    def collect(self) -> TeamMetrics:
        """
        Collect metrics from all registered sources
        
        Returns:
            TeamMetrics object with aggregated data
        """
        metrics = TeamMetrics(timestamp=datetime.now().isoformat())
        
        for name, collector in self.collectors.items():
            try:
                data = collector()
                # Update metrics with collected data
                for key, value in data.items():
                    if hasattr(metrics, key):
                        setattr(metrics, key, getattr(metrics, key) + value)
            except Exception as e:
                logger.error(f"Error collecting from {name}: {e}")
        
        return metrics
    
    def collect_manual(self, **kwargs) -> TeamMetrics:
        """
        Manually provide metrics
        
        Example:
            collector.collect_manual(
                slack_messages=150,
                notion_updates=20,
                ai_outputs=30
            )
        """
        metrics = TeamMetrics(timestamp=datetime.now().isoformat(), **kwargs)
        return metrics


def main():
    """Example usage"""
    # Initialize monitor
    monitor = CuratorMonitor(team_size=10, processing_hours_per_person=3.0)
    
    # Collect metrics (manual example)
    collector = MetricsCollector()
    metrics = collector.collect_manual(
        slack_messages=150,
        notion_updates=20,
        ai_outputs=30,
        emails=25
    )
    
    # Calculate Zc
    result = monitor.calculate_zc(metrics, timeframe_hours=24)
    
    # Print result
    print(f"\n{'='*60}")
    print(f"Curator AI - Monitoring Result")
    print(f"{'='*60}\n")
    print(f"Timestamp: {result.timestamp}")
    print(f"Zc Ratio: {result.zc}")
    print(f"Zone: {result.zone}")
    print(f"Mode: {result.mode}")
    print(f"Trend: {result.trend}")
    print(f"Confidence: {result.confidence:.0%}")
    print(f"\nRecommendation:")
    print(f"  {result.recommendation}\n")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
