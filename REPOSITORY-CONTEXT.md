# REPOSITORY-CONTEXT.md

# Repository Context

This file is the living memory for agents working in this repository.

Keep it specific to the current repository.
Update it when repository facts, commands, paths, architecture, or known issues change.

Use this file for:
- current repository facts
- canonical commands
- architecture notes grounded in the current codebase
- known constraints and baseline issues
- local conventions that are true in this repository

Do not use this file for:
- role definitions
- general engineering law for all repos
- speculative future-state plans presented as current reality

---

## Repository identity

- Name: `agentic-dev-governance-template`
- Purpose: Stack-agnostic agentic development governance template. Provides multi-charter agent governance (Development + Delivery), role definitions, permission matrices, lifecycle gates, escalation rules, and reusable skills for structured AI-assisted software delivery.
- Business domain: Developer tooling / AI agent governance
- Default branch: `master`
- Repository type: Governance template (no application code — markdown, JSON config, skill files only)
- Frontend package manager: N/A

---

## Structure overview

This is a governance template — there is no application code. Structure is documentation and config only.

- Agent governance hub: `AGENTS.md`
- Repository context (this file): `REPOSITORY-CONTEXT.md`
- OpenCode runtime config: `opencode.json`
- Charter definitions: `.agents/development.md`, `.agents/delivery.md`
- Agent role files: `.agents/roles/development/`, `.agents/roles/delivery/`, `.agents/roles/shared/`
- Engineering instructions: `.agents/instructions.md`, `.agents/instructions/`
- Governance rules: `.agents/governance/`
- Reusable skills: `.agents/skills/`
- OpenCode skills (UI/frontend): `.opencode/skills/`
- Institutional memory: `.agents/memory/decisions.md`, `.agents/memory/lessons.md`
- ADRs: `docs/adr/`
- Handoff template: `docs/templates/HANDOFF.md`

---

## Architecture notes

This repository is a governance template, not an application. Architecture notes cover the agent system design.

- Governance tier 1 (highest): `AGENTS.md` + charter files — cannot be overridden by lower tiers
- Governance tier 2: `.agents/instructions.md` + topic sub-files + `REPOSITORY-CONTEXT.md`
- Governance tier 3 (lowest): Role files, task specs, orchestrator instructions, skill packs
- Context loading strategy: Just-in-time — only `AGENTS.md` auto-loaded; all other files loaded on demand
- Role/runtime split: Universal role content in `.agents/roles/`; OpenCode-specific config (model, temperature, permissions) in `opencode.json` via `prompt: "{file:...}"` pointers
- Charter isolation: Development and Delivery charters are hard-separated; cross-charter work requires the HANDOFF template

---

## Agent configuration

### Primary agents (`opencode.json`)

| Agent | Model | Mode | Can edit files |
|-------|-------|------|---------------|
| `build` | `github-copilot/claude-sonnet-4.6` | primary | yes |
| `plan` | `github-copilot/claude-opus-4.6` | primary | ask |
| `development-orchestrator` | `github-copilot/claude-opus-4.6` | primary | no |
| `delivery-orchestrator` | `github-copilot/claude-opus-4.6` | primary | no |

### Key subagents

| Agent | Model | Purpose |
|-------|-------|---------|
| `implementer` | `github-copilot/gpt-5.4` | Full code implementation |
| `spec-writer` | `github-copilot/claude-sonnet-4.6` | Writes task specs to disk |
| `reviewer` | `github-copilot/gemini-3.1-pro-preview` | Independent code review |
| `security-reviewer` | `github-copilot/claude-sonnet-4.6` | Application security review |
| `context-mapper` | `github-copilot/claude-sonnet-4.6` | Pre-implementation context mapping |
| `docs-updater` | `github-copilot/claude-sonnet-4.6` | Documentation updates |

### Agent bash permissions

No build/test/lint commands — this is a docs/config-only repo. Agents use git read commands only (log, diff, show, status).

### code-memory-mcp

Status: `not configured`

### Vocabulary reference

**AI Coding Dictionary**: https://aicodingdictionary.com
Plain-English definitions for AI coding terms used throughout this repo's governance files and skill instructions (tokens, context windows, agents, MCP, handoffs, specs, tickets, compaction, hallucination, attention degradation, and more).

---

## Canonical commands

This repository has no build, test, or lint pipeline — it is markdown and JSON only.

### Git workflow

- Default branch: `master`
- Remote: `https://github.com/jensonchew/agentic-dev-governance-template.git`
- Push: `git push -u origin <branch>`
- Open PR: `gh pr create --base master`

### Skills installation

To add new skills from mattpocock/skills:
```
npx skills@latest add mattpocock/skills
```
Place skill files under `.agents/skills/<skill-name>/SKILL.md`.

---

## Skills inventory

### `.agents/skills/` (governance-aligned, agent-invokable)

| Skill | Source | Purpose |
|-------|--------|---------|
| `grill-me` | mattpocock/skills | Interview-style planning session |
| `grill-with-docs` | mattpocock/skills | Planning + domain model + inline ADRs |
| `tdd` | mattpocock/skills | Red-green-refactor TDD loop |
| `diagnose` | mattpocock/skills | Disciplined bug diagnosis |
| `handoff` | mattpocock/skills | Compact conversation into handoff doc |
| `zoom-out` | internal | Higher-level codebase perspective |
| `caveman` | internal | Ultra-compressed communication mode |
| `to-spec` | mattpocock/skills | Synthesize conversation into structured spec |
| `to-tickets` | mattpocock/skills | Break spec/plan into tracer-bullet tickets |
| `implement` | mattpocock/skills | End-to-end implement with TDD + code-review |
| `code-review` | mattpocock/skills | Two-axis parallel review (Standards + Spec) |
| `research` | mattpocock/skills | Background agent for primary-source research |
| `resolving-merge-conflicts` | mattpocock/skills | Intent-traced merge conflict resolution |

### `.opencode/skills/` (OpenCode UI skills)

Angular component, di, directives, forms, http, routing, signals, ssr, testing, tooling, design-system, frontend-design, setup, theme-factory, web-artifacts-builder, webapp-testing, mermaid, tldraw.

### `/setup` flow

- Starts with a short stack-family routing question
- Common families are grouped into frontend-led and enterprise .NET paths
- `.NET + Angular` remains a deliberate enterprise option
- `.NET + .NET frontend or no frontend` remains the enterprise fallback for users who want .NET backend without Angular
- The interview then narrows to the missing stack, architecture, data, testing, and tooling details

---

## Local development constraints

- No build toolchain required — this is a docs/config-only repository
- Git worktree note: if a local OpenCode worktree has a broken `.git` file reference, clone from remote to a temp directory and work from there rather than repairing in place.
- Agents should never commit: secrets, generated files, or personal credentials

---

## Known baseline issues

- None at this time.

---

## Repository-specific conventions

- Naming conventions: kebab-case for all files and directories
- Branching convention: `opencode/<feature-name>` for agent-created branches
- PR convention: merge feature branches → `master` via GitHub PR
- Documentation expectations: update `REPOSITORY-CONTEXT.md` and `.agents/memory/decisions.md` after any structural or config change
- Skills convention: agent-invokable skills go in `.agents/skills/`; OpenCode UI skills go in `.opencode/skills/`

---

## Update guidance

Update this file when:
- commands change
- paths move
- architecture boundaries change
- new integrations are added
- baseline issues are discovered or resolved
- agent-relevant repository facts become stale

If a fact is not yet true in the repository, do not record it here as reality.
