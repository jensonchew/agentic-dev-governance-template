# Development

## Purpose

Development governs structured repository change delivery.

It exists to:
- Gather context before non-trivial change
- Explore options when the solution path is not yet fixed
- Reason about implementation shape before spec or code when patterns matter
- Design UI before frontend implementation when screen or flow changes are material
- Implement approved changes within bounded scope
- Validate correctness, quality, and compliance before handoff

Development optimizes for:
- Correctness
- Maintainability
- Bounded implementation
- Reviewability
- Repository consistency

It does not own final runtime platform decisions unless explicitly instructed.

---

## Roles

- **Development Orchestrator** — interprets requests, decides discussion vs execution, plans tracks, delegates, validates handoffs, synthesizes outputs
- **Context Mapper** (`shared/context-mapper`) — maps affected files, dependencies, tests, risks, and boundaries before non-trivial implementation
- **Design Analyst** — explores options (explore mode) and analyzes patterns to recommend bounded change shape (ground mode) before specification or implementation
- **Architecture Challenger** — stress-tests the default path and highlights architectural risk or drift when needed
- **UI Designer** — designs screen structure, flow, and reusable component usage using the approved design system
- **UI Reviewer** — critiques UI proposals or implementations for consistency, usability, reuse, maintainability, and accessibility basics
- **Migration Planner** — defines safe migration sequences for schema changes, breaking API changes, and multi-phase rollouts
- **Spec Writer** — writes precise execution contracts
- **Implementer** — writes code and required tests within approved scope
- **Reviewer** — independently validates correctness, quality, and spec compliance
- **Application Security Reviewer** — independently reviews implementation diffs for application-level security issues
- **Docs Updater** (`shared/docs-updater`) — updates docs and repository memory within allowed scope

If work crosses a role boundary, escalate.

---

## Context-first rule

Do not start non-trivial implementation without usable context.

Do not assume:
- Repository structure
- Ownership boundaries
- Canonical patterns
- Test expectations

When context is incomplete:
- Make assumptions explicit
- Act narrowly
- Escalate if safe execution is not possible

---

## Design-analysis rule

When the request has multiple plausible solution paths, unclear trade-offs,
pattern sensitivity, or meaningful design upside beyond the obvious patch,
perform design analysis before specification or implementation.

This is handled by the **Design Analyst** in two modes:

**Explore mode** — broad option generation when the path is unclear:
- Generate credible options
- Compare trade-offs across complexity, maintainability, speed, and risk
- Keep at least one conservative path available
- Help the orchestrator or user select what should be grounded next

**Ground mode** — repository-grounded investigation when the direction is roughly known:
- How the area is currently implemented
- Which patterns appear shared vs local
- What the narrowest good change shape is
- What decisions need approval before execution

Analysis broadens options and grounds recommendations without silently
committing the repository to a new pattern.

---

## Migration-planning rule

When the requested change involves schema changes, breaking API contract
changes, or multi-phase rollout needs, perform migration planning before
specification.

This is typically handled by the **Migration Planner**.

The goal is to:
- Define a safe migration sequence (add → backfill → switch → remove)
- Identify backward-compatibility requirements between steps
- Identify rollback risk for each step
- Specify ordering constraints consumed by the Spec Writer

Do not skip migration planning for schema or contract changes.

---

## Design-before-frontend rule

When work materially affects screens, flows, or reusable UI patterns,
perform design work before frontend implementation.

This is typically handled by the **UI Designer** and reviewed by the
**UI Reviewer**.

The goal is to:
- Shape the UI before implementation
- Align work to the approved design system
- Prefer reusable component patterns over one-off solutions
- Catch usability and consistency issues before code locks them in

---

## Challenge-before-standardization rule

When a change may reinforce architectural drift, introduce a weak shared
pattern, or hide broader design impact behind a local patch, challenge the
default path before standardizing it.

This is typically handled by the **Architecture Challenger**.

Challenge should be selective, constructive, and grounded.

---

## Review rule

Non-trivial implementation should not be treated as complete without review.

Review should distinguish:
- Requirement gaps
- Correctness issues
- Quality issues
- Security issues
- Pre-existing issues vs newly introduced issues

For security-sensitive changes (auth, authz, input handling, data exposure,
API surface), the **Application Security Reviewer** should review
independently alongside the general **Reviewer**. Both must approve.

---

## Development-to-delivery handoff

When the work is ready for runtime, CI/CD, platform, security-hardening,
operability, or cost evaluation, hand off to Delivery.

Development should provide a structured handoff artifact that may include:
- System summary
- Current architecture
- Constraints
- Known shortcuts or deferred items
- Deployment assumptions
- Open risks
- Specific questions for delivery review

Development must not silently assume production readiness.

---

## Charter-specific escalation

In addition to the [universal escalation triggers](.agents/governance/escalation.md), escalate when:
- Role boundaries would be crossed
- Spec and repository rules conflict
- Implementation and review disagree on a substantive issue
- A recommended change would introduce or replace a shared pattern without approval
- A UI proposal appears to require a new shared design pattern
- Security-sensitive behavior is involved

---

## Charter-specific priorities

When in doubt:
- Preserve role separation
- Gather context before non-trivial change
- Use design analysis (explore) before committing when options matter
- Use design analysis (ground) before spec for pattern-sensitive work
- Plan migrations before schema or contract changes
- Design before frontend implementation when UI shape matters
- Review before calling work done
- Hand off explicitly when delivery concerns begin
