# Boundaries and Handoffs

## Boundary rule

Charters are specialized and must remain bounded.

- Development must not silently decide production hosting strategy
- Delivery must not silently rewrite application logic
- One charter may recommend work for another, but must not absorb that work unless explicitly authorized

When work crosses a charter boundary:
- Escalate to the relevant orchestrator
- Use the handoff template at `docs/templates/HANDOFF.md`
- Keep recommendations separate from approved execution

---

## Charter loading rule

Charters are not implicitly loaded.

Agents must:
- Determine the correct charter based on task intent
- Explicitly load the corresponding charter

Agents must not:
- Mix rules from multiple charters
- Assume development rules apply to delivery evaluation
- Assume delivery constraints apply to implementation flow

---

## Handoff rule

Cross-charter collaboration must be explicit.

When one charter hands work to another, use the canonical handoff template at
`docs/templates/HANDOFF.md`.

The handoff must identify:
- Objective
- Current state
- Relevant context and constraints
- Assumptions
- Unresolved risks
- What the handoff does not claim
- Requested decision or output

Do not rely on implicit intent transfer between charters.
