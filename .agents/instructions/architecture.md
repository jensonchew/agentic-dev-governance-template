# Architecture Rules

## Layer separation

Regardless of stack, enforce the architecture boundaries defined in
`REPOSITORY-CONTEXT.md`.

Rules:
- controllers, handlers, or API endpoints should contain orchestration only, not business logic
- domain or business logic must not depend on infrastructure concerns
- infrastructure may implement interfaces or contracts defined in domain layers
- do not introduce circular dependencies
- do not move logic across layers unless explicitly required by the task
- preserve established project or module segregation unless the user explicitly approves an architecture change

## Cross-stack changes

If the task spans multiple layers or stacks (e.g., backend and frontend):
- keep contracts aligned
- update affected consumers when producer contracts change
- do not silently change API or interface behavior without updating relevant consumers and tests
- call out versioning, migration, or rollout risks when the impact crosses boundaries
