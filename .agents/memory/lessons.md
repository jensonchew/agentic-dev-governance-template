# Lessons

Append-only log of patterns learned from past work in this repository.
Captures what worked, what failed, and what to avoid next time.

---

## 2026-08-24 — OpenCode worktree `.git` file can lose its reference

**What happened:** The OpenCode worktree at `.../glowing-star` has a `.git` file pointing to `Downloads/.../worktrees/glowing-star`, but the parent repo's `.git` dir only contains `objects` — the worktree metadata path does not exist. All `git` commands in the worktree directory fail with `fatal: not a git repository: (NULL)`.
**Lesson:** When the git worktree reference breaks, clone from remote to a temp directory (`C:\Users\jensonc\AppData\Local\Temp\opencode\<name>`) and work from there. Do not attempt to repair the worktree in-place.
**Applies to:** Any session working in an OpenCode-managed worktree on Windows.

## 2026-08-24 — Setting `$env:GIT_DIR` in a bash tool call pollutes subsequent calls

**What happened:** Setting `$env:GIT_DIR` explicitly in one tool call to test a git path caused all subsequent git commands in the same shell session to fail with `fatal: not a git repository: (NULL)`, even after `Remove-Item Env:GIT_DIR` in a child shell.
**Lesson:** Never set `GIT_DIR` directly in a bash tool call. Use `git -C <path>` instead for path overrides. If `GIT_DIR` is accidentally set, restart the session.
**Applies to:** Any git diagnostics or path-override work in the OpenCode bash tool.

## 2026-08-24 — `gh auth refresh` cannot complete inside OpenCode's shell environment

**What happened:** `gh auth refresh -h github.com -s workflow` uses a polling-based device flow. The command displays a one-time code, then polls GitHub until the user completes browser auth. OpenCode's bash tool kills the process after the timeout (even at 5 minutes), so the polling never receives the OAuth callback and the local token is never updated — even when the user completes the browser step.
**Lesson:** Do not attempt `gh auth refresh` inside OpenCode. For pushing `.github/workflows/` files (which require `workflow` scope), use the GitHub web UI editor directly on the branch. Alternatively, use a PAT with `repo` + `workflow` scopes set as `GITHUB_TOKEN` in the environment before the session.
**Applies to:** Any session that needs to push or update workflow files in `.github/workflows/`.

## 2026-08-24 — GitHub returns 403 (disguised as 404) when workflow scope is missing on API calls

**What happened:** Attempting to create or update `.github/workflows/` files via the GitHub Contents REST API without `workflow` scope returned HTTP 404 when the file did not yet exist, and a 403 with a message about `workflow` scope once the file existed. The 404 was misleading — it was a permissions rejection, not a missing resource.
**Lesson:** When the GitHub Contents API returns 404 for a workflow file operation, check OAuth scopes before assuming the branch or path is wrong. Both `git push` and `PUT /repos/.../contents/.github/workflows/...` require `workflow` scope — there is no API workaround without it.
**Applies to:** Any session creating or modifying GitHub Actions workflow files.

## 2026-08-24 — Gap analysis results may reflect stale file state — verify before fixing

**What happened:** The gap analysis identified three delivery specialist files (`pipeline-engineer.md`, `devsecops-reviewer.md`, `observability-engineer.md`) as missing the governance banner. Reading the actual files showed the banners were already present — the analysis was working from a prior cached or inferred state.
**Lesson:** Always read the actual file before applying a gap analysis fix. Gap analysis tools and agents can reflect stale or inferred state. One file read prevents a wasted edit and a misleading commit.
**Applies to:** Any session applying findings from a batch gap analysis.

