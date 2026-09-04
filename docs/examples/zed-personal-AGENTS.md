# Personal Zed AGENTS.md (optional)

Copy to **`~/.config/zed/AGENTS.md`** on macOS (same folder as Zed `settings.json`).

Project-specific policy stays in each repo's root `AGENTS.md`. This file is for **cross-repo habits** only.

---

## Session habits

- Start non-trivial work by reading the repo's `AGENTS.md` and `REPOSITORY-CONTEXT.md`.
- Do not edit application code until a task spec exists when the repo uses spec-before-implement (see `.agents/roles/development/spec-writer.md`).
- Prefer a **new Agent thread** between context-mapping and implementation.
- Use `@` file references instead of pasting whole packages or logs.

## When using GitHub Copilot in Zed

- Use Copilot Agent for multi-step work; use **local Ollama inline** (repo `.zed/settings.json`) for tab completion while typing — keep them in separate threads.
- For delivery-charter work, load `.agents/delivery.md` instead of development.

## Output

- Be concise; cite file paths.
- Distinguish facts, assumptions, and recommendations.

## Template repos

If the repo was forked from [agentic-dev-governance-template](https://github.com/jensonchew/agentic-dev-governance-template), see [docs/examples/zed-quickstart.md](../examples/zed-quickstart.md) for thread templates.
