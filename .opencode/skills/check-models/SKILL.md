---
name: check-models
description: >
  Validate all model IDs in opencode.json against the live GitHub Copilot
  models API. Reports any invalid or unavailable model IDs and suggests
  verified replacements. Does not modify any files — output only.
  Run this after any Copilot subscription change, or periodically to catch
  model deprecations before they cause agent failures.
---

# Check Models

Validate the model IDs in `opencode.json` against the live GitHub Copilot models API.

## When to use

- When an agent fails to initialize with a model-not-found error
- After a GitHub Copilot plan change (Pro → Pro+, or org policy changes)
- When onboarding this template to a new machine or GitHub account
- Periodically to get ahead of model deprecations (a GitHub Actions workflow also does this automatically — see `.github/workflows/validate-models.yml`)

## What this skill does

1. Reads all `model` values from `opencode.json`
2. Fetches the live model list from the GitHub Copilot API
3. Diffs the two lists
4. Reports: which models are valid, which are invalid, and suggested replacements for any invalid ones
5. **Does not modify any files** — presents findings for human review

## Workflow

### Step 1 — Read opencode.json

Read `opencode.json` and extract every `"model"` value. Build a table:

| Agent key | Model ID currently set |
|-----------|----------------------|
| build | ... |
| plan | ... |
| development-orchestrator | ... |
| ... | ... |

### Step 2 — Fetch live model list

Run:
```bash
gh api https://api.githubcopilot.com/models \
  -H "Authorization: Bearer $(gh auth token)" \
  -H "Copilot-Integration-Id: vscode-chat" \
  --jq '[.data[] | {id: .id, name: .name, category: .model_picker_category, endpoints: .supported_endpoints}]'
```

If the API call fails (auth, network, or permissions), report the error clearly and stop. Do not guess at model availability.

### Step 3 — Strip the provider prefix

`opencode.json` uses `github-copilot/<model-id>` format. Strip `github-copilot/` to get the bare model ID for comparison.

### Step 4 — Diff

For each agent's model ID:
- **Valid** — bare ID exists in the API response and supports `/chat/completions` or `/v1/messages`
- **Invalid** — bare ID does not appear in the API response
- **Endpoint warning** — bare ID exists but only supports `/responses` or `ws:/responses` (may not work with all OpenCode features)

### Step 5 — Suggest replacements

For any invalid model, suggest the best verified replacement based on the agent's role tier:

| Original intent | Suggested replacement |
|----------------|----------------------|
| Powerful Anthropic (orchestrator, plan) | `github-copilot/claude-opus-4.6` or newer Opus |
| Versatile Anthropic (specialist, everyday) | `github-copilot/claude-sonnet-4.6` or newer Sonnet |
| Google review model | `github-copilot/gemini-3.7-flash` |
| OpenAI implementer / pipeline | `github-copilot/gpt-5.4` |
| Lightweight / fast | `github-copilot/gpt-5-mini` or `github-copilot/claude-haiku-4.5` |

Always confirm the suggested replacement exists in the live API response before recommending it.

### Step 6 — Report

Output a summary table and, if any issues were found, a recommended diff to apply to `opencode.json`.

## Output format

### Model Validation Report

**Checked**: <date/time>
**Source**: GitHub Copilot API (`api.githubcopilot.com/models`)

#### Results

| Agent | Model ID | Status | Notes |
|-------|----------|--------|-------|
| build | github-copilot/claude-sonnet-4.6 | ✅ Valid | |
| plan | github-copilot/claude-opus-4.6 | ✅ Valid | |
| ... | ... | ✅/❌/⚠️ | |

**Status key**:
- ✅ Valid — confirmed in API, supports chat completions
- ❌ Invalid — not found in API response
- ⚠️ Endpoint warning — found but may have limited endpoint support

#### Recommended changes (if any)

```json
// opencode.json — suggested replacements
"agent-name": {
  "model": "github-copilot/<replacement>"  // was: github-copilot/<old-id>
}
```

#### No action needed (if all valid)

All model IDs in `opencode.json` are confirmed valid. No changes required.

## Rules

- never modify `opencode.json` directly — this skill is read-only
- if the API call fails, stop and report the error; do not assume models are valid
- only suggest replacements that appear in the live API response
- if a replacement candidate also fails the endpoint check, note it and suggest an alternative
- after presenting findings, remind the user that the GitHub Actions workflow (`.github/workflows/validate-models.yml`) will catch future drift automatically
