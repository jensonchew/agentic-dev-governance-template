# Framework alignment note — 14 November 2026

**Who this is for**

- **People forking this template:** why two rules were added, and which public documents they track.
- **Agents editing governance:** load this when a task is about oversight, tools, or permissions. Do not paste it into role files.
- **This is not** a certification, a legal opinion, or a runtime audit log.

The rules themselves stay in [`.agents/governance/shared-rules.md`](../../.agents/governance/shared-rules.md) and [`human-oversight-model.md`](./human-oversight-model.md). They do not name a statute, so they keep working when a framework is revised.

## What changed in this template

1. Higher-risk limits are enforced in permissions, role files, or tool registration. A prompt that says not to take the action is a backstop.
2. Granting a new tool, MCP server, fetch permission, model, or charter change reopens [`safety-assessment.md`](./safety-assessment.md) before the grant.

Session audit, circuit breakers, and ingest gates stay out. This repository has no assistant runtime. That limitation was accepted on 29 September 2026. See the decisions log.

## Why these two rules, and not a rewrite

| Source | Date | What this template takes from it |
|--------|------|----------------------------------|
| [IMDA MGF for Agentic AI v1.5](https://www.imda.gov.sg/assets/63438074-73f6-4dcc-a281-030f42642cf4.pdf) | Published 20 May 2026, updated 5 June 2026 | Prefer structural controls over prompt text for higher-risk actions. Re-open the risk note when tools, permissions, or the agent roster change. Third-party tools need a conscious grant. |
| [CSA addendum on securing agentic AI](https://www.csa.gov.sg/resources/publications/addendum-on-securing-ai-systems/) | 17 June 2026 | A coding assistant is one of the worked examples: judge autonomy, threat-model the workflow, keep identity and tool use limited. Voluntary cybersecurity guidance. |
| [MDDI, 6 October 2026](https://openhansard.sg/reports/written-answer-na-25101) | 6 Oct 2026 | Instructions alone are not a sufficient limit. Bound what the agent can access and do. |
| [IMDA agentic testing starter kit](https://www.imda.gov.sg/assets/603572eb-724a-46cf-ac12-14fe38e1558c.pdf) | October 2026 | Testing guidance for organisations that run agents. This template does not ship a test harness. Do not claim the kit was applied here. |
| [EU AI Act timeline](https://ai-act-service-desk.ec.europa.eu/en/ai-act/eu-ai-act-implementation-timeline) | Transparency from 2 Aug 2026; high-risk Annex III from 2 Dec 2027 | This template is not a product placed on the EU market. No conformity file. |
| [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) | AI RMF 1.0 and the July 2024 Generative AI Profile remain the stable texts | 2026 Cyber AI Profile and critical-infrastructure profile are drafts. Do not treat them as requirements. |

Singapore’s ministerial line through July and August 2026 is still case by case. The agentic framework is guidance. Existing law and sector guidelines come first. This template does not add a “high-risk” label.

## What not to write in a fork

- “Compliant with IMDA, CSA, AI Verify, NIST, or the EU AI Act.”
- A session JSONL logger copied in to look like a product audit.
- News about breaches or vendor investigations as if this repository were involved. Those belong in the product repo that operates an assistant, dated and sourced, not in this starter.

## Review

Update this note when a primary source above is replaced by a new version, or when a shared rule changes for a reason that is not already in `.agents/memory/decisions.md`.

Last reviewed: 2026-11-14.
