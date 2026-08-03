# Build and Validation Rules

Rules:
- use the build and test commands defined in `REPOSITORY-CONTEXT.md`
- validate in the intended working directory, not by assumption
- distinguish backend, frontend, and full-repo validation when reporting results

Implementers must:
- verify the baseline build before changes for non-trivial work when practical
- run the relevant tests for the changed area
- report what was run and what was not run

Reviewers must:
- distinguish verified results from unverified assumptions
- note when correctness depends on code paths not exercised
