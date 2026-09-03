# Lessons

Append-only log of patterns learned from past work in this repository.
Captures what worked, what failed, and what to avoid next time.

---

## 2026-08-24 — OpenCode worktree `.git` file can lose its reference

**What happened:** The OpenCode worktree at `.../worktrees/<branch>` has a `.git` file pointing to a missing worktree metadata path. All `git` commands in the worktree directory fail with `fatal: not a git repository: (NULL)`.
**Lesson:** When the git worktree reference breaks, clone from remote to a temp directory (e.g. `C:\Users\<you>\AppData\Local\Temp\opencode\<name>` on Windows) and work from there. Do not attempt to repair the worktree in-place.
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

## 2026-08-25 — Check target repo's `.gitignore` before adopting any template directory structure

**What happened:** Attempted full adoption of `agentic-dev-governance-template` into `multi-model-agentic-ai-assistant`. After copying `.agents/`, discovered it was gitignored twice in the target repo with the comment `# Feynman installer (local)`. Running `git add .agents/` failed silently until `git status` showed the ignore.
**Lesson:** Before adopting a template that introduces new directories, run `git check-ignore -v <directory>` or `grep -r '<directory>' .gitignore` in the target repo first. A gitignored directory is a signal that the repo has a different convention for that space.
**Applies to:** Any session adopting a governance template into an existing repo.

## 2026-08-25 — ruff format on a large file exposes all pre-existing lint issues, not just changed lines

**What happened:** Ran `ruff format` on `information_retrieval.py` (5800 lines) to fix a formatting complaint on our 1-line change. The formatter reformatted the entire file (115 insertions, 320 deletions), causing the CI lint step to find 228 pre-existing ruff violations in the diff — none from our change. Required an additional commit with `ruff check --fix` + `ruff format` to clear them.
**Lesson:** When touching a large legacy file that hasn't been ruff-formatted, do not run `ruff format` on it in the same commit as a logic change. Either: (a) run `ruff check --fix && ruff format` as a dedicated cleanup commit first, or (b) restore the original file and apply only the minimal edit without formatting. The CI compares the entire changed file against main, not just the diff.
**Applies to:** Any session making targeted fixes to large Python files in repos using ruff.

## 2026-08-25 — CI failures can mask each other — fix the first blocker to reveal subsequent ones

**What happened:** `multi-model-agentic-ai-assistant` CI had been failing on a broken doc link since 2026-08-14. Fixing that link (PR #49) revealed a second failure: 3 failing Python tests. Fixing those (PR #50) revealed a fourth failure: 1 more failing test. Each fix exposed the next hidden issue. Total: 4 CI failures that had been silently accumulating.
**Lesson:** When CI has been failing for weeks, assume there are multiple layered failures. After each fix, expect to find more. Plan for 2-3 rounds of CI iteration, not one. Run the full test suite locally before pushing to avoid the round-trip wait.
**Applies to:** Any session fixing a long-standing CI failure in a repo you don't run locally.

## 2026-09-01 — A folder can look like a repo but still be unusable if the git metadata is detached

**What happened:** A workspace path looked like the intended repo, but git commands failed and the folder only contained `.git/` and editor metadata. A fresh clone was required to recover a valid checkout.
**Lesson:** When a workspace feels suspiciously empty, verify both the visible files and the git remote before continuing. If the checkout is invalid, clone a fresh copy rather than trying to reason from the broken path.
**Applies to:** Any Windows OpenCode session where the current folder may be a broken worktree or partial extraction.

## 2026-09-01 — Use repo-agnostic skills for reusable workflows like diagrams and whiteboards

**What happened:** We added portable OpenCode skills for Tldraw and Mermaid rather than embedding those workflows in repo-specific docs.
**Lesson:** Cross-repo workflows should live in reusable skills when possible, with only minimal repo-specific adaptation at the destination. Keep the skill generic, and let the target repo decide how the artifact is stored or rendered.
**Applies to:** Any template or toolchain meant to travel across multiple repositories.

## 2026-09-01 — If winget is unavailable, use the package manager that is actually installed

**What happened:** `winget` was missing on this machine, but Chocolatey was installed and managed the GitHub CLI package.
**Lesson:** Don't assume the default Windows package manager exists or is the right path. Check what is installed first, then use the package manager that actually controls the tool.
**Applies to:** Any Windows tool upgrade, especially CLI utilities like `gh`.

