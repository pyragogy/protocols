# Architecture - Curator AI

**Version:** 3.0.0  
**Last Updated:** February 14, 2026

This document describes the technical architecture of the CIM Pattern Curator AI system.

---

## System Overview

```
┌─────────────────────────────────────────────────────────┐
│                      Frontend                            │
│  (React Dashboard - Port 3000)                          │
│  - Real-time Zc visualization                           │
│  - Historical charts                                     │
│  - AI recommendations display                            │
└────────────────┬────────────────────────────────────────┘
                 │
                 │ HTTP/REST
                 ▼
┌─────────────────────────────────────────────────────────┐
│              Backend API (FastAPI - Port 8000)           │
│  - /api/zc/*            - Zc calculations               │
│  - /api/recommendations  - AI-powered advice            │
│  - /api/stats/*         - Summary statistics            │
└────────┬────────────────┬─────────────────┬─────────────┘
         │                │                 │
         │                │                 │
         ▼                ▼                 ▼
┌────────────────┐ ┌──────────────┐ ┌──────────────────┐
│ Curator Monitor│ │ Recommender  │ │ Metrics Collector│
│                │ │              │ │                  │
│ - Zc calc      │ │ - Claude API │ │ - Slack API      │
│ - Trend detect │ │ - Advice gen │ │ - Discord API    │
│ - History mgmt │ │ - Fallback   │ │ - Custom sources │
└────────────────┘ └──────────────┘ └──────────────────┘
         │                │                 │
         │                │                 │
         ▼                ▼                 ▼
┌─────────────────────────────────────────────────────────┐
│              External Services                           │
│  - Anthropic Claude API (recommendations)               │
│  - Slack API (message monitoring, bot commands)         │
│  - Discord API (message monitoring, bot commands)       │
│  - Notion/Linear/etc (future integrations)              │
└─────────────────────────────────────────────────────────┘
```

---

## Core Components

### 1. Curator Monitor (`tools/curator-ai/monitor.py`)

**Purpose:** Core Zc calculation and monitoring engine

**Responsibilities:**
- Calculate Zc from TeamMetrics
- Detect zone (GREEN/YELLOW/RED)
- Recommend mode (STUDY_HALL/GUSH/JAM)
- Track historical data
- Analyze trends

**Key Classes:**

```python
class CuratorMonitor:
    - calculate_zc(metrics, timeframe_hours) -> ZcResult
    - get_history(hours) -> List[ZcResult]
    - export_history(filepath)
    - import_history(filepath)

class TeamMetrics:
    - slack_messages: int
    - discord_messages: int
    - notion_updates: int
    - github_events: int
    - ... (extensible)
    - total_items() -> int

class ZcResult:
    - timestamp: str
    - zc: float
    - v_generation: float
    - b_social: float
    - zone: str
    - mode: str
    - confidence: float
    - trend: str
    - recommendation: str
```

**Algorithm:**

```python
V_generation = total_items / timeframe_hours
B_social = (team_size × processing_hours_per_person × 24) / timeframe_hours
Zc = V_generation / B_social

if Zc < 0.7:
    zone = GREEN, mode = STUDY_HALL
elif Zc < 1.0:
    zone = YELLOW, mode = GUSH
else:
    zone = RED, mode = JAM
```

---

### 2. Curator Recommender (`tools/curator-ai/recommender.py`)

**Purpose:** Generate personalized AI-powered recommendations

**Responsibilities:**
- Call Claude API with context
- Parse JSON recommendations
- Fallback to rule-based recommendations if API unavailable

**Key Classes:**

```python
class CuratorRecommender:
    - generate_recommendation(result, team_context, history) -> Recommendation
    - format_recommendation(rec) -> str

class Recommendation:
    - summary: str
    - immediate_actions: List[str]
    - this_week: List[str]
    - avoid: List[str]
    - success_criteria: List[str]
    - context: str
```

**Claude API Integration:**

```python
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1000,
    messages=[{"role": "user", "content": prompt}]
)
```

Prompt includes:
- Current Zc status
- Team context (optional)
- Recent history (last 7 days)

Response is JSON with structured recommendations.

---

### 3. Slack Bot (`tools/integrations/slack/bot.py`)

