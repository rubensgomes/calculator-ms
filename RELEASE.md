# Release process

**Currently, only Rubens Gomes is authorized to push a release**

## Prerequisites

1. Ensure the following packages and tools are installed:

    - coreutils package
    - dnsutils package
    - curl 8.5.0 or later
    - gawk 5.2.1 or later
    - gh version 2.81.0 or later (GitHub CLI tool)
    - git version 2.43.0 or later
    - grep version 3.11 or later

2. Ensure a `release` branch is created in the remote repository.

3. Ensure the `claude/commands` files
   from <https://github.com/rubensgomes/ai-code-steps?tab=readme-ov-file> are
   installed in the local `~/.claude/commands` folder.

4. Ensure the `scripts/test_github_connectivity.sh` is executed prior to running
   a release to ensure connectivity to GitHub remote repository.

5. Ensure `poetry run python scripts/generate_openapi.py` is executed during
   release to ensure the latest version of `openapi.yaml` file is saved for that
   release.

## Environment Variables

The release process is done on a Linux machine using a "Claude Code" custom
slash command `.claude/commands/release-plan.md`. Therefore, it is expected
that a `Claude Code` CLI session is started running on an underlying Linux
`bash` shell with the following environment variables set:

- GIT_AUTHOR_NAME
- GIT_AUTHOR_EMAIL
- GIT_COMMITTER_EMAIL
- GITHUB_USER
- GITHUB_TOKEN
- GH_TOKEN (should be same as GITHUB_TOKEN)

## Commands to run during release

- The following commands must run and succeed during a release:

    ```bash
    # Format code
    poetry run black src/ tests/
    
    # Lint
    poetry run pylint src/
    
    # Type checking
    poetry run mypy src/
    
    # Sort imports
    poetry run isort src/ tests/
    
    # Run tests
    poetry run pytest

    # Run tests with coverage report
    poetry run python -m coverage run -m pytest tests/
    ```

## Generating a release plan

The release plan is generated/executed within `Claude Code`. You must
start `Claude Code`, and run the following custom slash command:

- Test connectivity to this project remote Git repo:

   ```bash
   test_github_connectivity.sh rubensgomes/calculator-ms
   ```

- Claude code custom slash command:

    ```text
    /release-plan javamcp
    ```

- Then once the plan is reviewed and approved, you prompt `Claude Code` to
  proceed with the plan.
