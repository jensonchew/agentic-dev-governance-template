# Decisions

Append-only log of architectural and implementation decisions.
Each entry records what was decided, why, and what alternatives were rejected.

---

## 2026-05-28 — Just-in-time context loading over eager bulk loading

**Context:** Agents were pre-loading all governance files, both charters, full instructions, and REPOSITORY-CONTEXT.md before seeing their task — 600+ lines of context before any useful work.
**Decision:** Just-in-time loading. Only `AGENTS.md` (74 lines) is globally auto-loaded. Each agent loads only what its current task requires.
**Alternatives rejected:** Eager loading (wastes context window, increases token cost, agents skip long preambles under pressure), per-agent hardcoded reading lists (still loads too much upfront).
**Rationale:** Research shows LLMs skip long governance preambles under context pressure. Smaller upfront context = better adherence to what is loaded. Sub-files loaded on demand stay fresh in context when relevant.

## 2026-05-28 — Agent-agnostic roles in .agents/roles/, runtime config in opencode.json

**Context:** Role definitions were mixed with OpenCode-specific frontmatter (model, temperature, permissions) in `.opencode/agents/` markdown files.
**Decision:** Split: universal role content in `.agents/roles/`, OpenCode runtime config in `opencode.json` using `prompt: "{file:...}"` pointers.
**Alternatives rejected:** Keep everything in `.opencode/agents/` (locks governance to one tool), duplicate content in both locations (drift risk).
**Rationale:** Makes governance portable across agent frameworks. Only the runtime wiring (which model, what permissions) is tool-specific.

## 2026-05-28 — Drop "cell" terminology, use plain charter names

**Context:** Original template used "Development Cell" / "Delivery Cell" as grouping nouns.
**Decision:** Drop "cell" everywhere. Files are `development.md` / `delivery.md`. Folders are `development/` / `delivery/`.
**Alternatives rejected:** Keep "cell" (adds jargon with no functional benefit), use "team" or "group" (equally unnecessary).
**Rationale:** The files speak for themselves. Extra grouping nouns add cognitive load without aiding navigation.

## 2026-05-28 — Progressive disclosure via hub files + topic sub-files

**Context:** Orchestrator files were 450-730 lines. Instructions file was 213 lines. All content inlined.
**Decision:** Hub files (~80-110 lines) link to topic sub-files loaded only when entering that phase or topic.
**Alternatives rejected:** Keep monolithic files (violates progressive disclosure, wastes context), split into too many tiny files (fragmentation).
**Rationale:** Agents load the sub-file relevant to their current phase. Hub files orient without overwhelming.

## 2026-08-24 — Pin explicit models for `build` and `plan` primary agents

**Context:** `build` and `plan` had no `model` set in `opencode.json`, so they inherited whichever model was selected in the UI — inconsistent across sessions.
**Decision:** Pin `build` to `github-copilot/claude-sonnet-4.6` (cost-effective for everyday coding) and `plan` to `github-copilot/claude-opus-4.6` (deeper reasoning for planning and analysis).
**Alternatives rejected:** Opus for both (unnecessary cost for build), Sonnet for both (plan benefits from deeper reasoning), leave unset (too session-dependent).
**Rationale:** Aligns with the existing tiering strategy — orchestrators use Opus, everyday workers use Sonnet. Removes dependency on UI state.

## 2026-08-24 — Add Matt Pocock engineering skills to `.agents/skills/`

**Context:** The skills inventory covered governance-aligned patterns (grill-me, tdd, diagnose, handoff) but lacked user-invokable workflow bridges: spec synthesis, ticket breakdown, end-to-end implement, code review, research, and conflict resolution.
**Decision:** Add 6 skills from `mattpocock/skills`: `to-spec`, `to-tickets`, `implement`, `code-review`, `research`, `resolving-merge-conflicts`. Placed in `.agents/skills/` alongside existing governance skills.
**Alternatives rejected:** Full `npx skills@latest add` install (would add duplicates of grill-me, grill-with-docs, tdd, diagnose, handoff already present; also adds non-engineering skills not relevant here), skip entirely (leaves workflow gap between planning and implementation).
**Rationale:** These skills fill the user-facing workflow layer: spec synthesis feeds the spec-writer agent, tickets feed the implementer, code-review provides a user-invokable complement to the reviewer subagent, research supports evidence-before-assertion governance rules, and conflict resolution supports the implementer's multi-branch work.

## 2026-08-24 — Align governance docs with IMDA MGF for Agentic AI and AI Verify

