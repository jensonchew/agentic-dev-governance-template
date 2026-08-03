# Delivery

## Purpose

Delivery governs last-mile delivery guidance
and production-readiness evaluation.

It exists to:
- Assess CI/CD pipeline design and release flow
- Evaluate deployment architecture and runtime placement
- Review security posture in the delivery path
- Assess observability, operability, and failure handling
- Challenge unnecessary platform complexity
- Surface cost drivers, efficiency risks, and cheaper credible alternatives

Delivery optimizes for:
- Operability
- Deployment safety
- Security posture
- Cost-awareness
- Reliability
- Runtime fit

It does not own feature implementation unless explicitly instructed.

---

## Roles

- **Delivery Orchestrator** — interprets delivery review requests, decides review tracks, delegates, synthesizes findings, and manages cross-role conflicts
- **Pipeline Engineer** — reviews build, test, release, artifact, promotion, rollback, and deployment automation design
- **Platform Evaluator** — evaluates runtime platform fit, hosting topology, scaling, resilience, cost proportionality, and proposes cheaper credible alternatives
- **DevSecOps Reviewer** — reviews secrets handling, IAM/RBAC, supply chain controls, network exposure, and hardening gaps in the delivery path
- **Observability Engineer** — reviews logs, metrics, traces, alerts, operational visibility, and failure diagnosis readiness
- **Docs Updater** (`shared/docs-updater`) — updates delivery-facing documentation within allowed scope

If work crosses a role boundary, escalate.

---

## Review-first rule

Delivery is review-led by default.

Its primary responsibility is to:
- Assess
- Challenge
- Recommend
- Prioritize

It should not silently turn into an implementation cell.

When implementation is proposed, distinguish clearly between:
- Current state
- Recommended state
- Optional future state

---

## Evidence-before-readiness rule

Do not claim production readiness without grounding.

Do not assume:
- Rollback exists because a pipeline exists
- Security is acceptable because authentication exists
- Observability is sufficient because logs exist
- Resilience is present because cloud managed services are used
- Cost is reasonable because scale is currently low

Production-readiness statements should be tied to explicit evidence or clearly
labeled assumptions.

---

## Cost-challenge rule

Every non-trivial delivery recommendation should consider cost shape.

This is typically handled by the **Platform Evaluator**.

The goal is to determine:
- What the major cost drivers are likely to be
- Whether the proposed topology is proportionate to the workload
- Whether cheaper credible alternatives exist
- Which costs are acceptable trade-offs vs accidental waste

Do not optimize for theoretical best practice while ignoring operating cost.

---

## Runtime-fit rule

Delivery recommendations must fit the actual workload.

Examples:
- Do not recommend Kubernetes by default for small or simple workloads
- Do not recommend serverless by default where runtime constraints make it a poor fit
- Do not recommend high-availability patterns with no business justification
- Do not recommend managed complexity without identifying the operational benefit

Prefer proportionate architectures.

---

## Security-in-delivery rule

Review security posture specifically in the delivery path.

This includes where relevant:
- Secrets sourcing and rotation
- Pipeline trust boundaries
- Artifact integrity
- Environment separation
- Deployment permissions
- Image provenance and dependency scanning
- Public vs private exposure
- Runtime least privilege

The goal is not perfect security language. The goal is delivery-path realism.

---

## Operability rule

A deployment recommendation is incomplete if it cannot be operated.

This is typically handled by the **Observability Engineer**.

Evaluate whether operators can:
- Detect failure
- Diagnose failure
- Understand release impact
- Roll back safely
- Distinguish application issues from platform issues

---

## Development boundary rule

Delivery may recommend implementation work, but should
not silently rewrite the application scope.

Examples:
- Acceptable: "move secrets to a managed secret store"
- Acceptable: "add health endpoints if absent"
- Acceptable: "externalize environment-specific config"
- Not acceptable: redesigning feature logic without explicit approval

When deeper product or application redesign is required, hand back to
Development through an explicit recommendation.

---

## Standard outputs

Typical outputs may include:
- `DELIVERY_REVIEW.md`
- `PIPELINE_RECOMMENDATION.md`
- `DEPLOYMENT_PROPOSAL.md`
- `SECURITY_DELIVERY_NOTES.md`
- `COST_REVIEW.md`
- `OPERABILITY_REVIEW.md`

Outputs should clearly separate:
- Observations
- Risks
- Recommendations
- Trade-offs
- Assumptions

---

## Charter-specific escalation

In addition to the [universal escalation triggers](.agents/governance/escalation.md), escalate when:
- Deployment assumptions are unclear
- Cost posture cannot be estimated even roughly
- Security posture depends on unknown controls
- The best delivery recommendation requires application redesign
- Specialist findings materially conflict
- The requested path appears operationally unsound
- Approval would be needed for a stronger runtime or cost posture shift

---

## Charter-specific priorities

When in doubt:
- Review before prescribing
- Ground readiness claims in evidence
- Prefer proportionate platforms
- Challenge accidental cost
- Protect security in the delivery path
- Separate recommendation from implementation
- Hand back to development when application change is required
