# Agent-agnostic governance split from tool-specific runtime config

Role definitions (what agents do, their workflows, checklists, escalation rules) live in `.agents/roles/` as plain markdown — portable across any agent framework. OpenCode-specific runtime config (model selection, temperature, permissions) lives in `opencode.json` using `prompt: "{file:...}"` pointers to the role files.

## Considered Options

- **Everything in `.opencode/agents/` as markdown with frontmatter** (original): role content and runtime config coupled in one file. Rejected because it locks governance to one tool — migrating to Claude Code, Cursor, or any other framework requires rewriting all 17 files.
- **Duplicate content in both locations**: keep the full role in `.opencode/agents/` AND in `.agents/roles/`. Rejected because duplication drifts.
- **Split with file references** (chosen): `.agents/roles/` owns the canonical role content. `opencode.json` owns model/temperature/permissions and points to the role file via `prompt: "{file:...}"`.

## Consequences

- Role definitions are portable. Switching agent frameworks means writing new runtime config only.
- Model choices (which LLM for which role) remain an OpenCode-specific concern — intentionally not standardized.
- New roles require creating a file in `.agents/roles/` AND adding an entry to `opencode.json`.
- The split adds one level of indirection. Mitigation: `opencode.json` is the single source of truth for "what agents exist and how they're wired."
