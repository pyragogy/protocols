"""
Dashboard Backend API
FastAPI server for Curator AI dashboard

Endpoints:
- GET /api/zc/current - Current Zc status
- GET /api/zc/history - Historical Zc data
- POST /api/zc/calculate - Calculate Zc from metrics
- GET /api/recommendations - Get AI recommendations
- GET /api/health - Health check
"""

import os
import json
from datetime import datetime, timedelta
from typing import List, Optional
from pydantic import BaseModel

try:
    from fastapi import FastAPI, HTTPException, Query
    from fastapi.middleware.cors import CORSMiddleware
    import uvicorn
    FASTAPI_AVAILABLE = True
except ImportError:
    FASTAPI_AVAILABLE = False
    print("FastAPI not installed. Install with: pip install fastapi uvicorn")

# Import curator modules
import sys
sys.path.insert(0, os.path.dirname(__file__) + '/../../curator-ai')

from monitor import CuratorMonitor, MetricsCollector, TeamMetrics, ZcResult
from recommender import CuratorRecommender, Recommendation


# Pydantic models for API
class MetricsInput(BaseModel):
    slack_messages: int = 0
    discord_messages: int = 0
    notion_updates: int = 0
    github_events: int = 0
    linear_updates: int = 0
    ai_outputs: int = 0
    emails: int = 0
    timeframe_hours: int = 24


class ZcResponse(BaseModel):
    timestamp: str
    zc: float
    v_generation: float
    b_social: float
    zone: str
    mode: str
    confidence: float
    trend: str
    recommendation: str


class HistoryResponse(BaseModel):
    data: List[ZcResponse]
    count: int


class RecommendationResponse(BaseModel):
    summary: str
    immediate_actions: List[str]
    this_week: List[str]
    avoid: List[str]
    success_criteria: List[str]
    context: str


class HealthResponse(BaseModel):
    status: str
    version: str
    team_size: int
    monitor_active: bool
    recommender_active: bool


# Initialize FastAPI app
if FASTAPI_AVAILABLE:
    app = FastAPI(
        title="Curator AI Dashboard API",
        version="3.0.0",
        description="Real-time cognitive impedance monitoring"
    )
    
    # CORS middleware for React frontend
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # In production, restrict to your domain
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Global instances (initialized on startup)
    monitor: Optional[CuratorMonitor] = None
    recommender: Optional[CuratorRecommender] = None
    
    
    @app.on_event("startup")
    async def startup_event():
        """Initialize curator components"""
        global monitor, recommender
        
        team_size = int(os.environ.get("TEAM_SIZE", "10"))
        monitor = CuratorMonitor(team_size=team_size)
        
        try:
            recommender = CuratorRecommender()
            print("✓ Recommender initialized with Claude API")
        except (ImportError, ValueError) as e:
            print(f"⚠ Recommender not available: {e}")
            recommender = None
        
        print(f"✓ Dashboard API started (team size: {team_size})")
    
    
    @app.get("/")
    async def root():
        """Root endpoint"""
        return {
            "message": "Curator AI Dashboard API",
            "version": "3.0.0",
            "docs": "/docs"
        }
    
    
    @app.get("/api/health", response_model=HealthResponse)
    async def health_check():
        """Health check endpoint"""
        return HealthResponse(
            status="healthy",
            version="3.0.0",
            team_size=monitor.team_size if monitor else 0,
            monitor_active=monitor is not None,
            recommender_active=recommender is not None
        )
    
    
    @app.get("/api/zc/current", response_model=Optional[ZcResponse])
    async def get_current_zc():
        """Get current Zc status"""
        if not monitor or len(monitor.history) == 0:
            return None
        
        current = monitor.history[-1]
        return ZcResponse(**current.__dict__)
    
    
    @app.get("/api/zc/history", response_model=HistoryResponse)
    async def get_zc_history(
        hours: int = Query(168, description="Hours of history to retrieve (default: 7 days)")
    ):
        """Get historical Zc data"""
        if not monitor:
            raise HTTPException(status_code=500, detail="Monitor not initialized")
        
        history = monitor.get_history(hours=hours)
        
        return HistoryResponse(
            data=[ZcResponse(**r.__dict__) for r in history],
            count=len(history)
        )
    
    
    @app.post("/api/zc/calculate", response_model=ZcResponse)
    async def calculate_zc(metrics: MetricsInput):
        """Calculate Zc from provided metrics"""
        if not monitor:
            raise HTTPException(status_code=500, detail="Monitor not initialized")
        
        # Create TeamMetrics from input
        team_metrics = TeamMetrics(
            timestamp=datetime.now().isoformat(),
            slack_messages=metrics.slack_messages,
            discord_messages=metrics.discord_messages,
            notion_updates=metrics.notion_updates,
            github_events=metrics.github_events,
            linear_updates=metrics.linear_updates,
            ai_outputs=metrics.ai_outputs,
            emails=metrics.emails
        )
        
        # Calculate Zc
        result = monitor.calculate_zc(team_metrics, timeframe_hours=metrics.timeframe_hours)
        
        return ZcResponse(**result.__dict__)
    
    
    @app.get("/api/recommendations", response_model=RecommendationResponse)
    async def get_recommendations(
        team_context: Optional[str] = Query(None, description="Team context for personalized advice")
    ):
        """Get AI-powered recommendations"""
        if not monitor or len(monitor.history) == 0:
            raise HTTPException(status_code=404, detail="No Zc data available")
        
        current = monitor.history[-1]
        recent_history = monitor.get_history(hours=168)
        
        if recommender:
            # Use Claude API
            rec = recommender.generate_recommendation(
                result=current,
                team_context=team_context,
                recent_history=recent_history
            )
        else:
            # Fallback
            rec = CuratorRecommender._fallback_recommendation(None, current)
        
        return RecommendationResponse(**rec.__dict__)
    
    
    @app.get("/api/stats/summary")
    async def get_summary_stats():
        """Get summary statistics"""
        if not monitor or len(monitor.history) == 0:
            return {
                "avg_zc": 0,
                "current_zc": 0,
                "zone_distribution": {"GREEN": 0, "YELLOW": 0, "RED": 0},
                "trend": "STABLE"
            }
        
        history = monitor.get_history(hours=168)
        
        # Calculate stats
        avg_zc = sum(r.zc for r in history) / len(history)
        current = history[-1]
        
        # Zone distribution
        zone_counts = {"GREEN": 0, "YELLOW": 0, "RED": 0}
        for r in history:
            zone_counts[r.zone] += 1
        
        return {
            "avg_zc": round(avg_zc, 2),
            "current_zc": current.zc,
            "current_zone": current.zone,
            "trend": current.trend,
            "zone_distribution": zone_counts,
            "data_points": len(history)
        }


def main():
    """Run the API server"""
    if not FASTAPI_AVAILABLE:
        print("Error: FastAPI required. Install with: pip install fastapi uvicorn")
        return
    
    # Configuration
    host = os.environ.get("API_HOST", "0.0.0.0")
    port = int(os.environ.get("API_PORT", "8000"))
    
    print(f"Starting Curator AI Dashboard API...")
    print(f"Server: http://{host}:{port}")
    print(f"Docs: http://{host}:{port}/docs")
    
    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    main()