**Purpose:** Slack integration for monitoring and commands

**Features:**
- **Slash Commands:**
  - `/zc` - Calculate current Zc
  - `/gush [time]` - Schedule GUSH session
  - `/fork [name]` - Declare BHO fork
  - `/status` - Team status dashboard

- **Automated Monitoring:**
  - Periodic Zc calculation (configurable interval)
  - Zone change alerts
  - Automatic recommendations

**Key Classes:**

```python
class SlackBot:
    - get_channel_metrics(channel_ids, hours) -> TeamMetrics
    - send_message(channel, text, blocks)
    - send_zc_status(channel, result)
    - send_zone_change_alert(channel, old_zone, new_zone, result)
    - monitor_loop(channel, interval_minutes)
```

**Architecture:**

```
User: /zc
  ↓
Slack API → SlackBot.handle_slash_command()
  ↓
SlackBot.get_channel_metrics() → Slack API (fetch messages)
  ↓
CuratorMonitor.calculate_zc(metrics)
  ↓
SlackBot.send_zc_status(channel, result)
  ↓
Slack API → User sees formatted message
```

---

### 4. Discord Bot (`tools/integrations/discord/bot.py`)

**Purpose:** Discord integration (parallel to Slack)

**Features:**
- **Commands:**
  - `!zc` - Calculate current Zc
  - `!gush [time]` - Schedule GUSH session
  - `!fork [name]` - Declare BHO fork
  - `!status` - Team status

- **Automated Monitoring:**
  - Periodic Zc calculation
  - Zone change alerts

**Key Classes:**

```python
class CuratorBot(commands.Bot):
    - get_channel_metrics(channel_id, hours) -> TeamMetrics
    - send_zc_status(channel, result)
    - send_zone_change_alert(channel, old_zone, new_zone, result)
    - monitor_loop() # Background task
```

---

### 5. Dashboard Backend (`tools/dashboard/backend/api.py`)

**Purpose:** REST API for React dashboard

**Tech Stack:**
- FastAPI (async Python web framework)
- Pydantic (data validation)
- Uvicorn (ASGI server)

**Endpoints:**

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/health` | GET | Health check |
| `/api/zc/current` | GET | Current Zc status |
| `/api/zc/history` | GET | Historical data |
| `/api/zc/calculate` | POST | Calculate Zc |
| `/api/recommendations` | GET | AI recommendations |
| `/api/stats/summary` | GET | Summary stats |

**Data Flow:**

```
React Dashboard → API Request
  ↓
FastAPI endpoint handler
  ↓
CuratorMonitor.calculate_zc() / get_history()
  ↓
Return JSON response
  ↓
React Dashboard updates UI
```

---

### 6. Dashboard Frontend (`tools/dashboard/frontend/`)

**Purpose:** Real-time web dashboard

**Tech Stack:**
- React 18
- Recharts (data visualization)
- Axios (HTTP client)

**Components:**

```
App.js
├── ZcGauge.js          # Current Zc visualization
├── HistoryChart.js     # 7-day trend chart
├── StatsPanel.js       # Summary statistics
└── Recommendations.js  # AI advice display
```

**State Management:**

```javascript
const [currentZc, setCurrentZc] = useState(null);
const [history, setHistory] = useState([]);
const [stats, setStats] = useState(null);

useEffect(() => {
  fetchData();
  const interval = setInterval(fetchData, 60000); // 1 min
}, []);
```

**API Calls:**

```javascript
fetch('/api/zc/current')
fetch('/api/zc/history?hours=168')
fetch('/api/stats/summary')
fetch('/api/recommendations')
```

---

## Data Flow

### Typical Usage Flow

```
1. User opens Dashboard
   ↓
2. React fetches /api/zc/current
   ↓
3. Backend returns latest Zc from monitor.history
   ↓
4. Dashboard displays Zc gauge, zone, mode
   ↓
5. User triggers manual calculation (or periodic auto-calc)
   ↓
6. Metrics collected from Slack/Discord/Manual
   ↓
7. CuratorMonitor.calculate_zc(metrics)
   ↓
8. ZcResult stored in history
   ↓
9. If zone changed → Send alert via Slack/Discord
   ↓
