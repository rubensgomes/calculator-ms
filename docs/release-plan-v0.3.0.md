# Release Plan — calculator-ms v0.3.0

**Date:** 2026-02-15
**Previous Release:** v0.2.0
**Repository:** rubensgomes/calculator-ms

## Summary

This release improves the developer tooling, documentation, and project
infrastructure for the calculator microservice. It adds dev dependencies for
static analysis (mypy, isort), introduces release automation scripts, delivers
a static OpenAPI spec file, and enhances the FastAPI app metadata with dynamic
versioning.

## Changes Included

### New Features
- Dynamic `version` field in FastAPI app metadata read from package metadata
  via `importlib.metadata.version("calculator-ms")`
- `openapi.yaml` — static OpenAPI 3.1 specification file committed to the repo
- `scripts/generate_openapi.py` — script to regenerate the static OpenAPI spec
- `scripts/test_github_connectivity.sh` — GitHub connectivity validation script
- `.claude/commands/release-plan.md` — Claude Code slash command for release
  planning

### Improvements
- Updated FastAPI app `description` to be more descriptive of all supported
  operations
- Changed `openapi_url` to `/docs` for cleaner Swagger UI integration
- Condensed `floor_divide` endpoint docstring to single line
- Reorganized README "Getting Started" section; added `poetry env activate` and
  `generate_openapi.py` steps
- Fixed YAML indentation in README configuration examples
- Improved RELEASE.md with release commands section, prerequisite updates, and
  editorial fixes
- Renamed `RELEASE_PLAN.md` to `docs/release-plan-v0.1.0.md` for consistent
  doc organization

### Dev Dependencies
- Added `isort >=7.0.0` — import sorting
- Added `mypy >=1.19.1` — static type checking
- Added `types-pyyaml >=6.0.12` — type stubs for PyYAML

## Files Changed

- `src/calculator/api.py` — dynamic version, updated description, openapi_url
- `pyproject.toml` — new dev dependencies (isort, mypy, types-pyyaml)
- `poetry.lock` — lockfile update
- `README.md` — reorganized Getting Started, fixed config YAML indentation
- `CHANGELOG.md` — added v0.2.0 entries (missed in prior release)
- `RELEASE.md` — added commands section, improved prerequisites
- `openapi.yaml` — new static OpenAPI spec
- `scripts/generate_openapi.py` — new script
- `scripts/test_github_connectivity.sh` — new script
- `.claude/commands/release-plan.md` — new Claude Code command
- `docs/release-plan-v0.1.0.md` — renamed from RELEASE_PLAN.md
- `docs/release-plan-v0.2.0.md` — minor updates

## Release Checklist

- [x] Bump version in `pyproject.toml` from `0.2.0` to `0.3.0`
- [x] Run `poetry lock` to sync the lockfile
- [x] Run `poetry run python scripts/generate_openapi.py` to regenerate OpenAPI spec
- [x] Run `poetry run mypy src/` and fix any issues
- [x] Run `poetry run isort src/ tests/` and fix any issues
- [x] Run `poetry run black src/ tests/` and fix any issues
- [x] Run `poetry run pytest` and fix any issues
- [x] Update `CHANGELOG.md` with v0.3.0 changes
- [x] Save this release plan in `docs/release-plan-v0.3.0.md`
- [x] Commit all changes with release message
- [x] Tag the commit as `v0.3.0`
- [x] Push commit and tag to remote
- [x] Create GitHub release for `v0.3.0`
