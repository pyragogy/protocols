"""
Discord Bot for CIM Pattern Curator AI

Provides commands and automated monitoring:
- !zc - Calculate current Zc
- !gush - Schedule GUSH session
- !fork - Declare BHO fork
- !status - Team status dashboard

Also sends automated notifications when zones change.
"""

import os
import asyncio
from datetime import datetime
from typing import Optional
import logging

try:
    import discord
    from discord.ext import commands, tasks
    DISCORD_PY_AVAILABLE = True
except ImportError:
    DISCORD_PY_AVAILABLE = False
    logging.warning("discord.py not installed. Install with: pip install discord.py")

# Import curator modules
import sys
sys.path.insert(0, os.path.dirname(__file__) + '/../../curator-ai')

from monitor import CuratorMonitor, MetricsCollector, TeamMetrics, ZcResult
from recommender import CuratorRecommender

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CuratorBot(commands.Bot):
    """
    Discord Bot for CIM Pattern Curator AI
    
    Provides real-time Zc monitoring and team commands.
    """
    
    def __init__(self, 
                 monitor: CuratorMonitor,
                 recommender: Optional[CuratorRecommender] = None):
        """
        Initialize Discord bot
        
        Args:
            monitor: CuratorMonitor instance
            recommender: Optional CuratorRecommender for AI advice
        """
        if not DISCORD_PY_AVAILABLE:
            raise ImportError("discord.py required. Install: pip install discord.py")
        
        intents = discord.Intents.default()
        intents.message_content = True
        intents.messages = True
        
        super().__init__(command_prefix='!', intents=intents)
        
        self.curator_monitor = monitor
        self.curator_recommender = recommender
        self.last_zone = None
        self.monitoring_channel = None
        
        # Register commands
        self._register_commands()
        
        logger.info("Discord Bot initialized")
    
    def _register_commands(self):
        """Register bot commands"""
        
        @self.command(name='zc', help='Calculate current cognitive impedance')
        async def zc_command(ctx):
            await self._handle_zc(ctx)
        
        @self.command(name='gush', help='Schedule a GUSH session')
        async def gush_command(ctx, *, time: str = "tomorrow at 2pm"):
            await self._handle_gush(ctx, time)
        
        @self.command(name='fork', help='Declare a BHO fork')
        async def fork_command(ctx, *, name: str = "New Fork"):
            await self._handle_fork(ctx, name)
        
        @self.command(name='status', help='Show team status')
        async def status_command(ctx):
            await self._handle_status(ctx)
    
    async def on_ready(self):
        """Called when bot is ready"""
        logger.info(f'Bot logged in as {self.user}')
        
        # Start monitoring loop
        if not self.monitor_loop.is_running():
            self.monitor_loop.start()
    
    async def get_channel_metrics(self, channel_id: int, hours: int = 24) -> TeamMetrics:
        """
        Collect metrics from Discord channel
        
        Args:
            channel_id: Channel ID to monitor
            hours: Timeframe in hours
            
        Returns:
            TeamMetrics with Discord message counts
        """
        channel = self.get_channel(channel_id)
        if not channel:
            return TeamMetrics(timestamp=datetime.now().isoformat())
        
        # Count messages in timeframe
        after = datetime.now() - timedelta(hours=hours)
        message_count = 0
        
        async for message in channel.history(after=after, limit=None):
            message_count += 1
        
        return TeamMetrics(
            timestamp=datetime.now().isoformat(),
            discord_messages=message_count
        )
    
    async def send_zc_status(self, channel, result: ZcResult):
        """Send formatted Zc status to channel"""
        
        # Color coding
        colors = {
            "GREEN": 0x16a34a,
            "YELLOW": 0xf59e0b,
            "RED": 0xdc2626
        }
        
        embed = discord.Embed(
            title="🎯 Cognitive Impedance Status",
            color=colors.get(result.zone, 0x808080),
            timestamp=datetime.now()
        )
        
        embed.add_field(name="Zc Ratio", value=f"`{result.zc}`", inline=True)
        embed.add_field(name="Zone", value=result.zone, inline=True)
        embed.add_field(name="Mode", value=result.mode, inline=True)
        embed.add_field(name="Trend", value=result.trend, inline=True)
        
        embed.add_field(
            name="Recommendation",
            value=result.recommendation,
            inline=False
        )
        
        await channel.send(embed=embed)
    
    async def send_zone_change_alert(self, channel, old_zone: str, new_zone: str, result: ZcResult):
        """Send alert when zone changes"""
        
        emoji_map = {
            "GREEN": "🟢",
            "YELLOW": "🟡",
            "RED": "🔴"
        }
        
        colors = {
            "GREEN": 0x16a34a,
            "YELLOW": 0xf59e0b,
            "RED": 0xdc2626
        }
        
        embed = discord.Embed(
            title=f"⚠️ Zone Change Alert",
            description=f"Cognitive load zone changed:\n**{old_zone} → {new_zone}**\n\nCurrent Zc: `{result.zc}`",
            color=colors.get(new_zone, 0x808080),
            timestamp=datetime.now()
        )
        
        embed.add_field(
            name="Action Required",
            value=result.recommendation,
            inline=False
        )
        
        await channel.send(embed=embed)
    
    async def send_gush_reminder(self, channel, gush_time: str):
        """Send GUSH session reminder"""
        
        embed = discord.Embed(
            title="🔔 GUSH Session Reminder",
            color=0xf59e0b,
            timestamp=datetime.now()
        )
        
        embed.add_field(name="Time", value=gush_time, inline=True)
        embed.add_field(name="Duration", value="60-90 minutes", inline=True)
        
        embed.add_field(
            name="Rules",
            value="• Camera ON\n• No multitasking\n• Decisions MUST be made\n• Timer enforcement",
            inline=False
        )
        
        embed.add_field(
            name="Template",
            value="[View GUSH Template](https://github.com/pyragogy/protocols/blob/main/tools/templates/GUSH-SESSION-TEMPLATE.md)",
            inline=False
        )
        
        await channel.send(embed=embed)
    
    async def _handle_zc(self, ctx):
        """Handle !zc command"""
        await ctx.send("Calculating Zc...")
        
        # Collect metrics from Discord
        metrics = await self.get_channel_metrics(ctx.channel.id)
        
        # Calculate Zc
        result = self.curator_monitor.calculate_zc(metrics)
        
        # Send status
        await self.send_zc_status(ctx.channel, result)
        
        # Check for zone change
        if self.last_zone and self.last_zone != result.zone:
            await self.send_zone_change_alert(ctx.channel, self.last_zone, result.zone, result)
        
        self.last_zone = result.zone
    
    async def _handle_gush(self, ctx, time: str):
        """Handle !gush command"""
        await self.send_gush_reminder(ctx.channel, time)
        await ctx.send(f"✅ GUSH session scheduled for {time}")
    
    async def _handle_fork(self, ctx, name: str):
        """Handle !fork command"""
        
        embed = discord.Embed(
            title="🌿 BHO Fork Declared",
            color=0x8b5cf6,
            timestamp=datetime.now()
        )
        
        embed.add_field(name="Fork Name", value=name, inline=True)
        embed.add_field(name="Owner", value=ctx.author.mention, inline=True)
        
        embed.add_field(
            name="Template",
            value="[View BHO Template](https://github.com/pyragogy/protocols/blob/main/tools/templates/BHO-FORK-TEMPLATE.md)",
            inline=False
        )
        
        await ctx.send(embed=embed)
    
    async def _handle_status(self, ctx):
        """Handle !status command"""
        # Get recent history
        history = self.curator_monitor.get_history(hours=168)  # Last 7 days
        
        if not history:
            await ctx.send("No history available yet. Run `!zc` to calculate Zc.")
            return
        
        # Calculate stats
        avg_zc = sum(r.zc for r in history) / len(history)
        current = history[-1]
        
        # Zone distribution
        zone_counts = {"GREEN": 0, "YELLOW": 0, "RED": 0}
        for r in history:
            zone_counts[r.zone] += 1
        
        embed = discord.Embed(
            title="📊 Team Status (Last 7 Days)",
            color=0x3b82f6,
            timestamp=datetime.now()
        )
        
        embed.add_field(name="Current Zc", value=f"{current.zc}", inline=True)
        embed.add_field(name="Average Zc", value=f"{avg_zc:.2f}", inline=True)
        embed.add_field(name="Current Zone", value=current.zone, inline=True)
        embed.add_field(name="Trend", value=current.trend, inline=True)
        
        embed.add_field(
            name="Zone Distribution",
            value=f"🟢 Green: {zone_counts['GREEN']} | 🟡 Yellow: {zone_counts['YELLOW']} | 🔴 Red: {zone_counts['RED']}",
            inline=False
        )
        
        await ctx.send(embed=embed)
    
    @tasks.loop(minutes=60)
    async def monitor_loop(self):
        """
        Continuous monitoring loop
        
        Calculates Zc every hour and sends alerts on zone changes.
        """
        if not self.monitoring_channel:
            return
        
        try:
            channel = self.get_channel(self.monitoring_channel)
            if channel:
                # Collect metrics
                metrics = await self.get_channel_metrics(self.monitoring_channel)
                
                # Calculate Zc
                result = self.curator_monitor.calculate_zc(metrics)
                
                # Check for zone change
                if self.last_zone and self.last_zone != result.zone:
                    await self.send_zone_change_alert(channel, self.last_zone, result.zone, result)
                
                self.last_zone = result.zone
                
        except Exception as e:
            logger.error(f"Error in monitoring loop: {e}")


def main():
    """Run the bot"""
    # Configuration
    BOT_TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
    TEAM_SIZE = int(os.environ.get("TEAM_SIZE", "10"))
    
    if not BOT_TOKEN:
        print("Error: DISCORD_BOT_TOKEN environment variable required")
        return
    
    # Initialize components
    monitor = CuratorMonitor(team_size=TEAM_SIZE)
    
    try:
        recommender = CuratorRecommender()
    except (ImportError, ValueError):
        recommender = None
        logger.warning("Recommender not available (no API key)")
    
    # Initialize and run bot
    bot = CuratorBot(monitor, recommender)
    
    print("Starting Discord bot...")
    print("Commands: !zc, !gush, !fork, !status")
    
    bot.run(BOT_TOKEN)


if __name__ == "__main__":
    # Need to add import for timedelta
    from datetime import timedelta
    main()
