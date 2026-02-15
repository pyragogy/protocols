"""
Slack Bot for CIM Pattern Curator AI

Provides slash commands and automated monitoring:
- /zc - Calculate current Zc
- /gush - Schedule GUSH session
- /fork - Declare BHO fork
- /status - Team status dashboard

Also sends automated notifications when zones change.
"""

import os
import json
import time
from datetime import datetime
from typing import Dict, List, Optional
import logging

try:
    from slack_sdk import WebClient
    from slack_sdk.errors import SlackApiError
    SLACK_SDK_AVAILABLE = True
except ImportError:
    SLACK_SDK_AVAILABLE = False
    logging.warning("Slack SDK not installed. Install with: pip install slack-sdk")

# Import curator modules (handle if not in path)
import sys
sys.path.insert(0, os.path.dirname(__file__) + '/../curator-ai')

from monitor import CuratorMonitor, MetricsCollector, TeamMetrics, ZcResult
from recommender import CuratorRecommender

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SlackBot:
    """
    Slack Bot for CIM Pattern Curator AI
    
    Provides real-time Zc monitoring and team commands.
    """
    
    def __init__(self, 
                 bot_token: str,
                 monitor: CuratorMonitor,
                 recommender: Optional[CuratorRecommender] = None):
        """
        Initialize Slack bot
        
        Args:
            bot_token: Slack Bot User OAuth Token
            monitor: CuratorMonitor instance
            recommender: Optional CuratorRecommender for AI advice
        """
        if not SLACK_SDK_AVAILABLE:
            raise ImportError("Slack SDK required. Install: pip install slack-sdk")
        
        self.client = WebClient(token=bot_token)
        self.monitor = monitor
        self.recommender = recommender
        self.last_zone = None  # Track zone changes
        
        logger.info("Slack Bot initialized")
    
    def get_channel_metrics(self, 
                           channel_ids: List[str],
                           hours: int = 24) -> TeamMetrics:
        """
        Collect metrics from Slack channels
        
        Args:
            channel_ids: List of channel IDs to monitor
            hours: Timeframe in hours
            
        Returns:
            TeamMetrics with Slack message counts
        """
        total_messages = 0
        oldest_timestamp = time.time() - (hours * 3600)
        
        for channel_id in channel_ids:
            try:
                response = self.client.conversations_history(
                    channel=channel_id,
                    oldest=oldest_timestamp
                )
                total_messages += len(response['messages'])
                
            except SlackApiError as e:
                logger.error(f"Error fetching messages from {channel_id}: {e}")
        
        return TeamMetrics(
            timestamp=datetime.now().isoformat(),
            slack_messages=total_messages
        )
    
    def send_message(self, channel: str, text: str, blocks: Optional[List] = None):
        """Send message to Slack channel"""
        try:
            self.client.chat_postMessage(
                channel=channel,
                text=text,
                blocks=blocks
            )
            logger.info(f"Message sent to {channel}")
        except SlackApiError as e:
            logger.error(f"Error sending message: {e}")
    
    def send_zc_status(self, channel: str, result: ZcResult):
        """Send formatted Zc status to channel"""
        
        # Color coding
        colors = {
            "GREEN": "#16a34a",
            "YELLOW": "#f59e0b",
            "RED": "#dc2626"
        }
        
        blocks = [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": f"🎯 Cognitive Impedance Status"
                }
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": f"*Zc Ratio:*\n`{result.zc}`"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"*Zone:*\n{result.zone}"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"*Mode:*\n{result.mode}"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"*Trend:*\n{result.trend}"
                    }
                ]
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*Recommendation:*\n{result.recommendation}"
                }
            }
        ]
        
        self.send_message(channel, f"Zc Status: {result.zc} ({result.zone})", blocks)
    
    def send_zone_change_alert(self, channel: str, old_zone: str, new_zone: str, result: ZcResult):
        """Send alert when zone changes"""
        
        emoji_map = {
            "GREEN": "🟢",
            "YELLOW": "🟡",
            "RED": "🔴"
        }
        
        text = f"{emoji_map.get(new_zone, '⚪')} Zone Change: {old_zone} → {new_zone}"
        
        blocks = [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": f"⚠️ Zone Change Alert"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"Cognitive load zone changed:\n*{old_zone} → {new_zone}*\n\nCurrent Zc: `{result.zc}`"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*Action Required:*\n{result.recommendation}"
                }
            }
        ]
        
        self.send_message(channel, text, blocks)
    
    def send_gush_reminder(self, channel: str, gush_time: str):
        """Send GUSH session reminder"""
        
        blocks = [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "🔔 GUSH Session Reminder"
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
                        "text": "*Duration:*\n60-90 minutes"
                    }
                ]
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Rules:*\n• Camera ON\n• No multitasking\n• Decisions MUST be made\n• Timer enforcement"
                }
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "View Template"
                        },
                        "url": "https://github.com/pyragogy/protocols/blob/main/tools/templates/GUSH-SESSION-TEMPLATE.md"
                    }
                ]
            }
        ]
        
        self.send_message(channel, f"GUSH Session at {gush_time}", blocks)
    
    def handle_slash_command(self, command: str, channel: str, user: str, **kwargs) -> str:
        """
        Handle slash commands
        
        Supported commands:
        - /zc - Calculate current Zc
        - /gush - Schedule GUSH session
        - /fork - Declare BHO fork
        - /status - Team status
        
        Returns:
            Response message
        """
        
        if command == "/zc":
            return self._handle_zc_command(channel, **kwargs)
        elif command == "/gush":
            return self._handle_gush_command(channel, user, **kwargs)
        elif command == "/fork":
            return self._handle_fork_command(channel, user, **kwargs)
        elif command == "/status":
            return self._handle_status_command(channel, **kwargs)
        else:
            return f"Unknown command: {command}"
    
    def _handle_zc_command(self, channel: str, **kwargs) -> str:
        """Handle /zc command"""
        # Collect metrics from Slack
        channel_ids = kwargs.get('channel_ids', [channel])
        metrics = self.get_channel_metrics(channel_ids)
        
        # Calculate Zc
        result = self.monitor.calculate_zc(metrics)
        
        # Send status
        self.send_zc_status(channel, result)
        
        # Check for zone change
        if self.last_zone and self.last_zone != result.zone:
            self.send_zone_change_alert(channel, self.last_zone, result.zone, result)
        
        self.last_zone = result.zone
        
        return "Zc calculated successfully"
    
    def _handle_gush_command(self, channel: str, user: str, **kwargs) -> str:
        """Handle /gush command"""
        time_arg = kwargs.get('time', 'tomorrow at 2pm')
        
        self.send_gush_reminder(channel, time_arg)
        
        return f"GUSH session scheduled for {time_arg}"
    
    def _handle_fork_command(self, channel: str, user: str, **kwargs) -> str:
        """Handle /fork command"""
        fork_name = kwargs.get('name', 'New Fork')
        
        blocks = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"🌿 *BHO Fork Declared*\n\nFork: {fork_name}\nOwner: <@{user}>\n\nUse the BHO template to structure your fork:\nhttps://github.com/pyragogy/protocols/blob/main/tools/templates/BHO-FORK-TEMPLATE.md"
                }
            }
        ]
        
        self.send_message(channel, f"BHO Fork: {fork_name}", blocks)
        
        return f"Fork '{fork_name}' declared"
    
    def _handle_status_command(self, channel: str, **kwargs) -> str:
        """Handle /status command"""
        # Get recent history
        history = self.monitor.get_history(hours=168)  # Last 7 days
        
        if not history:
            return "No history available yet. Run /zc to calculate Zc."
        
        # Calculate stats
        avg_zc = sum(r.zc for r in history) / len(history)
        current = history[-1]
        
        # Zone distribution
        zone_counts = {"GREEN": 0, "YELLOW": 0, "RED": 0}
        for r in history:
            zone_counts[r.zone] += 1
        
        blocks = [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "📊 Team Status (Last 7 Days)"
                }
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": f"*Current Zc:*\n{current.zc}"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"*Average Zc:*\n{avg_zc:.2f}"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"*Current Zone:*\n{current.zone}"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"*Trend:*\n{current.trend}"
                    }
                ]
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*Zone Distribution:*\n🟢 Green: {zone_counts['GREEN']} | 🟡 Yellow: {zone_counts['YELLOW']} | 🔴 Red: {zone_counts['RED']}"
                }
            }
        ]
        
        self.send_message(channel, "Team Status", blocks)
        
        return "Status sent"
    
    def monitor_loop(self, channel: str, interval_minutes: int = 60):
        """
        Continuous monitoring loop
        
        Calculates Zc at regular intervals and sends alerts on zone changes.
        
        Args:
            channel: Channel to send alerts to
            interval_minutes: How often to check Zc
        """
        logger.info(f"Starting monitoring loop (interval: {interval_minutes}min)")
        
        while True:
            try:
                # Calculate Zc
                self._handle_zc_command(channel)
                
                # Sleep
                time.sleep(interval_minutes * 60)
                
            except KeyboardInterrupt:
                logger.info("Monitoring stopped by user")
                break
            except Exception as e:
                logger.error(f"Error in monitoring loop: {e}")
                time.sleep(60)  # Wait 1 min before retry


def main():
    """Example usage"""
    # Configuration
    BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
    CHANNEL = os.environ.get("SLACK_CHANNEL", "#team")
    TEAM_SIZE = int(os.environ.get("TEAM_SIZE", "10"))
    
    if not BOT_TOKEN:
        print("Error: SLACK_BOT_TOKEN environment variable required")
        return
    
    # Initialize components
    monitor = CuratorMonitor(team_size=TEAM_SIZE)
    
    try:
        recommender = CuratorRecommender()
    except (ImportError, ValueError):
        recommender = None
        logger.warning("Recommender not available (no API key)")
    
    # Initialize bot
    bot = SlackBot(BOT_TOKEN, monitor, recommender)
    
    # Example: Calculate and send Zc
    print(f"Calculating Zc for {CHANNEL}...")
    bot._handle_zc_command(CHANNEL)
    
    # To run continuous monitoring:
    # bot.monitor_loop(CHANNEL, interval_minutes=60)


if __name__ == "__main__":
    main()
