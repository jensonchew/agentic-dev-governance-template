---
name: wrap-up
description: >
  Close the session by updating repository memory with decisions made and
  lessons learned. Invokes docs-updater to append to .agents/memory/decisions.md
  and .agents/memory/lessons.md. IDE and model agnostic — works in any agent
  framework that supports the docs-updater role. Use at the end of every
  session, whether or not an orchestrator was active.
---

# Wrap Up

Record what happened in this session before closing. Keeps repository memory
current so the next session — regardless of IDE, model, or agent framework —
starts with accurate context.

## When to use

- At the end of any working session, before closing the IDE or switching context
- After completing work outside the orchestrator workflow (e.g. direct skill use,
  ad-hoc edits, exploratory discussions)
- When the orchestrator's mandatory memory update did not fire (e.g. session
  ended before track closure)
- Any time you want to manually ensure decisions or lessons are recorded

The orchestrators invoke this automatically via `docs-updater` at track closure.
This skill is the fallback for everything else.

## What this skill does

1. Asks the agent to review the current session context
2. Identifies any decisions, lessons, or documentation gaps
3. Invokes `docs-updater` to write the entries
4. Confirms what was written and what was skipped (with reason)

## Workflow

### Step 1 — Review the session

Without loading extra files, review what happened in this session:

- What was decided? (architectural, implementation, governance, or tooling decisions)
- What was learned? (failures, unexpected behaviour, patterns to avoid, lessons for next time)
- Did any documentation fall out of sync? (`REPOSITORY-CONTEXT.md`, `README.md`, etc.)

### Step 2 — Classify entries

For each item identified:

| Type | Target file | Entry when |
|------|------------|------------|
| Decision | `.agents/memory/decisions.md` | A meaningful choice was made between alternatives |
| Lesson | `.agents/memory/lessons.md` | Something failed, surprised, or should be done differently next time |
| Docs gap | Relevant doc file | A file is now stale or missing content |

Do not record:
- routine implementation steps that produced no meaningful choice
- observations that were not acted on
- speculative future concerns

### Step 3 — Write entries via docs-updater

Invoke `docs-updater` with:
- the list of decisions to append to `.agents/memory/decisions.md`
- the list of lessons to append to `.agents/memory/lessons.md`
- any documentation files that need updating

Use the existing entry format already in those files:

```markdown
## <YYYY-MM-DD> — <short title>

**Context:** <what situation prompted this>
**Decision:** <what was decided>
**Alternatives rejected:** <what was not chosen and why>
**Rationale:** <why this choice was made>
```

For lessons:

```markdown
## <YYYY-MM-DD> — <short title>

**What happened:** <what occurred>
**Lesson:** <what to do differently>
**Applies to:** <when this lesson is relevant>
```

### Step 4 — Confirm

Report:
- entries written (file + title of each)
- entries skipped (with reason — e.g. "no decisions made", "lesson already recorded")
- any documentation files updated

If nothing warranted recording, say so explicitly. Do not silently skip.

## Rules

- always run this at session end — even if you believe nothing changed
- never fabricate decisions or lessons that did not occur in this session
- keep entries factual and specific — avoid generic statements like "we made good progress"
- entries are append-only — do not edit or remove existing memory entries
- if `docs-updater` is unavailable, write entries directly using the edit tool
  and note that docs-updater was bypassed

## IDE and framework portability

This skill is defined in `.agents/skills/` and is framework-agnostic. It can be
invoked by name in any agent framework that supports skill loading:

- **OpenCode**: `/wrap-up`
- **Cursor / Windsurf / other IDEs**: load `SKILL.md` and follow the workflow
- **Automated pipelines**: invoke docs-updater directly with the session summary

The underlying mechanism (`docs-updater`) is also framework-agnostic — it uses
only file editing, which every agent framework supports.
