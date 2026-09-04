# IDE adapters

Governance in this template is **IDE-agnostic**. Role definitions, charters, skills, and engineering rules live in plain markdown under `.agents/` and `AGENTS.md` — any agent-capable editor can load them.

**OpenCode** ships first-class wiring (`opencode.json`, slash commands, `.opencode/skills/`). **Cursor**, **Zed**, and **VS Code** use the same governance files with thin adapter notes below.

---

## What is portable vs IDE-specific

| Layer | Location | Portable? |
|-------|----------|-----------|
| Root governance | `AGENTS.md` | Yes — all IDEs |
| Charters & roles | `.agents/development.md`, `.agents/delivery.md`, `.agents/roles/` | Yes |
| Engineering rules | `.agents/instructions.md`, `.agents/instructions/` | Yes |
| Agent-agnostic skills | `.agents/skills/` | Yes — invoke by path or copy to your IDE's skill dir |
| Repository facts | `REPOSITORY-CONTEXT.md` | Yes |
| OpenCode runtime | `opencode.json`, `.opencode/skills/` | OpenCode only |
| Stack setup command | `/setup` | OpenCode (or replicate prompts manually in other IDEs) |

---

## OpenCode

- Root [`opencode.json`](../../opencode.json) maps agents → `{file:./.agents/roles/...}` prompts.
- Commands: `/setup`, `/wrap-up`, orchestrator delegation.
- Run `/setup` after forking to generate stack-specific rules.

---

## Cursor

1. Ensure [`AGENTS.md`](../../AGENTS.md) is loaded (Cursor injects root `AGENTS.md` automatically in many setups).
2. Add thin rules in [`.cursor/rules/`](../../.cursor/rules/) that **reference** policy files — do not duplicate governance text.
3. Copy or symlink skills from [`.agents/skills/`](../../.agents/skills/) into `.cursor/skills/` if you want slash-style harness workflows.
4. Follow the phased workflow in role files: triage → context map → spec → implement → review (fresh chat between spec and implement when threads are long).

**Example Cursor rule (one line):**  
`Follow AGENTS.md and load docs/agent-policy/ or .agents/ charters only when the task needs them.`

---

## Zed

1. Zed auto-loads root [`AGENTS.md`](../../AGENTS.md) as project Agent rules.
2. Use **separate threads** for explore/design vs implement — same phase discipline as OpenCode orchestration.
3. Map OpenCode orchestrator phases to Copilot Agent first messages (e.g. "Context map only — read-only, no edits").
4. Optional: personal rules in `~/.config/zed/AGENTS.md` for operator preferences; keep repo governance in this template.

---

## VS Code (GitHub Copilot / Copilot Chat)

1. Point workspace instructions at [`AGENTS.md`](../../AGENTS.md).
2. Use Copilot Chat modes or custom instructions files that link to `.agents/roles/` for role-specific prompts.
3. Keep `REPOSITORY-CONTEXT.md` open or @-mentioned before run/build/test tasks.

---

## Choosing an IDE

| If you want… | Start with… |
|--------------|-------------|
| Built-in multi-agent orchestration + permissions | **OpenCode** |
| Daily coding + strong inline + Agent mode | **Cursor** |
| Lightweight editor + Copilot Agent | **Zed** |
| Team already on Copilot in VS Code | **VS Code** |

You can switch IDEs without rewriting governance — only the adapter layer changes.

---

## Related

- [`AGENTS.md`](../../AGENTS.md) — root governance
- [`README.md`](../../README.md) — quick start
- [ADR 0002: agent-agnostic governance split](adr/0002-agent-agnostic-governance-split.md)
