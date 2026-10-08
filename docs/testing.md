# Test suites

DojoAgents uses the same execution-boundary markers as DojoSDK:

- `unit`: deterministic service and model tests.
- `offline_integration`: Dashboard and DojoSDK local snapshot integration.
- `online_integration`: live external service tests.
- `contract`: API, configuration, and cross-repository contracts.
- `slow`: long-running dataset or end-to-end tests.

Typical local commands:

```bash
uv run --extra dev python -m pytest -m "not online_integration and not slow" -q
uv run --extra dev python -m pytest -m offline_integration -q
uv run --extra dev python -m pytest -m contract -q
```

Live and slow suites must be selected explicitly in CI with their required
credentials and services. They must not be inferred from a developer's local
offline configuration.

