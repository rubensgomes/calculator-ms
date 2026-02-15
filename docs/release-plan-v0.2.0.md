# Release Plan — calculator-ms v0.2.0

**Date:** 2026-02-14
**Previous Release:** v0.1.0
**Repository:** rubensgomes/calculator-ms

## Summary

This release adds developer experience improvements to the calculator
microservice: an OpenAPI 3.1 YAML spec endpoint, a root redirect to the
Swagger UI docs page, and improved API docstrings.

## Changes Included

### New Features
- `GET /openapi.yaml` — returns the full OpenAPI 3.1 specification in YAML
  format with proper `application/vnd.oai.openapi;version=3.1` content type
- `GET /` — redirects (HTTP 307) to `/docs` so Swagger UI is the default
  landing page
- FastAPI app metadata (`title`, `description`) with a download link to the
  YAML spec displayed on the Swagger UI page

### Improvements
- Updated all `@app.post` docstrings to use explicit
  "Returns an HTTP 400 Bad Request error" wording

### Tests
- Added `test_root_redirects_to_docs` integration test
- Added `test_openapi_yaml` integration test

## Files Changed

- `src/calculator/api.py` — new endpoints, updated docstrings, app metadata
- `tests/test_api.py` — two new test functions
- `pyproject.toml` — dependency and dev-dependency updates
- `poetry.lock` — lockfile update
- `CLAUDE.md` — documentation update
- `README.md` — documentation update

## Release Checklist

- [x] Bump version in `pyproject.toml` from `0.1.0` to `0.2.0`
- [x] Run `poetry lock` to sync the lockfile
- [x] Run `black src/ tests/` to verify formatting
- [x] Run `pylint src/ tests/` and confirm 10.00/10
- [x] Run `pytest` and confirm all tests pass
- [ ] Commit all changes with release message
- [ ] Tag the commit as `v0.2.0`
- [ ] Push commit and tag to remote
- [ ] Create GitHub release for `v0.2.0`
