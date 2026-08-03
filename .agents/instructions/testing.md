# Testing Rules

## Universal expectations

Rules:
- every new public method, endpoint, or exported function must have at least one test
- changed behavior must be covered by tests
- bug fixes should include regression coverage where practical
- keep tests behavior-focused, not implementation-coupled

## Stack-specific testing

Use the testing frameworks and tools defined in `REPOSITORY-CONTEXT.md`.

Do not:
- add excessive mocking where simpler behavior tests are possible
- claim test coverage that was not executed
- treat pre-existing failing tests as newly introduced defects
