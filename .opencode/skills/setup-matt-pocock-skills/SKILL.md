---
name: setup-matt-pocock-skills
description: >
  Configure the issue tracker integration used by the /to-spec, /to-tickets,
  and /code-review skills. Creates docs/agents/issue-tracker.md with your
  tracker details so those skills can link specs and tickets to the right place.
---

# Setup: Issue Tracker Integration

The `/to-spec`, `/to-tickets`, and `/code-review` skills can optionally link
to your issue tracker (GitHub Issues, Linear, Jira, etc.). This skill creates
the configuration file they look for.

## When to use

Run this once after cloning the template, if you want those skills to include
tracker links in their output. If you do not use an issue tracker, skip this —
the skills will work without it.

## What this skill does

Creates `docs/agents/issue-tracker.md` with your tracker details.

## Workflow

Ask the user:
1. **Tracker type**: GitHub Issues, Linear, Jira, Notion, or none
2. **Project URL**: the base URL for creating new issues or tickets
3. **Ticket prefix** (if applicable): e.g., `PROJ-`, `ENG-`, or leave blank for GitHub Issues

Then generate `docs/agents/issue-tracker.md` with the following content,
filled in with the user's answers:

```markdown
# Issue Tracker

type: <github-issues | linear | jira | notion | none>
project_url: <base URL>
ticket_prefix: <prefix or blank>
new_issue_url: <URL to create a new issue/ticket>
```

## If no tracker is used

Create the file with:

```markdown
# Issue Tracker

type: none
```

This satisfies the dependency check in `/to-spec`, `/to-tickets`, and
`/code-review` without requiring a real tracker.

## After generation

Tell the user:
- The file has been created at `docs/agents/issue-tracker.md`
- Commit it to the repository so all team members share the same tracker config
- Re-run `/setup-matt-pocock-skills` if the tracker changes