10. Dashboard polls API every 60s for updates
```

---

## Configuration

### Environment Variables

```bash
# Team Configuration
TEAM_SIZE=10
PROCESSING_HOURS_PER_PERSON=3.0

# API Keys
ANTHROPIC_API_KEY=sk-ant-...
SLACK_BOT_TOKEN=xoxb-...
DISCORD_BOT_TOKEN=...

# API Configuration
API_HOST=0.0.0.0
API_PORT=8000

# Monitoring
MONITORING_INTERVAL_MINUTES=60
```

### Config File (`tools/curator-ai/config.yaml`)

YAML configuration for:
- Team settings
- Data sources (enable/disable)
- Notification channels
- Thresholds (customizable)

---

## Extensibility

### Adding New Data Sources

1. **Create collector function:**

```python
def collect_notion_metrics():
    # Call Notion API
    return {"notion_updates": count}
```

2. **Register with MetricsCollector:**

```python
collector = MetricsCollector()
collector.register_collector("notion", collect_notion_metrics)
```

3. **Metrics automatically included in Zc calculation**

### Adding New Integrations

1. Create new file in `tools/integrations/[platform]/`
2. Implement bot class (similar to Slack/Discord)
3. Use CuratorMonitor for Zc calculation
4. Use CuratorRecommender for advice

---

## Performance Considerations

### Scalability

**Current limits:**
- Single-instance deployment
- In-memory history storage
- No database persistence (yet)

**Recommended for:**
- Teams of 5-50 people
- <1000 Zc calculations per day

**Future improvements (v3.1+):**
- PostgreSQL for history storage
- Redis for caching
- WebSocket for real-time updates
- Multi-instance deployment with load balancer

### API Response Times

Target response times:
- `/api/zc/current` - <50ms
- `/api/zc/calculate` - <200ms
- `/api/recommendations` (with Claude API) - <2000ms
- `/api/recommendations` (fallback) - <100ms

---

## Security

### Current Status (v3.0)

- ⚠️ No authentication
- ⚠️ CORS enabled for all origins
- ⚠️ No rate limiting

**OK for:** Internal development, trusted networks

**NOT OK for:** Public internet deployment

### Production Recommendations

1. **Add authentication:**
   - API keys
   - OAuth 2.0
   - JWT tokens

2. **Restrict CORS:**
   ```python
   allow_origins=["https://yourdomain.com"]
   ```

3. **Add rate limiting:**
   - 100 requests/hour per IP
   - 10 requests/minute per endpoint

4. **Encrypt sensitive data:**
   - API keys in environment variables
   - TLS/HTTPS for all endpoints

5. **Input validation:**
   - Pydantic models (already implemented)
   - Sanitize user inputs

---

## Testing Strategy

### Unit Tests (`tests/unit/`)

- `test_monitor.py` - Zc calculation logic
- `test_recommender.py` - Recommendation generation
- Coverage target: 80%+

### Integration Tests (`tests/integration/`)

- `test_api.py` - API endpoint testing
- `test_slack_integration.py` - Slack bot testing
- `test_discord_integration.py` - Discord bot testing

### E2E Tests (`tests/e2e/`)

- Full workflow testing (Milestone 4)

---

## Deployment Options

### Local Development

```bash
# Backend
python tools/dashboard/backend/api.py

# Frontend
cd tools/dashboard/frontend
npm start
```

### Docker Compose

```yaml
version: '3.8'
services:
  backend:
    build: ./tools/dashboard/backend
    ports:
      - "8000:8000"
    environment:
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
  
  frontend:
    build: ./tools/dashboard/frontend
    ports:
      - "3000:3000"
    depends_on:
      - backend
```

### Cloud Deployment

**Backend:** Heroku, Railway, Render  
**Frontend:** Vercel, Netlify, Cloudflare Pages

---

## Monitoring & Observability

### Logging

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Zc calculated: 0.85 (YELLOW)")
logger.error("API call failed: timeout")
```

### Metrics (Future)

- Zc calculation count
- API response times
- Error rates
- Zone distribution over time

---

**This architecture supports the current v3.0 implementation and is designed for future extensibility.**

Last updated: February 14, 2026
