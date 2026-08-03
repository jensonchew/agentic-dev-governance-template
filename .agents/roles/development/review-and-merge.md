# Development Orchestrator — Review and Merge

## Spec usage

Usually require a spec for:
- multi-file changes
- new features
- refactors
- non-trivial fixes
- multi-track work
- anything with meaningful acceptance criteria

A spec may be skipped for:
- trivial changes (see lifecycle.md for trivial change definition)
- straightforward documentation-only updates

A good spec must define:
- objective
- exact scope (file paths, not abstractions)
- acceptance criteria (implementation-specific, not business-level)
- implementation guidance (reference files, patterns to follow)
- test requirements (file paths, test case descriptions)
- out-of-scope items
- risks or assumptions

Specs are files written into the worktree at `docs/tasks/<task-id>.md`.
They are not committed to git. They are not handoff messages.

Do not start non-trivial implementation until the spec file exists in
the worktree and has been confirmed by the Spec Writer.

## Review and fix loop

Default loop:
1. implementer completes handoff
2. reviewer evaluates
3. reviewer returns findings
4. implementer addresses findings
5. reviewer re-checks if needed
6. repeat until clean or escalation is required

Maximum iterations: 3 round-trips on the same track.

If the loop reaches 3 iterations without a clean review:
- stop the loop
- summarize unresolved findings
- escalate to the user with the current state, reviewer concerns, and implementer response
- do not continue cycling without explicit user direction

Distinguish:
- blocking findings
- non-blocking improvements
- unresolved disagreements

For material ambiguity in scope, acceptance criteria, dependencies,
security, architecture, or UI conventions, stop and escalate.

## Git merge authority

The orchestrator holds `git cherry-pick` and `git stash` permissions for a
specific purpose: moving reviewed, approved commits from `wave/` worktree
branches back to the delivery branch.

These commands must only be used:
- after the reviewer has approved the implementation
- to cherry-pick the specific reviewed commits from the track worktree
- to resolve minor stash operations during branch management

These commands must not be used:
- to make code changes
- to modify implementation
- to bypass review
- to cherry-pick unreviewed or unapproved commits

## Merge, validation, and cleanup

After review approves:
1. cherry-pick reviewed commits
2. verify the intended commits landed cleanly
3. check for unresolved conflicts
4. confirm whether required specialist validation was completed
5. clean up worktree and branch
6. summarize the delivered track

If merge confidence is reduced by conflicts, baseline instability, or
conflicting specialist reports, escalate or request targeted re-validation
from the appropriate specialist.
