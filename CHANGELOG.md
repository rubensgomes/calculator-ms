# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.3.0] - 2026-02-15

### Added

- Dynamic `version` field in FastAPI app metadata via `importlib.metadata`.
- `openapi.yaml` static OpenAPI 3.1 specification file committed to the repo.
- `scripts/generate_openapi.py` script to regenerate the static OpenAPI spec.
- `scripts/test_github_connectivity.sh` GitHub connectivity validation script.
- `.claude/commands/release-plan.md` Claude Code slash command for release planning.
- Dev dependencies: `isort`, `mypy`, `types-pyyaml`.

### Changed

- Updated FastAPI app `description` to list all supported operations.
- Changed `openapi_url` to `/docs` for cleaner Swagger UI integration.
- Condensed `floor_divide` endpoint docstring to single line.
- Reorganized README "Getting Started" section; added `poetry env activate` and `generate_openapi.py` steps.
- Fixed YAML indentation in README configuration examples.
- Improved RELEASE.md with release commands section and prerequisite updates.
- Renamed `RELEASE_PLAN.md` to `docs/release-plan-v0.1.0.md` for consistent doc organization.

## [0.2.0] - 2026-02-14

### Added

- `GET /openapi.yaml` endpoint returning the full OpenAPI 3.1 specification in YAML format.
- `GET /` root redirect (HTTP 307) to `/docs` Swagger UI landing page.
- FastAPI app metadata (`title`, `description`) with a download link to the YAML spec.
- `test_root_redirects_to_docs` integration test.
- `test_openapi_yaml` integration test.

### Changed

- Updated all `@app.post` docstrings to use explicit "Returns an HTTP 400 Bad Request error" wording.

## [0.1.0] - 2026-02-14

### Added

- Core `Calculator` class with arithmetic operations: add, subtract, multiply, divide.
- Power and root operations: power, sqrt, nth_root.
- Modulo and integer math: modulo, floor_divide.
- Absolute value, rounding, floor, and ceil operations.
- Logarithmic and exponential functions: log10, ln, exp.
- FastAPI REST API with POST endpoints for all calculator operations.
- Pydantic request/response models for API validation.
- Unit tests for all calculator operations.
- Integration tests for all API endpoints.
- Poetry-based project configuration with src-layout.
