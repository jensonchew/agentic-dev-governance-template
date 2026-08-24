# Safety Assessment

Aligned with: IMDA MGF for Agentic AI — Trusted Development and Deployment; AI Verify Principles 4 (Safety), 5 (Security), 6 (Robustness).

This document records the risk assessment that justifies the current permission
settings and governance controls in this agentic development system. It is a living
document — update it when the permission matrix or agent roster changes.

---

## Scope

This assessment covers the agentic development system defined in `opencode.json`,
governed by the charters in `.agents/development.md` and `.agents/delivery.md`.

**System purpose:** AI-assisted software development and delivery — specification,
implementation, code review, security review, and delivery pipeline evaluation.

**Operating environment:** Developer workstations; changes are committed to git
and reviewed before any production impact.

**AI models in use:** See `REPOSITORY-CONTEXT.md` — Agent configuration table.

---

## Risk identification

### R1 — Unintended file modification
**Description:** An agent writes, overwrites, or deletes files outside the approved
task scope.
**Likelihood:** Medium — agents have broad file access when implementing.
**Impact:** Medium — changes are in git; reversible via `git revert`.
**Control:** `spec-writer` and `docs-updater` are the only non-implementer agents
with edit permissions. `implementer` works in an isolated worktree. Review gate
catches unintended changes before merge.
**Residual risk:** Low.

### R2 — Irreversible action without approval
**Description:** An agent executes a destructive or irreversible action (push,
deploy, delete) without human confirmation.
**Likelihood:** Low — bash permissions are explicitly allowlisted.
**Impact:** High — depends on action; could affect production.
**Control:** Tier 3 actions classified in human oversight model. `"deny"` on
destructive bash commands for all agents except `implementer`. Git push requires
human to run it manually after review. Shared rule: never execute irreversible
action without explicit human confirmation.
**Residual risk:** Low for current agent roster.

### R3 — Prompt injection
**Description:** Malicious content embedded in tool results, file reads, or
external data redirects an agent to perform unauthorised actions.
**Likelihood:** Low in a closed development environment; higher if agents
fetch external content.
**Impact:** High — could cause scope expansion, data exfiltration, or
unauthorised commits.
**Control:** Shared rule prohibiting agents from following instructions in
tool results. Escalation trigger for suspected injection. `webfetch` permission
controlled per agent.
**Residual risk:** Medium — no automated injection detection; relies on agent
instruction-following. Recommend adding automated content screening if agents
are granted broad web access.

### R4 — Hallucination with consequence
**Description:** An agent asserts a fact it did not verify (e.g., claims a
test passed, claims a security review was done) and another agent or human
acts on that assertion.
**Likelihood:** Medium — LLMs are non-deterministic and can confabulate.
**Impact:** Medium to High — could result in unreviewed code reaching production.
**Control:** Shared rule: agents must not claim validation they did not perform.
Output format requires Confidence field. Review gate requires independent
reviewer agent to validate implementer's claims. Hard cap of 3 review loops
before mandatory human escalation.
**Residual risk:** Low — multiple independent checks.

### R5 — Charter boundary violation
**Description:** An agent acts outside its defined charter scope, absorbing
responsibilities it is not governed to perform.
**Likelihood:** Low — charter isolation is enforced by role files and escalation rules.
**Impact:** Medium — could produce ungoverned output that bypasses review.
**Control:** Charter boundary rules in `boundaries.md`. Escalation triggers for
boundary crossings. Orchestrators cannot edit files. Handoff template required
for cross-charter work.
**Residual risk:** Low.

### R6 — Model non-determinism producing inconsistent governance
**Description:** The same governance instruction produces different agent
behaviour across sessions due to LLM non-determinism.
**Likelihood:** Medium — non-determinism is inherent to LLMs.
**Impact:** Low to Medium — governance rules may be interpreted differently.
**Control:** Temperature set low (0.1–0.2) for governance-sensitive agents
(orchestrators, reviewers, security reviewer). Explicit, unambiguous rule
language. Human review gate as final check.
**Residual risk:** Medium — acceptable given human review gate.

---

## Overall risk posture

| Risk | Residual level |
|------|---------------|
| R1 — Unintended file modification | Low |
| R2 — Irreversible action without approval | Low |
| R3 — Prompt injection | Medium |
| R4 — Hallucination with consequence | Low |
| R5 — Charter boundary violation | Low |
| R6 — Non-determinism | Medium |

**Overall residual risk: Low–Medium.** Appropriate for a development tooling
system where all changes pass through human review before production impact.
Not appropriate for systems with direct production write access or autonomous
deployment without human oversight.

---

## Limitations and mitigations not yet in place

| Gap | Status | Mitigation plan |
|-----|--------|----------------|
| No automated prompt injection detection | Open | Manual rule only; consider content screening if web access expands |
| No per-session action log | Open | Rely on git history and lessons.md for now |
| Non-determinism in governance interpretation | Accepted | Low temperature + human review gate |
| No formal repeatability testing | Open | Add to future governance review |

---

## Review and update guidance

Update this assessment when:
- A new agent is added or an existing agent's permissions change
- A new tool or external integration is granted to any agent
- An incident reveals an unidentified risk
- The operating environment changes (e.g., agents gain production access)
- Annual governance review is due

Last reviewed: `<replace: date>`
Reviewed by: `<replace: name and role>`
