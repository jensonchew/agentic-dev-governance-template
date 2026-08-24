# ADR-0003: Model tiering strategy for agent roles

**Date**: 2026-08-24
**Status**: Accepted

---

## Context

`opencode.json` assigns a specific model to each agent. Without an explicit
tiering strategy, model assignments drift — some agents end up over-powered for
their task (wasting cost), others under-powered (producing lower quality output).

Two prior issues surfaced the need for a documented strategy:

1. `build` and `plan` had no explicit model set and inherited the UI-selected
   model, making behaviour session-dependent (fixed in ADR entry 2026-08-24 in
   `decisions.md`)
2. Four agents referenced model IDs that did not exist in the Copilot API
   (`gemini-3.1-pro-preview`, `gpt-5.3`), causing silent agent failures

---

## Decision

Assign models to agents based on a four-tier hierarchy matched to role
responsibility and reasoning demand:

### Tier 1 — Orchestrators and planners (Opus / most capable)

**Model**: `github-copilot/claude-opus-4.6`

Used for: `development-orchestrator`, `delivery-orchestrator`, `plan`

Rationale: Orchestrators coordinate multi-agent work, make planning decisions,
and must reason about scope, boundaries, and trade-offs. Errors at this tier
cascade through the entire track. The cost premium is justified.

### Tier 2 — Specialists and everyday work (Sonnet / versatile)

**Model**: `github-copilot/claude-sonnet-4.6`

Used for: `design-analyst`, `architecture-challenger`, `ui-designer`,
`migration-planner`, `spec-writer`, `security-reviewer`, `platform-evaluator`,
`observability-engineer`, `context-mapper`, `docs-updater`, `build`

Rationale: These roles perform bounded, well-defined tasks that benefit from
strong reasoning but do not need the highest-capability model. Sonnet provides
the best cost-to-capability ratio for the majority of agent work.

### Tier 3 — Independent review (Gemini / alternative vendor perspective)

**Model**: `github-copilot/gemini-3.7-flash`

Used for: `reviewer`, `ui-reviewer`

Rationale: Using a different model family for review reduces the risk of
systematic blind spots — a Sonnet-implemented change reviewed by another Sonnet
instance may share the same failure modes. Gemini provides a genuinely
independent perspective. Flash is sufficient for review tasks.

### Tier 4 — Implementation and pipeline (GPT / strong tool use)

**Model**: `github-copilot/gpt-5.4`

Used for: `implementer`, `pipeline-engineer`, `devsecops-reviewer`

Rationale: GPT-5.4 has strong tool-calling and code generation capabilities
suited for hands-on implementation and structured technical review tasks.

---

## Model ID validation

Model IDs are verified against the live GitHub Copilot API
(`api.githubcopilot.com/models`). A model is considered valid for an agent if:

1. Its bare ID (without `github-copilot/` prefix) appears in the API response
2. It supports `/chat/completions` or `/v1/messages` endpoint

Two mechanisms enforce this:

- **`/check-models` skill** — manual, on-demand validation
- **`.github/workflows/validate-models.yml`** — automated weekly check; opens
  a GitHub issue if any model ID is no longer valid

When a model is deprecated or renamed, replace it with the best available model
in the same tier that satisfies both validation criteria.

---

## Alternatives rejected

**Single model for all agents**: Simpler config, but eliminates cost optimisation
and the independent-reviewer benefit of using a different model family.

**Agent-by-agent ad hoc assignment**: Already led to the drift problem this ADR
addresses. Without a documented strategy, individual assignments lack rationale
and are hard to maintain.

**Always use the newest/most powerful model**: Cost-prohibitive and unnecessary
for bounded specialist tasks. Orchestrators benefit from more capable models;
context mappers and docs updaters do not.

---

## Consequences

- New agents added to `opencode.json` should be assigned a tier based on this
  strategy, with a rationale comment if they deviate
- When upgrading models within a tier (e.g., Sonnet 4.6 → Sonnet 5), update
  all agents in that tier together to maintain consistency
- Model assignments are OpenCode-specific runtime config (`opencode.json`);
  the role definitions in `.agents/roles/` remain tool-agnostic
