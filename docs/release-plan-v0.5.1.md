# Release Plan — calculator-ms v0.5.1

**Date:** 2026-02-20
**Previous Release:** v0.5.0
**Repository:** rubensgomes/calculator-ms

## Summary

Patch release with project housekeeping: expanded `.gitignore`, LICENSE
corrections and MIT license addition, streamlined `RELEASE.md`, and new
`SETUP.md` developer onboarding guide.

## Changes Included

### Added

- `SETUP.md` — comprehensive developer setup guide covering prerequisites,
  tool installation (pyenv, Python, pipx, Poetry, Claude Code), virtual
  environment management, common commands, PyCharm IDE configuration, and
  PyPI publishing steps.

### Changed

- Expanded `.gitignore` with organized sections for Claude Code, Python,
  Jupyter, testing/coverage, logs, OS files, AI/ML artifacts, and secrets.
- Updated `LICENSE`: fixed punctuation, capitalized "Limitation of Liability"
  heading, and appended the standard MIT License text.
- Streamlined `RELEASE.md`: removed inline command listings (now references
  `.claude/commands/release-plan.md`), removed duplicate prerequisites,
  capitalized title.
- Updated `poetry.lock` (dependency hash refresh, no version changes).

## Release Checklist

- [x] Bump version in `pyproject.toml` from `0.5.0` to `0.5.1`
- [x] Run `poetry lock` to sync the lockfile
- [x] Run `poetry run mypy src/` and fix any issues
- [x] Run `poetry run isort src/ tests/` and fix any issues
- [x] Run `poetry run black src/ tests/` and fix any issues
- [x] Run `poetry run pytest` and fix any issues
- [x] Run `export SOURCE_DATE_EPOCH=$(date +%s); poetry build -v` and fix any issues
- [x] Update `CHANGELOG.md` with v0.5.1 changes
- [x] Save this release plan in `docs/release-plan-v0.5.1.md`
- [x] Commit all changes with release message
- [x] Tag the commit as `v0.5.1`
- [x] Push commit and tag to remote
- [x] Create GitHub release for `v0.5.1`
