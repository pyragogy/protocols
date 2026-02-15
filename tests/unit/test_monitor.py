"""
Unit Tests for Curator AI Monitor

Run with: pytest tests/unit/test_monitor.py
"""

import pytest
from datetime import datetime
import sys
import os

# Add curator-ai to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../tools/curator-ai'))

from monitor import CuratorMonitor, MetricsCollector, TeamMetrics, ZcResult


class TestZcCalculation:
    """Test Zc calculation logic"""
    
    def test_basic_zc_calculation(self):
        """Test basic Zc calculation"""
        monitor = CuratorMonitor(team_size=10, processing_hours_per_person=3.0)
        
        metrics = TeamMetrics(
            timestamp=datetime.now().isoformat(),
            slack_messages=150,
            notion_updates=20,
            ai_outputs=30
        )
        
        result = monitor.calculate_zc(metrics, timeframe_hours=24)
        
        # V_generation = 200 items / 24 hours = 8.33 items/hour
        # B_social = 10 people × 3 hours = 30 capacity/hour
        # Zc = 8.33 / 30 = 0.28
        
        assert result.zc == pytest.approx(0.28, rel=0.01)
        assert result.zone == "GREEN"
        assert result.mode == "STUDY_HALL"
    
    def test_yellow_zone_detection(self):
        """Test Yellow zone detection (Zc 0.7-1.0)"""
        monitor = CuratorMonitor(team_size=10)
        
        metrics = TeamMetrics(
            timestamp=datetime.now().isoformat(),
            slack_messages=250  # High message count
        )
        
        result = monitor.calculate_zc(metrics, timeframe_hours=24)
        
        # Zc should be in Yellow zone
        assert 0.7 <= result.zc < 1.0
        assert result.zone == "YELLOW"
        assert result.mode == "GUSH"
    
    def test_red_zone_detection(self):
        """Test Red zone detection (Zc >= 1.0)"""
        monitor = CuratorMonitor(team_size=5, processing_hours_per_person=2.0)
        
        metrics = TeamMetrics(
            timestamp=datetime.now().isoformat(),
            slack_messages=300,
            ai_outputs=50
        )
        
        result = monitor.calculate_zc(metrics, timeframe_hours=24)
        
        # Zc should be in Red zone
        assert result.zc >= 1.0
        assert result.zone == "RED"
        assert result.mode == "JAM"
    
    def test_zero_b_social_raises_error(self):
        """Test that zero B_social raises ValueError"""
        monitor = CuratorMonitor(team_size=0)  # Results in B_social = 0
        
        metrics = TeamMetrics(
            timestamp=datetime.now().isoformat(),
            slack_messages=100
        )
        
        with pytest.raises(ValueError):
            monitor.calculate_zc(metrics)


class TestTrendDetection:
    """Test trend detection logic"""
    
    def test_increasing_trend(self):
        """Test detection of increasing Zc trend"""
        monitor = CuratorMonitor(team_size=10)
        
        # Simulate increasing Zc over time
        for zc_value in [0.4, 0.6, 0.8]:
            metrics = TeamMetrics(
                timestamp=datetime.now().isoformat(),
                slack_messages=int(zc_value * 300)
            )
            monitor.calculate_zc(metrics)
        
        # Last result should show INCREASING trend
        assert monitor.history[-1].trend == "INCREASING"
    
    def test_decreasing_trend(self):
        """Test detection of decreasing Zc trend"""
        monitor = CuratorMonitor(team_size=10)
        
        # Simulate decreasing Zc over time
        for zc_value in [0.8, 0.6, 0.4]:
            metrics = TeamMetrics(
                timestamp=datetime.now().isoformat(),
                slack_messages=int(zc_value * 300)
            )
            monitor.calculate_zc(metrics)
        
        # Last result should show DECREASING trend
        assert monitor.history[-1].trend == "DECREASING"
    
    def test_stable_trend(self):
        """Test detection of stable Zc trend"""
        monitor = CuratorMonitor(team_size=10)
        
        # Simulate stable Zc over time
        for _ in range(3):
            metrics = TeamMetrics(
                timestamp=datetime.now().isoformat(),
                slack_messages=150
            )
            monitor.calculate_zc(metrics)
        
        # Last result should show STABLE trend
        assert monitor.history[-1].trend == "STABLE"


class TestMetricsCollector:
    """Test MetricsCollector"""
    
    def test_manual_collection(self):
        """Test manual metrics collection"""
        collector = MetricsCollector()
        
        metrics = collector.collect_manual(
            slack_messages=100,
            notion_updates=10
        )
        
        assert metrics.slack_messages == 100
        assert metrics.notion_updates == 10
        assert metrics.total_items() == 110
    
    def test_collector_registration(self):
        """Test collector registration"""
        collector = MetricsCollector()
        
        def dummy_collector():
            return {"slack_messages": 50}
        
        collector.register_collector("test", dummy_collector)
        
        assert "test" in collector.collectors


class TestHistoryManagement:
    """Test history storage and retrieval"""
    
    def test_history_storage(self):
        """Test that calculations are stored in history"""
        monitor = CuratorMonitor(team_size=10)
        
        metrics = TeamMetrics(
            timestamp=datetime.now().isoformat(),
            slack_messages=100
        )
        
        monitor.calculate_zc(metrics)
        
        assert len(monitor.history) == 1
        assert monitor.history[0].zc > 0
    
    def test_get_recent_history(self):
        """Test retrieval of recent history"""
        monitor = CuratorMonitor(team_size=10)
        
        # Add 5 calculations
        for _ in range(5):
            metrics = TeamMetrics(
                timestamp=datetime.now().isoformat(),
                slack_messages=100
            )
            monitor.calculate_zc(metrics)
        
        recent = monitor.get_history(hours=168)
        
        assert len(recent) == 5


class TestRecommendations:
    """Test recommendation generation"""
    
    def test_green_zone_recommendation(self):
        """Test recommendation for Green zone"""
        monitor = CuratorMonitor(team_size=10)
        
        metrics = TeamMetrics(
            timestamp=datetime.now().isoformat(),
            slack_messages=50  # Low
        )
        
        result = monitor.calculate_zc(metrics)
        
        assert "async" in result.recommendation.lower()
        assert result.zone == "GREEN"
    
    def test_yellow_zone_recommendation(self):
        """Test recommendation for Yellow zone"""
        monitor = CuratorMonitor(team_size=10)
        
        metrics = TeamMetrics(
            timestamp=datetime.now().isoformat(),
            slack_messages=250  # Medium-high
        )
        
        result = monitor.calculate_zc(metrics)
        
        assert "gush" in result.recommendation.lower()
        assert result.zone == "YELLOW"
    
    def test_red_zone_recommendation(self):
        """Test recommendation for Red zone"""
        monitor = CuratorMonitor(team_size=5, processing_hours_per_person=2.0)
        
        metrics = TeamMetrics(
            timestamp=datetime.now().isoformat(),
            slack_messages=300,
            ai_outputs=50
        )
        
        result = monitor.calculate_zc(metrics)
        
        assert ("jam" in result.recommendation.lower() or 
                "bho" in result.recommendation.lower())
        assert result.zone == "RED"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
