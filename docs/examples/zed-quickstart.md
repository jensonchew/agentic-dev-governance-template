# Zed quickstart

**Purpose:** Use this template's governance in [Zed](https://zed.dev) with GitHub Copilot Agent — without OpenCode slash commands.

**Related:** [IDE adapters](../IDE_ADAPTERS.md) · [AGENTS.md](../../AGENTS.md) · [`.zed/README.md`](../../.zed/README.md)

---

## What Zed loads automatically

| Layer | File | Notes |
|-------|------|--------|
| Project governance | [`AGENTS.md`](../../AGENTS.md) | Zed Agent rules — loaded for this repo |
| Charters | [`.agents/development.md`](../../.agents/development.md), [`.agents/delivery.md`](../../.agents/delivery.md) | Load when task scope is clear |
| Repository facts | [`REPOSITORY-CONTEXT.md`](../../REPOSITORY-CONTEXT.md) | Commands, paths, conventions |
| Personal habits | `~/.config/zed/AGENTS.md` | Optional — see [zed-personal-AGENTS.md](./zed-personal-AGENTS.md) |

Zed does **not** auto-load `.agents/skills/` — reference skill files by path when needed.

---

## OpenCode commands → Zed first messages

Paste these as the **first message** in a new Zed Agent thread.

### Stack setup (`/setup` in OpenCode)

```
Read AGENTS.md and REPOSITORY-CONTEXT.md.
Help me configure this repo for my stack: <e.g. Go + Chi, React + Vite, PostgreSQL>.
Update REPOSITORY-CONTEXT.md and .agents/instructions-stack.md with accurate paths and commands.
Do not invent tools — ask if unsure.
```

### Development orchestrator (non-trivial work)

```
You are the development orchestrator. Read .agents/roles/development/orchestrator.md and .agents/development.md.
Do not edit code directly — coordinate context mapping, spec, implementation, and review.
Load REPOSITORY-CONTEXT.md first.
Task: <describe goal>
```

### Context map (read-only)

```
Follow .agents/roles/shared/context-mapper.md (or development context-mapper role).
Read-only — list affected files, tests, and risks. No edits.
Task: <change or bug>
```

### Spec before implement

```
Follow .agents/roles/development/spec-writer.md.
Write an execution spec under docs/tasks/<YYYY-MM-DD-slug>.md — docs only, no application code.
Task: <feature or fix scope>
```

### Implement (fresh thread)

```
New thread — implement only.
Read docs/tasks/<task-id>.md and REPOSITORY-CONTEXT.md.
Follow .agents/roles/development/implementer.md.
```

### Review (fresh thread)

```
Read-only review. Diff vs docs/tasks/<task-id>.md and AGENTS.md policy.
Follow .agents/roles/development/reviewer.md. No edits.
```

### Session wrap-up (OpenCode `/wrap-up`)

```
Follow .agents/skills/wrap-up/SKILL.md.
Update .agents/memory/decisions.md and .agents/memory/lessons.md if warranted.
Summarize what was verified and what remains open.
```

### Cross-charter handoff

```
Use docs/templates/HANDOFF.md.
Hand off from development to delivery (or reverse) with explicit scope and verification steps.
```

---

## Phased workflow (token-efficient)

Use a **new thread per phase** — same discipline as OpenCode orchestration.

| Phase | Edit code? | Zed first message snippet |
|-------|------------|---------------------------|
| **Triage** | No | "Restate goal; pick development vs delivery charter. No edits." |
| **Context map** | No | "Affected files and tests only; follow .agents/skills/zoom-out/SKILL.md if broad." |
| **Design** | No | "Options and trade-offs; read .agents/roles/development/design-analyst.md." |
| **Spec** | Docs only | "Write docs/tasks/<id>.md per spec-writer role; no code." |
| **Implement** | Yes | New thread: attach spec + `@` relevant files only. |
| **Review** | No | "Diff vs spec; follow reviewer role; no edits." |
| **Handoff** | Docs | Use handoff template above. |

---

## Skills by path

| Skill | Path | When |
|-------|------|------|
| Zoom out | `.agents/skills/zoom-out/SKILL.md` | Blast radius, affected modules |
| TDD | `.agents/skills/tdd/SKILL.md` | Bug fix with regression test |
| Diagnose | `.agents/skills/diagnose/SKILL.md` | Incidents, logs, failures |
| Grill with docs | `.agents/skills/grill-with-docs/SKILL.md` | Stress-test a plan |
| To spec | `.agents/skills/to-spec/SKILL.md` | User-invokable spec synthesis |
| Code review | `.agents/skills/code-review/SKILL.md` | User-invokable review |
| Wrap up | `.agents/skills/wrap-up/SKILL.md` | End session, update memory |

Say: **"Follow `.agents/skills/tdd/SKILL.md`"** — Zed reads the file like any other doc.

---

## Copilot vs local Ollama in Zed

| Mode | Use for |
|------|---------|
| **GitHub Copilot Agent** | Multi-file work, orchestration, reviews (subscription) |
| **Local Ollama** (optional `.zed/settings.json`) | Tab completion, offline inline |

Do not mix both in one thread. For full permission-gated orchestration (orchestrator → implementer with deny rules), run **OpenCode in Zed's terminal** — see [`opencode.json`](../../opencode.json).

Copy [`.zed/settings.json.example`](../../.zed/settings.json.example) to `.zed/settings.json` if you want local Ollama inline (file is gitignored by default).

---

## Verify after changes

Use commands from `REPOSITORY-CONTEXT.md` for your stack (test, lint, build). The template does not ship a single global verify script — `/setup` fills in repo-specific commands.

---

## Optional: personal Zed router

Add to `~/.config/zed/AGENTS.md` (see [zed-personal-AGENTS.md](./zed-personal-AGENTS.md)):

```
For repos using agentic-dev-governance-template: start non-trivial work by reading AGENTS.md and REPOSITORY-CONTEXT.md; use a new Agent thread between spec and implement.
```
