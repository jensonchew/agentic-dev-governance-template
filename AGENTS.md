# AGENTS.md

Stack-agnostic agentic development template with structured governance.
Run `/setup` to configure for your tech stack.

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

---

## Final principle

When in doubt: preserve governance, keep charters separate, make handoffs explicit, ground conclusions in evidence, escalate rather than improvise.
