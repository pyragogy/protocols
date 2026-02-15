"""
Curator AI - Recommendation Engine
Uses Claude API to generate personalized team advice

This module takes Zc analysis and generates context-aware
recommendations using Anthropic's Claude API.
"""

import os
import json
from typing import Dict, List, Optional
from dataclasses import dataclass
import logging

try:
    import anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False
    logging.warning("Anthropic SDK not installed. Install with: pip install anthropic")

from monitor import ZcResult, TeamMetrics

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class Recommendation:
    """Detailed recommendation from Curator AI"""
    summary: str
    immediate_actions: List[str]
    this_week: List[str]
    avoid: List[str]
    success_criteria: List[str]
    context: str


class CuratorRecommender:
    """
    Curator AI Recommendation Engine
    
    Generates personalized advice using Claude API based on:
    - Current Zc status
    - Historical trends
    - Team context
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize recommender
        
        Args:
            api_key: Anthropic API key (or use ANTHROPIC_API_KEY env var)
        """
        if not ANTHROPIC_AVAILABLE:
            raise ImportError("Anthropic SDK required. Install: pip install anthropic")
        
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError("Anthropic API key required (set ANTHROPIC_API_KEY env var)")
        
        self.client = anthropic.Anthropic(api_key=self.api_key)
        logger.info("Curator Recommender initialized")
    
    def generate_recommendation(self, 
                               result: ZcResult,
                               team_context: Optional[str] = None,
                               recent_history: Optional[List[ZcResult]] = None) -> Recommendation:
        """
        Generate personalized recommendation using Claude
        
        Args:
            result: Current Zc analysis
            team_context: Optional context about team (industry, size, etc.)
            recent_history: Optional recent Zc history
            
        Returns:
            Detailed Recommendation object
        """
        # Build context for Claude
        prompt = self._build_prompt(result, team_context, recent_history)
        
        # Call Claude API
        try:
            response = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=1000,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            # Extract recommendation
            content = response.content[0].text
            recommendation = self._parse_recommendation(content, result)
            
            logger.info("Recommendation generated successfully")
            return recommendation
            
        except Exception as e:
            logger.error(f"Error calling Claude API: {e}")
            # Fallback to basic recommendation
            return self._fallback_recommendation(result)
    
    def _build_prompt(self, 
                     result: ZcResult,
                     team_context: Optional[str],
                     history: Optional[List[ZcResult]]) -> str:
        """Build prompt for Claude"""
        
        prompt = f"""You are the Curator AI for the CIM Pattern (Cognitive Impedance Mismatch protocol).

A team needs your expert advice on managing cognitive load.

CURRENT STATUS:
- Zc Ratio: {result.zc}
- Zone: {result.zone}
- Mode: {result.mode}
- Trend: {result.trend}
- V_generation: {result.v_generation} items/hour
- B_social: {result.b_social} capacity/hour
"""
        
        if team_context:
            prompt += f"\nTEAM CONTEXT:\n{team_context}\n"
        
        if history and len(history) > 0:
            prompt += "\nRECENT HISTORY (last 7 days):\n"
            for h in history[-7:]:
                prompt += f"- {h.timestamp[:10]}: Zc={h.zc} ({h.zone})\n"
        
        prompt += """
TASK:
Generate a detailed, actionable recommendation for this team.

Respond ONLY with valid JSON in this exact format:
{
  "summary": "One sentence assessment",
  "immediate_actions": ["Action 1", "Action 2", "Action 3"],
  "this_week": ["Task 1", "Task 2"],
  "avoid": ["Anti-pattern 1", "Anti-pattern 2"],
  "success_criteria": ["Metric 1", "Metric 2"],
  "context": "Brief explanation of the recommendation rationale"
}

IMPORTANT:
- Be specific and actionable (no vague advice)
- Use CIM Pattern terminology (GUSH, BHO, BLUES, Study Hall)
- Consider the trend (is Zc improving or worsening?)
- Immediate actions should be doable today
- Success criteria should be measurable

Respond with ONLY the JSON, no preamble or markdown.
"""
        return prompt
    
    def _parse_recommendation(self, content: str, result: ZcResult) -> Recommendation:
        """Parse Claude's JSON response into Recommendation"""
        try:
            # Remove any markdown code fences
            content = content.replace("```json", "").replace("```", "").strip()
            
            data = json.loads(content)
            
            return Recommendation(
                summary=data.get("summary", result.recommendation),
                immediate_actions=data.get("immediate_actions", []),
                this_week=data.get("this_week", []),
                avoid=data.get("avoid", []),
                success_criteria=data.get("success_criteria", []),
                context=data.get("context", "")
            )
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse JSON: {e}")
            return self._fallback_recommendation(result)
    
    def _fallback_recommendation(self, result: ZcResult) -> Recommendation:
        """Fallback recommendation without Claude API"""
        
        recommendations_map = {
            "GREEN": Recommendation(
                summary="Team is in healthy Green Zone - continue async-first approach",
                immediate_actions=[
                    "Maintain current async workflows",
                    "Document what's working well",
                    "Share success patterns with team"
                ],
                this_week=[
                    "Weekly Zc check-in (15 min)",
                    "Update team documentation"
                ],
                avoid=[
                    "Don't add new sync meetings",
                    "Don't change what's working"
                ],
                success_criteria=[
                    "Zc stays below 0.7",
                    "Team reports low stress",
                    "Decisions made in <48h"
                ],
                context="Green zone indicates healthy cognitive load. No interventions needed."
            ),
            "YELLOW": Recommendation(
                summary="Team approaching overload - schedule GUSH session to force convergence",
                immediate_actions=[
                    "Schedule 90-min GUSH session within 48h",
                    "Identify 3-5 pending decisions",
                    "Share GUSH template with team"
                ],
                this_week=[
                    "Run GUSH session",
                    "Clear decision backlog",
                    "Re-measure Zc post-GUSH"
                ],
                avoid=[
                    "Don't defer decisions again",
                    "Don't schedule more async discussions"
                ],
                success_criteria=[
                    "Zc drops below 0.7",
                    "70%+ decisions closed",
                    "Team confidence >7/10"
                ],
                context="Yellow zone requires forced convergence via GUSH protocol."
            ),
            "RED": Recommendation(
                summary="Critical overload - activate The Jam immediately (BHO + BLUES)",
                immediate_actions=[
                    "Pause new initiatives for 48h",
                    "Declare BHO forks for deep work streams",
                    "Emergency GUSH for time-sensitive decisions"
                ],
                this_week=[
                    "Implement BLUES pulse rhythm",
                    "Weekly BHO merge events",
                    "Daily Zc monitoring"
                ],
                avoid=[
                    "Don't try to process everything",
                    "Don't add more people to threads"
                ],
                success_criteria=[
                    "Zc drops to Yellow zone",
                    "2-3 BHO forks active",
                    "BLUES rhythm established"
                ],
                context="Red zone means standard consensus broken. The Jam protocols are required."
            )
        }
        
        return recommendations_map.get(result.zone, recommendations_map["YELLOW"])
    
    def format_recommendation(self, rec: Recommendation) -> str:
        """Format recommendation for display"""
        output = []
        output.append("=" * 70)
        output.append("CURATOR AI RECOMMENDATION")
        output.append("=" * 70)
        output.append("")
        output.append(f"📝 SUMMARY")
        output.append(f"  {rec.summary}")
        output.append("")
        
        output.append(f"🚨 IMMEDIATE ACTIONS (Today)")
        for i, action in enumerate(rec.immediate_actions, 1):
            output.append(f"  {i}. {action}")
        output.append("")
        
        output.append(f"📅 THIS WEEK")
        for i, task in enumerate(rec.this_week, 1):
            output.append(f"  {i}. {task}")
        output.append("")
        
        output.append(f"❌ AVOID")
        for i, anti in enumerate(rec.avoid, 1):
            output.append(f"  {i}. {anti}")
        output.append("")
        
        output.append(f"✅ SUCCESS CRITERIA")
        for i, criteria in enumerate(rec.success_criteria, 1):
            output.append(f"  {i}. {criteria}")
        output.append("")
        
        if rec.context:
            output.append(f"💡 CONTEXT")
            output.append(f"  {rec.context}")
            output.append("")
        
        output.append("=" * 70)
        
        return "\n".join(output)


