# AGENTS.md

Stack-agnostic agentic development template with structured governance.
Works with **OpenCode, Cursor, Zed, and VS Code** — see [docs/IDE_ADAPTERS.md](docs/IDE_ADAPTERS.md).
Run `/setup` in OpenCode to configure for your tech stack.

---

## Charters

| Charter | Focus |
|---------|-------|
| [Development](.agents/development.md) | Context, spec, implementation, review |
| [Delivery](.agents/delivery.md) | CI/CD, deployment, runtime, security, cost |

Charters must not silently absorb each other's responsibilities.

---

## Context loading

Agents load context just-in-time, not upfront. The minimum shared context is this file.

**Always loaded** (via opencode.json instructions):
- `AGENTS.md` (this file)

**Loaded by the role file** (each agent loads only what it needs):
- `REPOSITORY-CONTEXT.md` — repository facts, commands, conventions
- `.agents/instructions.md` — engineering rules hub (links to sub-files)
- Relevant charter — only the one that applies to your role

**Loaded on demand** (only when the current task requires it):
- `.agents/instructions/<topic>.md` — specific rule when that topic is relevant
- `.agents/governance/<file>.md` — when governance questions arise
- `.agents/instructions-stack.md` — when stack-specific rules are needed
- Orchestrator sub-files (lifecycle, handoffs, specialist-rules) — when entering that phase

Do not pre-load files you may not need. Load when the task demands it.

---

## Precedence

When guidance conflicts, three tiers apply:

1. **Governance** — `AGENTS.md` and relevant charter
2. **Instructions** — `.agents/instructions.md`, `.agents/instructions-stack.md`, `REPOSITORY-CONTEXT.md`
3. **Task** — Role file, task spec, orchestrator instructions, external skill packs

A lower tier must not override a higher tier.

---

## Core rules

All agents must:
- Stay within the scope of the user request or approved task
- Distinguish facts from assumptions from recommendations
- State material uncertainty when context is incomplete
- Escalate when a request crosses role, charter, or approval boundaries

All agents must not:
- Present guesses as facts
- Silently broaden scope
- Claim validation they did not perform
- Claim production readiness, security posture, or cost posture without evidence

Full behavioral rules: [`.agents/governance/shared-rules.md`](.agents/governance/shared-rules.md)

---

## Governance references

- [Boundaries and handoffs](.agents/governance/boundaries.md)
- [Escalation triggers](.agents/governance/escalation.md)
- [Output format](.agents/governance/output-format.md)
- [Handoff template](docs/templates/HANDOFF.md)

### MGF / AI Verify compliance documents

- [Accountability register](docs/governance/accountability-register.md) — named human owners per charter
- [Human oversight model](docs/governance/human-oversight-model.md) — risk-tiered action classification
- [Incident reporting](docs/governance/incident-reporting.md) — what to report and how
- [Safety assessment](docs/governance/safety-assessment.md) — risk identification and residual posture

Aligned with: IMDA MGF for Agentic AI (2026); AI Verify Testing Framework (11 principles).

---

## Vocabulary reference

When AI coding terminology is unclear, consult the **AI Coding Dictionary**:
https://aicodingdictionary.com

Covers: tokens, context windows, agents, MCP, handoffs, specs, tickets, compaction, hallucination, attention degradation, and more. Use this to resolve ambiguity in terminology used across governance files and skill instructions.

---

## Final principle

When in doubt: preserve governance, keep charters separate, make handoffs explicit, ground conclusions in evidence, escalate rather than improvise.

---

## End-User Responsibility & Education

To safely operate within this agentic framework, human users must:
- Understand when and how agents are being used
- Actively oversee agent actions rather than relying on automation bias
- Retain the foundational software engineering skills necessary to review, audit, and correct agent-generated code and infrastructure
- Know how to manually intervene and stop an agent if it behaves unexpectedly
