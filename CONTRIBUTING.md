# Contributing to this template

This is a governance template, not an application. There is no code to compile and no tests to run.
This guide explains how to adapt it, extend it, and work with it effectively.

---

## Quick start

### 1. Run `/setup`

Before anything else, configure the template for your stack:

```
/setup Go backend with Chi, React frontend with Vite, PostgreSQL with sqlc
```

Or run `/setup` interactively. This generates:
- `REPOSITORY-CONTEXT.md` — filled with your actual paths, commands, and conventions
- `.agents/instructions-stack.md` — stack-specific engineering rules

### 2. Commit `REPOSITORY-CONTEXT.md` and `instructions-stack.md`

These are the two files most agents load on every invocation. Keep them accurate as your stack evolves.

### 3. Start working

For any non-trivial task, use the **development orchestrator**:

```
@development-orchestrator Add a paginated list endpoint for user search
```

For lightweight, self-contained tasks, use a skill directly (see below).

---

## Two workflows: orchestrator vs. skills

The template provides two ways to get work done. Knowing which to use is the most important decision.

### Orchestrator workflow

Use when:
- The task spans multiple files or layers
- The change shape is not obvious (design analysis is needed)
- The task involves schema changes, API contracts, or security-sensitive code
- You want spec → implement → review discipline enforced automatically
- You want a multi-agent review (reviewer + security-reviewer)

How it works:
1. **Context mapper** identifies affected files and blast radius
2. **Design analyst** explores options or grounds the pattern
3. **Spec writer** writes an execution contract
4. **Implementer** writes code and tests in an isolated worktree
5. **Reviewer** validates against the spec and repository rules
6. **Security reviewer** checks for auth/authz, injection, and exposure risks
7. Orchestrator synthesizes and presents results for your approval

Invocation:
```
@development-orchestrator <describe the work>
```

### Skill workflow

Use when:
- The task is self-contained and bounded
- You want a quick output without multi-agent overhead
- You already know the shape of the change and just need execution

| Skill | Use for |
|-------|---------|
| `/implement` | Implement a specific bounded change |
| `/to-spec` | Turn a description into a structured spec |
| `/to-tickets` | Break a feature into tracked tickets |
| `/code-review` | Review a diff or file for issues |
| `/research` | Research a question with evidence before writing code |
| `/tdd` | Write tests first, then implement |
| `/diagnose` | Diagnose a bug or failure |
| `/grill-me` | Test your understanding of a design decision |
| `/zoom-out` | Map an unfamiliar area of the codebase |
| `/check-models` | Validate model IDs in `opencode.json` against the live Copilot API |
| `/handoff` | Prepare a structured handoff between development and delivery |

Skills are lighter and faster. The orchestrator enforces more discipline.
**When in doubt on a non-trivial change, use the orchestrator.**

---

## Adapting the template

### Changing agent models

Edit `opencode.json`. The model tiering strategy used in this template:

| Tier | Use for | Current assignment |
|------|---------|-------------------|
| Opus / powerful | Orchestrators, planning | `github-copilot/claude-opus-4.6` |
| Sonnet / versatile | Specialists, everyday work | `github-copilot/claude-sonnet-4.6` |
| Gemini flash | Independent review perspective | `github-copilot/gemini-3.7-flash` |
| GPT-5.4 | Implementation, pipeline | `github-copilot/gpt-5.4` |

Run `/check-models` to validate model IDs against the live API before committing changes.
A weekly GitHub Actions workflow (`.github/workflows/validate-models.yml`) also catches drift automatically.

### Adding a new agent role

1. Create the role file in `.agents/roles/<charter>/` following the existing pattern:
   - Start with the governance banner
   - Include `## Context loading` (always + on demand)
   - Include `## Role`, `## Rules`, `## Output format`
2. Add the agent entry to `opencode.json` (model, temperature, permissions, prompt pointer)
3. Reference the new agent in the relevant orchestrator's specialist table
4. Add a "when to invoke" note in the orchestrator's `specialist-rules.md`

### Adding a new skill

1. Create `.agents/skills/<skill-name>/SKILL.md` for agent-agnostic skills
   or `.opencode/skills/<skill-name>/SKILL.md` for OpenCode-specific skills
2. Follow the structure: frontmatter (name, description) → workflow → output format → rules
3. If the skill bridges to the orchestrator workflow, document the relationship in this file

### Updating stack rules

Re-run `/setup` whenever your tech stack changes materially. The generated
`.agents/instructions-stack.md` will be overwritten with current rules.

### Updating `REPOSITORY-CONTEXT.md`

Edit it directly. Keep it accurate — it is loaded by almost every agent on every invocation.
Stale context in this file is one of the most common causes of incorrect agent output.

---

## Repository memory

`.agents/memory/decisions.md` and `.agents/memory/lessons.md` are append-only logs.

- **decisions.md** — record architectural and implementation decisions
- **lessons.md** — record patterns learned from past sessions

Add entries by hand or ask the `docs-updater` agent to do it after a session.
Never delete or edit existing entries.

---

## File layout quick reference

```
AGENTS.md                          # Root governance — always loaded
REPOSITORY-CONTEXT.md              # Repository facts — loaded by every agent
opencode.json                      # OpenCode runtime config (models, permissions)

.agents/
├── development.md / delivery.md   # Charter files
├── instructions.md                # Engineering rules hub
├── instructions/                  # Topic sub-files (load on demand)
├── instructions-stack.md          # Generated by /setup — your stack rules
├── governance/                    # Shared governance rules
├── roles/                         # Agent role definitions (agent-agnostic)
├── skills/                        # Agent-agnostic skills
└── memory/                        # Append-only decision and lesson logs

.opencode/
└── skills/                        # OpenCode-specific skills

.github/
└── workflows/
    └── validate-models.yml        # Weekly model ID validation CI
```

---

## Governance model

The template enforces a two-charter model:

- **Development** — context, design, spec, implementation, review
- **Delivery** — CI/CD, pipeline, platform, security posture, observability

Charters do not silently absorb each other's responsibilities.
Work that spans both charters uses the handoff format in `.agents/roles/development/handoffs.md`.

When an agent's guidance conflicts with governance, governance wins.
See `AGENTS.md` for the full precedence hierarchy.
