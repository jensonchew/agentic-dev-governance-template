# Development Orchestrator — Handoff Formats

## Context handoff

Provide:
- track name
- objective
- problem being addressed
- likely affected area
- known boundaries or exclusions
- specific questions to answer

## Design analyst handoff

Provide:
- track name
- objective
- problem being addressed
- affected area
- context map, if available
- known boundaries or exclusions
- **mode**: explore or ground
- for explore mode: specific trade-offs or concerns to explore
- for ground mode: specific decisions or trade-offs to evaluate
- prior explore-mode output, if invoking ground mode after exploration

## Migration planner handoff

Provide:
- track name
- objective
- affected area
- context map
- design analyst output, if available
- identified schema, contract, or deployment changes
- known ordering constraints or rollback requirements

## Security reviewer handoff

Provide:
- worktree path
- branch name
- task spec path, if any
- track objective
- security-relevant scope areas
- any security requirements from the spec
- any security concerns flagged by the general reviewer

## UI design handoff

Provide:
- track name
- objective
- user or business need being addressed
- affected screens, flows, or frontend area
- context map, if available
- design-system constraints
- known boundaries or exclusions
- specific UX, consistency, or reuse concerns to shape

## UI review handoff

Provide:
- track name
- objective
- UI proposal or implementation being reviewed
- relevant design-system constraints
- known trade-offs already accepted
- specific concerns to critique

## Architecture challenge handoff

Provide:
- track name
- objective
- problem being addressed
- affected area
- context map, if available
- design analyst output, if available
- assumptions to challenge
- possible broader impacts to stress-test

## Spec handoff

Provide:
- **worktree path** (required — Spec Writer writes the spec file here)
- approved track objective
- context map
- design analyst output, if any
- migration plan, if any
- UI design output, if any
- UI review output, if any
- architecture challenge output, if any
- agreed scope boundaries
- explicit out-of-scope items
- approval decisions already made

## Implementer handoff

Provide:
- worktree path
- branch name
- task spec path (required — must be `docs/tasks/<task-id>.md`, present in the worktree)
- track objective (one sentence)
- constraints and exclusions

Do not include the full spec content in the handoff message. The implementer
reads the spec from the file. The handoff message is navigation, not content.

The implementer must work only in the assigned worktree.

## Reviewer handoff

Provide:
- worktree path
- branch name
- task spec path (`docs/tasks/<task-id>.md` — written into the worktree by the Spec Writer)
- track objective
- review focus areas
- any accepted trade-offs
- any baseline limitations or pre-existing issues already identified
- UI review output, if relevant

The reviewer reads the spec from the file in the worktree. The spec is not
committed — it is a planning artifact on disk. The reviewer should review
only the track delta against the baseline branch.

## Dev-to-Delivery handoff

When the work is ready for delivery evaluation, provide a structured handoff
to the Delivery using the template at `docs/templates/HANDOFF.md`.

The handoff must include:
- system summary and architecture overview
- what was built or changed
- intended deployment assumptions
- known shortcuts, deferred items, or technical debt
- constraints the delivery must respect
- open risks and unresolved questions for delivery review
- explicit statement of what the Development is not claiming (e.g., production readiness, cost posture, security hardening)

Do not silently assume production readiness.
Do not hand off without identifying what the delivery needs to evaluate.
