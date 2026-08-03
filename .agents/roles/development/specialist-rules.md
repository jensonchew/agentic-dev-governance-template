# Development Orchestrator — Specialist Rules

## Context-first rule

For non-trivial work, gather context before any downstream specialist.

Context mapping is not just a prerequisite for implementation — it is a
prerequisite for design analysis, migration planning, spec writing, and
track planning. Do not invoke the design analyst, migration planner, or
spec writer until the affected area is mapped.

Use the `context-mapper` to identify:
- affected files
- dependencies
- relevant tests
- architecture boundaries
- risks
- useful existing patterns

When the user asks to assess impact, find affected areas, identify what
is touched, or map the blast radius of a change — this is context mapping
work, not design analysis. Use the context mapper first.

Do not send any downstream specialist into non-trivial work without a
usable context handoff.

## Pre-existing issues rule

When the user points to a file, pipeline, or area that already contains
errors, warnings, or failing checks, do not assume those issues are in scope
for correction.

You must:
- distinguish the requested change from pre-existing issues
- keep the requested change bounded unless the user expands scope
- use the `context-mapper` and `reviewer` to identify whether an issue appears
  pre-existing or newly introduced
- state clearly when validation confidence is limited by unrelated baseline issues

Do not let nearby pre-existing problems silently expand the track.

## Design-analysis rule

For non-trivial changes, use the `design-analyst` before
specification or implementation.

**Prerequisite**: for non-trivial work, ensure context mapping has been
completed or is clearly unnecessary before invoking design analysis.
If the affected area is not yet known, use the context mapper first.

### Explore mode
Use explore mode for broad option generation when the path is not yet fixed.

Invoke this when:
- the user asks for options
- multiple credible solution shapes exist
- the affected area is messy and different cleanup paths are plausible
- the team wants a creative but practical pass before narrowing scope

Exploration broadens possibilities. It does not approve a pattern, define
final scope, or replace repository-grounded analysis.

### Ground mode
Use ground mode for repository-grounded investigation when the direction
is roughly known but the implementation shape needs precision.

Invoke this when:
- the request may introduce or change a pattern
- multiple plausible implementation paths exist
- consistency, reuse, or maintainability are part of the request
- the repository state needs interpretation, not just discovery

### Combined invocation
For complex work, invoke explore mode first, then ground mode with the
selected option. The design analyst will refine the chosen option rather
than restart from scratch.

Do not send the spec-writer or implementer into pattern-sensitive work until
the change shape is understood well enough to bound safely.

## Migration-planning rule

When the context map or design analyst output indicates schema changes,
breaking API contract changes, or multi-phase rollout needs, invoke the
`migration-planner` before specification.

Use this when:
- database schema changes are involved (new tables, column changes, constraints)
- API contracts are changing in breaking ways
- shared DTOs or event contracts have multiple consumers
- the change requires a specific deployment order
- data migration or backfill is needed

The migration planner produces a migration sequence and ordering constraints
that the spec writer must incorporate into the execution contract.

Do not skip migration planning for schema or contract changes.

## Security-review rule

For implementation diffs that touch security-sensitive code, invoke the
`security-reviewer` as an independent pass alongside the
general reviewer.

Use this when:
- the change affects auth, authz, or access control logic
- user input handling or validation is modified
- API surface or data exposure changes
- cryptographic operations or credential handling is involved
- the spec identifies security requirements
- the context map indicates security-sensitive files in scope

The security reviewer operates independently from the general reviewer.
Both must approve for security-sensitive tracks.

## Design-before-frontend rule

For work that materially affects screens, flows, or reusable frontend
patterns, perform UI design before frontend implementation.

Use the `ui-designer` to:
- shape screen structure and interaction flow
- align UI proposals to the approved design system
- identify reusable component opportunities
- make states, hierarchy, and key interactions explicit

Use the `ui-reviewer` to:
- critique the proposal or implementation for consistency
- check usability, reuse, maintainability, and accessibility basics
- identify one-off UI patterns that should remain shared or be avoided

Use this especially when:
- a new screen or major UI section is introduced
- a user flow or navigation path changes
- a reusable frontend component may be added or changed
- the work could affect visual consistency across features
- the team wants critique before implementation locks in the UI shape

Design work should remain bounded. Do not turn routine frontend work into speculative product redesign.

## Challenge-before-standardization rule

When a change may reinforce architectural drift, introduce a weak shared
pattern, or hide broader design impact behind a local patch, challenge the
default path before standardizing it.

Use the `architecture-challenger` to:
- question assumptions behind the obvious path
- identify drift, hidden coupling, pattern sprawl, or future cleanup cost
- surface stronger alternatives or future-state directions
- determine whether the practical answer is still to keep the change narrow

Use this especially when:
- a local fix may have cross-module or long-term impact
- the repository contains competing patterns or visible drift
- the obvious path may quietly lock in avoidable technical debt
- the team wants an explicit challenge pass before approving a stronger pattern

Challenge should be constructive and selective. Do not turn every request into an architecture initiative.

## When to invoke specialists

Use the `context-mapper` when:
- the user asks to assess impact, find affected areas, or identify what is touched
- non-trivial work is starting and no context map exists yet
- the request spans multiple files, components, or modules
- a broad change (upgrade, migration, refactor) needs its blast radius identified
- track planning requires knowing which files and tests are affected
- the design analyst, migration planner, or spec writer would benefit from a context handoff

Context mapping must happen before design analysis for non-trivial work.

Use the `design-analyst` in **explore mode** when:
- the user wants options
- there are multiple credible solution shapes
- the change could benefit from creative but practical exploration

Use the `design-analyst` in **ground mode** when:
- the request spans multiple components or modules
- there are likely competing implementation patterns
- the change could introduce a new shared utility, abstraction, or convention
- maintainability, consistency, or reuse is part of the user's concern
- the repository area is old, uneven, or likely to contain local exceptions
- the work is a refactor or architecture-sensitive fix

Use the `migration-planner` when:
- the context map identifies schema changes or ORM model changes
- API contracts are being changed in breaking ways
- shared contracts have multiple consumers that need coordination
- the change requires multi-phase deployment or data backfill
- rollback safety for data changes must be explicitly planned

Use the `security-reviewer` when:
- the implementation touches auth, authz, or access control
- user input handling or validation is modified
- API surface or data exposure changes
- the spec identifies security requirements
- the general reviewer flags a security concern during review

Use the `ui-designer` when:
- a new screen, page section, dialog, or flow must be shaped
- reusable component usage is part of the decision
- consistency with the design system matters before implementation
- frontend implementation is not yet safely bounded from requirements alone

Use the `ui-reviewer` when:
- a UI proposal needs independent critique
- frontend consistency, usability, reuse, or maintainability is in question
- a new reusable UI pattern may be introduced
- the team wants a design-system-aligned challenge pass before implementation or approval

Use the `architecture-challenger` when:
- the local change may reinforce architectural drift
- a patch may have understated cross-module impact
- the repository already shows pattern sprawl or hidden coupling
- the team wants an explicit challenge pass before accepting a stronger pattern