def main():
    """Example usage"""
    # Check if API key is available
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("⚠️  ANTHROPIC_API_KEY not set. Using fallback recommendations.")
        print("   Set API key to use Claude-powered recommendations.")
        print("")
    
    # Import monitor
    from monitor import CuratorMonitor, MetricsCollector
    
    # Simulate a team measurement
    monitor = CuratorMonitor(team_size=10)
    collector = MetricsCollector()
    
    metrics = collector.collect_manual(
        slack_messages=180,
        notion_updates=25,
        ai_outputs=40,
        emails=30
    )
    
    result = monitor.calculate_zc(metrics, timeframe_hours=24)
    
    # Generate recommendation
    try:
        recommender = CuratorRecommender(api_key=api_key)
        
        team_context = """
        - 10-person startup team
        - Heavy AI tool usage (Claude, Cursor)
        - Fully remote
        - Using Slack, Notion, Linear
        """
        
        recommendation = recommender.generate_recommendation(
            result=result,
            team_context=team_context
        )
    except (ImportError, ValueError) as e:
        print(f"Note: {e}")
        print("Using fallback recommendation.\n")
        recommender = CuratorRecommender(api_key="dummy")  # Will use fallback
        recommendation = recommender._fallback_recommendation(result)
    
    # Display
    print(recommender.format_recommendation(recommendation))


if __name__ == "__main__":
    main()
