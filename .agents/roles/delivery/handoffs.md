# Delivery Orchestrator — Handoffs and Synthesis

## Context handoff

Provide:
- track name
- objective
- delivery concern being addressed
- likely affected area
- known boundaries or exclusions
- specific questions to answer

## Specialist handoff

Provide:
- track name
- objective
- delivery concern being addressed
- affected area
- context map, if available
- known boundaries or exclusions
- specific risks, assumptions, or questions to evaluate
- development handoff, if available

## Output contract

For each specialist, expect output that clearly identifies:
- current state
- assumptions
- findings
- risks
- recommendations
- confidence
- implications for cost, complexity, security, or operability where relevant

Do not accept vague approval language.

## Handoff from Development

When the request comes from a development handoff, expect some or all of:
- system summary
- current architecture
- intended deployment assumptions
- known shortcuts or deferred work
- explicit constraints
- open questions for delivery review

If the handoff is incomplete, narrow the review or gather missing context before proceeding.

## Synthesis rules

When combining specialist outputs:
- remove duplicates
- separate facts from recommendations
- rank issues by practical impact
- make trade-offs explicit
- avoid turning every concern into a blocker
- identify what is required now vs what is future improvement

Where specialists disagree:
- identify the source of disagreement
- explain the trade-off clearly
- escalate when the decision requires user input or business prioritization

## Handoff to Development

When delivery review surfaces follow-on implementation work, hand back to Development with:

- **Summary**: what delivery review found that requires development action
- **Trigger**: what specific finding or recommendation requires a development response
- **Affected area**: which components, services, or layers are implicated
- **Constraints identified**: any delivery-path constraints (e.g., deployment topology, secret handling, platform limits) the implementer must respect
- **Recommended next step**: suggested Development phase to enter (e.g., design analysis, migration planning, implementation)
- **Open questions**: what the Delivery review could not resolve that Development must answer

Do not recommend implementation specifics. Delivery defines what must change and why; Development decides how.
