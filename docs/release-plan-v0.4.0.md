# Release Plan — calculator-ms v0.4.0

**Date:** 2026-02-16
**Previous Release:** v0.3.0
**Repository:** rubensgomes/calculator-ms

## Summary

This is a minor housekeeping release that fixes documentation references and
improves project metadata.

## Changes Included

### Improvements
- Updated `pyproject.toml` project description from empty string to
  "A calculator microservice."
- Fixed `RELEASE.md` script path from `test_github_connectivity.sh` to
  `scripts/test_github_connectivity.sh`
- Fixed `RELEASE.md` slash command example from `/release-plan javamcp` to
  `/release-plan rubensgomes/calculator-ms`
- Removed trailing instructions paragraph from `RELEASE.md`

### Docs
- `807ca33` — marked release plan v0.3.0 as completed

## Files Changed

- `pyproject.toml` — updated project description, bumped version to 0.4.0
- `RELEASE.md` — fixed script path and slash command references
- `CHANGELOG.md` — added v0.4.0 entries
- `openapi.yaml` — regenerated with v0.4.0
- `docs/release-plan-v0.4.0.md` — this release plan

## Release Checklist

- [x] Bump version in `pyproject.toml` from `0.3.0` to `0.4.0`
- [x] Run `poetry lock` to sync the lockfile
- [x] Run `poetry run python scripts/generate_openapi.py` to regenerate OpenAPI spec
- [x] Run `poetry run mypy src/` and fix any issues
- [x] Run `poetry run isort src/ tests/` and fix any issues
- [x] Run `poetry run black src/ tests/` and fix any issues
- [x] Run `poetry run pytest` and fix any issues
- [x] Update `CHANGELOG.md` with v0.4.0 changes
- [x] Save this release plan in `docs/release-plan-v0.4.0.md`
- [x] Commit all changes with release message
- [x] Tag the commit as `v0.4.0`
- [x] Push commit and tag to remote
- [x] Create GitHub release for `v0.4.0`