**Context:** The template had robust technical governance (role files, permissions, escalation rules) but no human-facing compliance documentation mapping it to recognised AI governance frameworks. A gap remediation pass identified four missing artefacts.
**Decision:** Create four documents under `docs/governance/` explicitly aligned to IMDA's Model AI Governance Framework for Agentic AI (v1.0, Jan 2026) and Singapore's AI Verify testing principles:
- `safety-assessment.md` — risk register with residual posture (IMDA MGF + AI Verify 4/5/6)
- `accountability-register.md` — named human owners per charter (IMDA MGF Accountability + AI Verify 9)
- `human-oversight-model.md` — Tier 1/2/3 risk-tiered oversight model (IMDA MGF Human Oversight + AI Verify 10)
- `incident-reporting.md` — incident definition, severity tiers, reporting path (IMDA MGF + AI Verify 4)

Companion updates: `shared-rules.md` (reversibility principle + prompt injection defence), `escalation.md` (irreversible action + injection triggers), `output-format.md` (terminology fix), `AGENTS.md` (compliance document references).
**Alternatives rejected:** Reference frameworks only in README (insufficient — agents and auditors need structured, loadable documents); create a single combined compliance doc (harder to load on demand; mixes concerns).
**Rationale:** IMDA MGF for Agentic AI directly addresses the risk profile of this template (multi-agent, autonomous actions, tool use). AI Verify provides testable principles. Explicit alignment means the template is audit-ready out of the box and gives teams a documented compliance basis when adapting it for regulated environments.

## 2026-08-24 — Model ID validation: manual skill + weekly CI, not auto-on-open

**Context:** Four agent model IDs in `opencode.json` were invalid (`gemini-3.1-pro-preview`, `gpt-5.3`). Discussed whether to auto-validate on IDE open, require manual triggering, or use CI.
**Decision:** Two-mechanism approach: `/check-models` skill for on-demand manual validation; `.github/workflows/validate-models.yml` for automated weekly checks that open a `model-drift` issue if drift is found.
**Alternatives rejected:** Auto-modify `opencode.json` on session start (mutates config while session is already loaded; breaks offline; model replacement requires judgment not just lookup); single manual skill only (relies on humans remembering to run it).
**Rationale:** Manual skill covers immediate needs; CI catches drift automatically without session impact. Neither modifies files autonomously — both surface findings for human review and approval.

## 2026-08-24 — Four-tier model tiering strategy for agent roles

**Context:** Model assignments in `opencode.json` had drifted (invalid IDs, no documented rationale). Needed a principled basis for assigning and upgrading models.
**Decision:** Tier 1 Opus (orchestrators/plan), Tier 2 Sonnet (specialists/everyday), Tier 3 Gemini flash (independent review — different vendor perspective), Tier 4 GPT-5.4 (implementation/pipeline). Documented in `docs/adr/0003-model-tiering-strategy.md`.
**Alternatives rejected:** Single model for all (no cost optimisation, no independent-review benefit); ad hoc per-agent assignment (already caused the drift problem); always use newest/most powerful (cost-prohibitive, unnecessary for bounded tasks).
**Rationale:** Tiering aligns cost with reasoning demand. Different vendor for review reduces systematic blind spots. Documented strategy prevents future unanchored drift.

## 2026-08-24 — CI workflow permissions: minimum required, not convenience defaults

**Context:** The `validate-models.yml` workflow was initially written with `contents: write` and `pull-requests: write` — both unnecessary for a read-then-report-issues workflow.
**Decision:** Tighten to `contents: read` (checkout only) and `issues: write` (open/comment/close model-drift issues).
**Alternatives rejected:** Keep `contents: write` (opens unnecessary blast radius — scheduled workflow could push commits); keep `pull-requests: write` (workflow never touches PRs).
**Rationale:** Principle of least privilege. A scheduled read-and-report workflow has no legitimate need to write to the repository or manage PRs.

## 2026-08-24 — Session memory automation: three-layer agnostic approach

**Context:** Repository memory was only updated on explicit human request. Sessions ended with no decisions or lessons recorded. Any new session — in any IDE — started blind.
**Decision:** Three layers: (1) Governance rule in both orchestrator `lifecycle.md` files — mandatory `docs-updater` invocation before session close; (2) `docs-updater` guidance in both `specialist-rules.md` files; (3) `.agents/skills/wrap-up/SKILL.md` — IDE-agnostic fallback skill for non-orchestrator sessions, plus `/wrap-up` command in `opencode.json` as OpenCode-specific convenience trigger.
**Alternatives rejected:** OpenCode session-end hook (not supported by OpenCode); auto-commit memory on every turn (too noisy, not meaningful); memory update only via orchestrator (misses ad-hoc and skill-led sessions).
**Rationale:** Governance rule covers orchestrator-led sessions automatically. Wrap-up skill covers everything else with a single command. Agnostic layer (`.agents/skills/`) ensures the mechanism works in any IDE, not just OpenCode.

