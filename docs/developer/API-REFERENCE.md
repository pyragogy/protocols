# API Reference - Curator AI

**Version:** 3.0.0  
**Base URL:** `http://localhost:8000`

This document describes the Curator AI Dashboard API endpoints.

---

## Authentication

Currently no authentication required (v3.0). In production, add API keys or OAuth.

---

## Endpoints

### Health Check

**GET** `/api/health`

Check API health status.

**Response:**
```json
{
  "status": "healthy",
  "version": "3.0.0",
  "team_size": 10,
  "monitor_active": true,
  "recommender_active": true
}
```

---

### Current Zc Status

**GET** `/api/zc/current`

Get the most recent Zc calculation.

**Response:**
```json
{
  "timestamp": "2026-02-14T17:30:00",
  "zc": 0.85,
  "v_generation": 25.5,
  "b_social": 30.0,
  "zone": "YELLOW",
  "mode": "GUSH",
  "confidence": 0.8,
  "trend": "INCREASING",
  "recommendation": "Schedule GUSH session within 48h..."
}
```

**Status Codes:**
- `200` - Success
- `404` - No data available (calculate Zc first)

---

### Zc History

**GET** `/api/zc/history?hours=168`

Get historical Zc data.

**Query Parameters:**
- `hours` (optional): Hours of history to retrieve. Default: 168 (7 days)

**Response:**
```json
{
  "data": [
    {
      "timestamp": "2026-02-14T10:00:00",
      "zc": 0.65,
      "zone": "GREEN",
      ...
    },
    {
      "timestamp": "2026-02-14T11:00:00",
      "zc": 0.72,
      "zone": "YELLOW",
      ...
    }
  ],
  "count": 168
}
```

**Status Codes:**
- `200` - Success
- `500` - Monitor not initialized

---

### Calculate Zc

**POST** `/api/zc/calculate`

Calculate Zc from provided metrics.

**Request Body:**
```json
{
  "slack_messages": 150,
  "discord_messages": 0,
  "notion_updates": 20,
  "github_events": 0,
  "linear_updates": 0,
  "ai_outputs": 30,
  "emails": 25,
  "timeframe_hours": 24
}
```

**All fields optional** (default: 0). Only `timeframe_hours` defaults to 24.

**Response:**
```json
{
  "timestamp": "2026-02-14T17:30:00",
  "zc": 0.85,
  "v_generation": 25.5,
  "b_social": 30.0,
  "zone": "YELLOW",
  "mode": "GUSH",
  "confidence": 0.8,
  "trend": "STABLE",
  "recommendation": "Schedule GUSH session within 48h..."
}
```

**Status Codes:**
- `200` - Success
- `400` - Invalid input
- `500` - Calculation error

---

### AI Recommendations

**GET** `/api/recommendations?team_context=...`

Get personalized AI-powered recommendations.

**Query Parameters:**
- `team_context` (optional): Text description of team for context-aware advice

**Response:**
```json
{
  "summary": "Team approaching overload - schedule GUSH session",
  "immediate_actions": [
    "Schedule 90-min GUSH session within 48h",
    "Identify 3-5 pending decisions",
    "Share GUSH template with team"
  ],
  "this_week": [
    "Run GUSH session",
    "Clear decision backlog",
    "Re-measure Zc post-GUSH"
  ],
  "avoid": [
    "Don't defer decisions again",
    "Don't schedule more async discussions"
  ],
  "success_criteria": [
    "Zc drops below 0.7",
    "70%+ decisions closed",
    "Team confidence >7/10"
  ],
  "context": "Yellow zone requires forced convergence via GUSH protocol."
}
```

**Status Codes:**
- `200` - Success (uses Claude API if available, fallback otherwise)
- `404` - No Zc data available

---

### Summary Statistics

**GET** `/api/stats/summary`

Get summary statistics for last 7 days.

**Response:**
```json
{
  "avg_zc": 0.72,
  "current_zc": 0.85,
  "current_zone": "YELLOW",
  "trend": "INCREASING",
  "zone_distribution": {
    "GREEN": 120,
    "YELLOW": 40,
    "RED": 8
  },
  "data_points": 168
}
```

**Status Codes:**
- `200` - Success

---

## Error Responses

All error responses follow this format:

```json
{
  "detail": "Error message here"
}
```

**Common status codes:**
- `400` - Bad Request (invalid input)
- `404` - Not Found (no data available)
- `500` - Internal Server Error

---

## Rate Limiting

No rate limiting in v3.0. In production, implement rate limiting to prevent abuse.

---

## CORS

CORS is enabled for all origins in development. In production, restrict to your domain:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourdomain.com"],
    ...
)
```

---

## WebSocket Support (Future)

v3.1+ will add WebSocket endpoint for real-time Zc updates:

```
ws://localhost:8000/ws/zc
```

---

## Example Usage

### Python

```python
import requests

# Calculate Zc
response = requests.post('http://localhost:8000/api/zc/calculate', json={
    'slack_messages': 150,
    'ai_outputs': 30,
    'timeframe_hours': 24
})

result = response.json()
print(f"Zc: {result['zc']} ({result['zone']})")
```

### JavaScript

```javascript
// Fetch current Zc
fetch('/api/zc/current')
  .then(res => res.json())
  .then(data => {
    console.log(`Zc: ${data.zc} (${data.zone})`);
  });

// Calculate Zc
fetch('/api/zc/calculate', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    slack_messages: 150,
    ai_outputs: 30,
    timeframe_hours: 24
  })
})
  .then(res => res.json())
  .then(data => console.log(data));
```

### curl

```bash
# Health check
curl http://localhost:8000/api/health

# Get current Zc
curl http://localhost:8000/api/zc/current

# Calculate Zc
curl -X POST http://localhost:8000/api/zc/calculate \
  -H "Content-Type: application/json" \
  -d '{"slack_messages": 150, "ai_outputs": 30}'

# Get recommendations
curl http://localhost:8000/api/recommendations
```

---

## Deployment

### Development

```bash
python tools/dashboard/backend/api.py
```

Server runs on `http://localhost:8000`

### Production (Uvicorn)

```bash
uvicorn tools.dashboard.backend.api:app \
  --host 0.0.0.0 \
  --port 8000 \
  --workers 4
```

### Docker

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "tools.dashboard.backend.api:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## Environment Variables

```bash
# Required
ANTHROPIC_API_KEY=sk-ant-...  # For AI recommendations

# Optional
TEAM_SIZE=10                   # Team size (default: 10)
API_HOST=0.0.0.0              # API host (default: 0.0.0.0)
API_PORT=8000                 # API port (default: 8000)
```

---

## Testing

Run API tests:

```bash
pytest tests/integration/test_api.py -v
```

---

**Last updated:** February 14, 2026  
**API Version:** 3.0.0
