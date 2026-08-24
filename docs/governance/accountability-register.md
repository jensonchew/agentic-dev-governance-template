# Accountability Register

Aligned with: IMDA MGF for Agentic AI — Accountability dimension; AI Verify Principle 9.

This register names the human accountable owner for each charter and agent scope.
Update this file when ownership changes. An external auditor should be able to reach
the named owner for any AI-related incident or compliance question.

---

## How to use this register

- **Accountable owner**: The named human ultimately responsible for decisions and
  outcomes within this scope. This person can be contacted if an agent causes harm,
  acts outside its charter, or triggers an incident.
- **Operating team**: The team that manages day-to-day agent operations within this scope.
- **Review cadence**: How often the charter's governance and permissions are reviewed.

---

## Development Charter

| Field | Value |
|-------|-------|
| Accountable owner | `<replace: name and role, e.g. "Lead Engineer — Jane Doe">` |
| Contact | `<replace: email or channel>` |
| Operating team | `<replace: e.g. "Software Engineering Team">` |
| Scope | Specification, implementation, code review, security review, migration planning, UI design |
| Agents covered | development-orchestrator, spec-writer, implementer, reviewer, security-reviewer, design-analyst, architecture-challenger, migration-planner, ui-designer, ui-reviewer, context-mapper, docs-updater |
| Review cadence | `<replace: e.g. "Quarterly">` |
| Last reviewed | `<replace: date>` |

---

## Delivery Charter

| Field | Value |
|-------|-------|
| Accountable owner | `<replace: name and role, e.g. "Platform Lead — John Smith">` |
| Contact | `<replace: email or channel>` |
| Operating team | `<replace: e.g. "Platform / DevOps Team">` |
| Scope | CI/CD pipeline review, platform evaluation, delivery-path security, observability, cost assessment |
| Agents covered | delivery-orchestrator, pipeline-engineer, platform-evaluator, devsecops-reviewer, observability-engineer |
| Review cadence | `<replace: e.g. "Quarterly">` |
| Last reviewed | `<replace: date>` |

---

## Overall AI Governance Owner

The person responsible for ensuring this register is maintained, incidents are
reported, and the governance framework remains current.

| Field | Value |
|-------|-------|
| AI Governance owner | `<replace: name and role>` |
| Contact | `<replace: email or channel>` |
| Escalation path | `<replace: e.g. "Engineering Director → CTO">` |
| Framework reference | IMDA MGF for Agentic AI; AI Verify Testing Framework (Principle 9 — Accountability) |

---

## Accountability chain for multi-agent actions

When agents chain together (orchestrator → specialist → tool execution), accountability
flows as follows:

1. **Orchestrator** is accountable for the decision to invoke a specialist
2. **Specialist** is accountable for the output it produces
3. **Human reviewer** (where required by the human oversight model) is accountable
   for approving any irreversible or high-risk action
4. **Charter accountable owner** is ultimately accountable for all agent actions
   within their charter scope

No agent action removes human accountability. The agent acted; a human is still
responsible for the governance that permitted it.

---

## Review and update guidance

Update this register when:
- Ownership changes (staff movement, reorg)
- New agents are added to either charter
- A new charter is created
- An incident reveals an accountability gap
- Annual review is due
