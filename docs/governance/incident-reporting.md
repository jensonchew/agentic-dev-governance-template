# Incident Reporting

Aligned with: IMDA MGF for Agentic AI — Incident Reporting dimension; AI Verify Principle 4 (Safety).

This document defines what constitutes an AI incident in the context of this
agentic development system, how to report it, and how to learn from it.

---

## What is an AI incident?

An AI incident is any event where an agent:

- Took an action outside its approved scope (charter boundary violation)
- Produced output that caused harm — to code, data, systems, or people
- Executed an irreversible action without explicit human approval
- Appeared to be influenced by prompt injection (content in tool results redirected its behaviour)
- Bypassed a required review or approval step
- Made a claim it did not verify (hallucination with consequence)
- Caused a security exposure (leaked secrets, exposed credentials, opened unintended access)
- Failed in a way that was not caught by existing guardrails

Near-misses — events where harm was averted but the guardrail was the only thing
that stopped it — should also be reported. Near-misses are as valuable as incidents
for improving governance.

---

## Severity tiers

| Tier | Description | Examples |
|------|-------------|---------|
| **P1 — Critical** | Irreversible harm, security exposure, or production impact | Agent pushed to production without approval; secrets committed; data deleted |
| **P2 — High** | Recoverable harm or significant charter violation | Agent merged without review; wrong branch targeted; scope silently expanded |
| **P3 — Medium** | Governance breach without immediate harm | Agent claimed validation it did not perform; output-format rules not followed |
| **P4 — Low / Near-miss** | No harm but guardrail was stressed | Escalation trigger fired correctly; injection attempt detected and stopped |

---

## How to report an incident

### Immediate response (P1/P2)

1. **Stop** — interrupt the agent session immediately
2. **Contain** — revert any harmful changes (`git revert`, restore from backup)
3. **Notify** — contact the charter accountable owner named in `docs/governance/accountability-register.md`
4. **Preserve** — save the session transcript and any relevant logs before clearing

### All incidents

Record the incident in `.agents/memory/lessons.md` using this format:

```
## <date> — <short title>

**Severity:** P1 / P2 / P3 / P4
**What happened:** Factual description of what the agent did.
**Impact:** What harm occurred or was narrowly avoided.
**Root cause:** Which governance rule was absent, unclear, or bypassed.
**Remediation:** What was done to contain or reverse the harm.
**Governance fix:** What rule, permission, or process was updated as a result.
**Applies to:** Which agents or scenarios this lesson applies to.
```

---

## Reporting to external bodies

If the incident involves:
- **Personal data** — report per PDPA obligations (Singapore) within 3 business days if it is a notifiable data breach
- **Material business impact** — escalate per your organisation's existing incident management process
- **Regulatory AI systems** — follow sector-specific reporting requirements (MAS, MOH, etc.)

For guidance on whether an incident is notifiable, consult the PDPC's breach assessment tool at pdpc.gov.sg.

---

## Post-incident review

For P1 and P2 incidents, conduct a post-incident review within 5 business days:

1. **Timeline** — reconstruct exactly what the agent did and when
2. **Root cause** — identify which governance control failed or was absent
3. **Governance update** — update the relevant rule file, permission, or process
4. **Lessons entry** — record in `.agents/memory/lessons.md`
5. **Register review** — check whether the accountability register needs updating

The goal is not blame but improvement. Every incident is evidence that the governance
model needs strengthening.

---

## Continuous improvement

Review this document and the lessons log at least quarterly. Patterns in P3/P4
incidents often predict P1/P2 incidents before they happen.
