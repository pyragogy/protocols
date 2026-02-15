# Curator AI - Core Engine

The heart of the CIM Pattern monitoring system.

## Components

### `monitor.py` - Monitoring Engine

Calculates Zc (Cognitive Impedance) and detects zones/modes.

**Usage:**

```python
from monitor import CuratorMonitor, MetricsCollector, TeamMetrics

# Initialize
monitor = CuratorMonitor(team_size=10, processing_hours_per_person=3.0)

# Collect metrics
collector = MetricsCollector()
metrics = collector.collect_manual(
    slack_messages=150,
    ai_outputs=30,
    timeframe_hours=24
)

# Calculate Zc
result = monitor.calculate_zc(metrics)

print(f"Zc: {result.zc} ({result.zone})")
print(f"Mode: {result.mode}")
print(f"Recommendation: {result.recommendation}")
```

### `recommender.py` - AI Recommendations

Generates personalized advice using Claude API.

**Usage:**

```python
from recommender import CuratorRecommender

# Requires ANTHROPIC_API_KEY environment variable
recommender = CuratorRecommender()

# Generate recommendation
recommendation = recommender.generate_recommendation(
    result=result,  # From monitor
    team_context="10-person startup, heavy AI usage"
)

print(recommender.format_recommendation(recommendation))
```

### `config.yaml` - Configuration

Copy to `config.local.yaml` and customize for your team.

## Dependencies

```bash
pip install anthropic
```

## Environment Variables

```bash
export ANTHROPIC_API_KEY="sk-ant-..."  # Required for AI recommendations
export TEAM_SIZE=10                     # Optional (default: 10)
```

## Quick Test

```bash
python monitor.py      # Run example calculation
python recommender.py  # Test AI recommendations
```

## Integration

Curator AI is used by:
- Dashboard Backend (`../dashboard/backend/api.py`)
- Slack Bot (`../integrations/slack/bot.py`)
- Discord Bot (`../integrations/discord/bot.py`)

## See Also

- [API Reference](../../docs/developer/API-REFERENCE.md)
- [Architecture](../../docs/developer/ARCHITECTURE.md)
