# Release Plan — calculator-ms v0.5.0

**Date:** 2026-02-18
**Previous Release:** v0.4.0
**Repository:** rubensgomes/calculator-ms

## Summary

This release extracts the core `Calculator` class into the external
`calculator-lib-rubens` package, removing the local `calculator.py` module.
It also improves documentation (README, CLAUDE.md, RELEASE.md) and renames
the GitHub connectivity script for brevity.

## Changes Included

### Breaking

- Removed `src/calculator/calculator.py`; the `Calculator` class is now
  provided by the `calculator-lib-rubens` (`calculator_lib`) dependency.

### Added

- `calculator-lib-rubens (>=0.1.2,<0.2.0)` as a project dependency in
  `pyproject.toml`.
- "Common Poetry Commands" section in `README.md` with everyday dev commands.

### Changed

- Updated imports in `__init__.py`, `api.py`, and `test_calculator.py` to use
  `calculator_lib.Calculator` instead of the local module.
- Updated `CLAUDE.md`: added `calculator-lib-rubens` to tech stack, removed
  `calculator.py` from project structure, fixed `black` command prefix.
- Updated `RELEASE.md`: fixed script path references to `scripts/test_github.sh`,
  added `poetry build` command to release commands section.
- Renamed `scripts/test_github_connectivity.sh` to `scripts/test_github.sh`.

### Removed

- `src/calculator/calculator.py` — replaced by external library.
- `logs/calculator.log` — stale log file (current log is `calculator-ms.log`).

## Release Checklist

- [x] Bump version in `pyproject.toml` from `0.4.0` to `0.5.0`
- [x] Run `poetry lock` to sync the lockfile
- [x] Run `poetry run python scripts/generate_openapi.py` to regenerate OpenAPI spec
- [x] Run `poetry run mypy src/` and fix any issues
- [x] Run `poetry run isort src/ tests/` and fix any issues
- [x] Run `poetry run black src/ tests/` and fix any issues
- [x] Run `poetry run pytest` and fix any issues
- [x] Run `export SOURCE_DATE_EPOCH=$(date +%s); poetry build -v` and fix any issues
- [x] Update `CHANGELOG.md` with v0.5.0 changes
- [x] Save this release plan in `docs/release-plan-v0.5.0.md`
- [x] Commit all changes with release message
- [x] Tag the commit as `v0.5.0`
- [x] Push commit and tag to remote
- [x] Create GitHub release for `v0.5.0`
