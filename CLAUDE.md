# CLAUDE.md

## Project Overview

**calculator-ms** — Python calculator microservice built with FastAPI. Provides arithmetic operations via a REST API. Distribution name is `calculator-ms`; the Python package remains `calculator` (hyphens not allowed in Python package names).

## Tech Stack

- **Python 3.14+**, **FastAPI**, **Uvicorn**, **Pydantic**
- **Poetry** for dependency management
- **calculator-lib-rubens** (`calculator_lib`) for the core Calculator class
- **pytest** for testing, **httpx** for API tests, **black** for formatting
- **PyYAML** for application configuration

## Project Structure

```
config.yaml           # Application configuration (server and logging settings)
src/calculator/       # Source code (src-layout)
  api.py              # FastAPI endpoints (POST-based, Pydantic request/response models)
  config.py           # Reads config.yaml; provides load_config(), setup_logging(), get_server_config()
  __init__.py         # Public API: Calculator, app, get_server_config
tests/
  test_calculator.py  # Unit tests (one test class per operation)
  test_api.py         # Integration tests (FastAPI TestClient)
logs/                 # Log output directory (created automatically)
```

## Common Commands

```bash
# Install dependencies
poetry install

# Run tests
pytest

# Run tests verbose
pytest -v

# Format code
poetry run black src/ tests/

# Start dev server
poetry run python -m uvicorn calculator.api:app --reload
```

## Configuration

- All settings live in `config.yaml` with two top-level sections: `server` and `logging`
- `load_config()` + `setup_logging()` in `config.py` are called once at app startup in `api.py`
- `get_server_config()` returns the `server` section (host, port)

### Server

- `server.host`: bind address (default: `0.0.0.0`)
- `server.port`: listening port (default: `8000`)

### Logging

- `logging` section is passed directly to Python `dictConfig`
- Console handler (stdout) + rotating file handler (`logs/calculator-ms.log`, 10 MB, 5 backups)
- Log levels used: DEBUG for inputs/results, INFO for operation completions, WARNING for validation errors

## Conventions

- All `Calculator` methods are stateless and use `float` type hints
- Validation errors raise `ValueError` with descriptive messages
- API returns 400 with error detail for invalid inputs
- Tests use `pytest.approx()` for float comparisons
- Test classes are named `Test<Operation>` (e.g., `TestAdd`, `TestDivide`)
