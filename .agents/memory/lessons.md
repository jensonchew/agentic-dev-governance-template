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

