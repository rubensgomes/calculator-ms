# Calculator-MS

Python calculator microservice built with FastAPI. Provides arithmetic
operations via a REST API.

- **Distribution name**: `calculator-ms`
- **Python package**: `calculator` (imported as `from calculator import ...`)
- **Repository**: `rubensgomes/calculator-ms`

## Requirements

- Python 3.14+
- [Poetry](https://python-poetry.org/)

## Getting Started

```bash
# Install dependencies
poetry install

# Start the development server
poetry run python -m uvicorn calculator.api:app --reload

# Run tests
poetry run pytest

# Format code
poetry run black src/ tests/
```

The API will be available at `http://127.0.0.1:8000`. Interactive docs are
served at `/docs`.

## API Endpoints

All endpoints accept POST requests with JSON bodies and return
`{"result": <float>}`.

### Core Arithmetic

| Endpoint    | Body             | Description |
|-------------|------------------|-------------|
| `/add`      | `{"a":, "b": }`  | a + b       |
| `/subtract` | `{"a": , "b": }` | a - b       |
| `/multiply` | `{"a": , "b": }` | a * b       |
| `/divide`   | `{"a": , "b": }` | a / b       |

### Power & Roots

| Endpoint    | Body             | Description             |
|-------------|------------------|-------------------------|
| `/power`    | `{"a": , "b": }` | a raised to the power b |
| `/sqrt`     | `{"a": }`        | Square root of a        |
| `/nth_root` | `{"a": , "b": }` | b-th root of a          |

### Modulo & Integer Math

| Endpoint        | Body             | Description |
|-----------------|------------------|-------------|
| `/modulo`       | `{"a": , "b": }` | a mod b     |
| `/floor_divide` | `{"a": , "b": }` | a // b      |

### Absolute & Rounding

| Endpoint    | Body                    | Description                 |
|-------------|-------------------------|-----------------------------|
| `/absolute` | `{"a": }`               | Absolute value of a         |
| `/round`    | `{"a": , "decimals": }` | Round a to n decimal places |
| `/floor`    | `{"a": }`               | Floor of a                  |
| `/ceil`     | `{"a": }`               | Ceiling of a                |

### Logarithmic & Exponential

| Endpoint | Body      | Description             |
|----------|-----------|-------------------------|
| `/log10` | `{"a": }` | Base-10 logarithm       |
| `/ln`    | `{"a": }` | Natural logarithm       |
| `/exp`   | `{"a": }` | e raised to the power a |

Invalid inputs (e.g., division by zero, log of a negative number) return HTTP
400 with an error detail message.

## Example

```bash
curl -X POST http://127.0.0.1:8000/add \
  -H "Content-Type: application/json" \
  -d '{"a": 10, "b": 3}'
# {"result": 13.0}
```

## Configuration

All settings are in `config.yaml` at the project root, organized into two sections.

### Server

```yaml
server:
  host: "0.0.0.0"        # Bind address
  port: 8000              # Listening port
```

Access the server config programmatically with `get_server_config()`.

### Logging

```yaml
logging:
  root:
    level: INFO           # DEBUG, INFO, WARNING, ERROR, CRITICAL

  handlers:
    file:
      filename: logs/calculator-ms.log
      maxBytes: 10485760  # 10 MB
      backupCount: 5
```

By default, logs are sent to both stdout (console handler) and
`logs/calculator-ms.log` (rotating file handler, 10 MB max, 5 backups).

## Project Structure

```
config.yaml               # Application configuration (server + logging)
src/calculator/
  api.py                  # FastAPI endpoints
  calculator.py           # Core Calculator class
  config.py               # Configuration loader (server settings, logging setup)
  __init__.py
tests/
  test_calculator.py      # Unit tests
  test_api.py             # Integration tests
logs/                     # Log output (created automatically)
```

## Tech Stack

- **FastAPI** + **Uvicorn** — web framework and ASGI server
- **Pydantic** — request/response validation
- **PyYAML** — application configuration
- **Poetry** — dependency management
- **pytest** + **httpx** — testing
- **Black** — code formatting
