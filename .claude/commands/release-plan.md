---
description: Generate a release plan for the project.
argument-hint: Git repository name (e.g., rubensgomes/calculator-ms)
---

# Generate Release Plan

1. If no argument is provided, respond with "Error: Git repository name is
   required."
2. If the argument is provided, check if the $ARGUMENT repository exists.
3. MUST run `scripts/test_github_connectivity.sh $ARGUMENT`, and ensure it
   succeeds
4. If the `scripts/test_github_connectivity.sh $ARGUMENT` succeeds generate the
   release plan and continues.
5. If the `scripts/test_github_connectivity.sh $ARGUMENT` fails print error
   message and stop.
6. Upon completion of release plan, request user's approval.
7. Upon approval of the release plan:

- MUST run `poetry run mypy src/` and fix any issues
- MUST run `poetry run isort src/ tests/` and fix any issues
- MUST run `poetry run black src/ tests/` and fix any issues
- MUST run `poetry run pytest` and fix any issues
- MUST ensure a CHANGELOG.md file exists in the project
- MUST update the CHANGELOG.md with the current release changes
- MUST save the release plan in the project's docs folder
- MUST mark off checkboxes as steps in the plan are completed
- MUST get user's approval for each release step being executed

