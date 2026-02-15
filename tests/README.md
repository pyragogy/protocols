# Tests

Test suite for CIM Pattern components.

## Running Tests

```bash
# All tests
pytest -v

# Unit tests only
pytest tests/unit/ -v

# Integration tests
pytest tests/integration/ -v

# E2E tests
pytest tests/e2e/ -v

# With coverage
pytest --cov=tools --cov-report=html
```

## Test Structure

- `unit/` - Unit tests for individual components
- `integration/` - Integration tests for APIs and bots
- `e2e/` - End-to-end workflow tests

## Current Coverage

- ✅ Unit tests: Curator AI monitor
- 🔄 Integration tests: Coming in Milestone 3
- 🔄 E2E tests: Coming in Milestone 4

## Writing Tests

Follow pytest conventions:
- Test files: `test_*.py`
- Test functions: `def test_*()`
- Use fixtures for common setup
- Keep tests isolated

See `unit/test_monitor.py` for examples.
