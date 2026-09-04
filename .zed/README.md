# Zed workspace settings (optional)

Zed loads root [`AGENTS.md`](../AGENTS.md) automatically as project Agent rules. **No committed AI settings are required** for governance to work.

## Optional: local Ollama inline

If you use [Ollama](https://ollama.com) for tab completion (separate from GitHub Copilot Agent):

1. Copy [`settings.json.example`](./settings.json.example) → `settings.json`
2. Set `default_model` to a model you have pulled (`ollama list`)
3. Keep `settings.json` local — it is listed in `.gitignore` so operator-specific endpoints are not committed

**GitHub Copilot** in Zed is independent of Ollama settings.

## Quickstart

Thread templates and phased workflow: [`docs/examples/zed-quickstart.md`](../docs/examples/zed-quickstart.md)

IDE overview: [`docs/IDE_ADAPTERS.md`](../docs/IDE_ADAPTERS.md)
