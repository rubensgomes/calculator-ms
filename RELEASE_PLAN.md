# Release Plan — calculator-ms v0.1.0

**Repository:** rubensgomes/calculator-ms
**Date:** 2026-02-14
**Release Version:** 0.1.0
**Release Type:** Initial release
**Branch Strategy:** main → release → tag v0.1.0

## Pre-flight Checks

- [x] Repository `rubensgomes/calculator-ms` exists and is accessible
- [x] Remote `release` branch exists
- [x] All required environment variables are set (GIT_AUTHOR_NAME, GIT_AUTHOR_EMAIL, GIT_COMMITTER_EMAIL, GITHUB_USER, GITHUB_TOKEN, GH_TOKEN)
- [x] All 86 tests pass (86 passed, 0 failed)
- [x] Current version in `pyproject.toml` is `0.1.0`
- [x] `CHANGELOG.md` has entry for `[0.1.0] - 2026-02-14`

## Release Steps

- [ ] **Step 1: Commit all pending changes to main**
  - Stage all modified and new files on `main`
  - Commit with message: `release: prepare v0.1.0`
  - Push `main` to `origin`

- [ ] **Step 2: Merge main into release branch**
  - Fetch latest from origin
  - Checkout `release` branch
  - Merge `main` into `release` (fast-forward preferred)
  - Push `release` to `origin`

- [ ] **Step 3: Create Git tag**
  - Create annotated tag `v0.1.0` on the `release` branch with message `v0.1.0`
  - Push tag to `origin`

- [ ] **Step 4: Create GitHub Release**
  - Create a GitHub release from tag `v0.1.0`
  - Title: `v0.1.0`
  - Release notes from CHANGELOG.md (0.1.0 section):
    - Core `Calculator` class with arithmetic operations: add, subtract, multiply, divide
    - Power and root operations: power, sqrt, nth_root
    - Modulo and integer math: modulo, floor_divide
    - Absolute value, rounding, floor, and ceil operations
    - Logarithmic and exponential functions: log10, ln, exp
    - FastAPI REST API with POST endpoints for all calculator operations
    - Pydantic request/response models for API validation
    - Unit tests for all calculator operations
    - Integration tests for all API endpoints
    - Poetry-based project configuration with src-layout

- [ ] **Step 5: Switch back to main**
  - Checkout `main` branch

## Post-Release Verification

- [ ] **Step 6: Verify the release**
  - Confirm GitHub release `v0.1.0` is visible
  - Confirm tag `v0.1.0` exists on remote
