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

## 2026-05-28 — Three-tier precedence (Governance > Instructions > Task)

**Context:** Original had 8 precedence levels creating confusion about which rule wins.
**Decision:** Flatten to 3 tiers. Governance (AGENTS.md + charter) > Instructions (engineering rules + repo context) > Task (role file + spec + orchestrator).
**Alternatives rejected:** Keep 8 levels (too complex to remember), 2 levels (not granular enough to resolve real conflicts).
**Rationale:** Any conflict can be resolved by asking "which tier?" — simple, memorable, enforceable.
