# Just-in-time context loading

Agents load context on demand rather than pre-loading all governance, charters, and instruction files upfront. Only `AGENTS.md` (74 lines) is globally auto-loaded. Everything else is pulled in by the agent when its current task requires it.

## Considered Options

- **Eager bulk loading** (original): every agent pre-loads AGENTS.md + both charters + full instructions + all governance files (~600+ lines before task). Rejected because LLMs demonstrably skip long preambles under context pressure, wasting tokens and reducing governance adherence.
- **Per-agent hardcoded reading lists** ("Read first: 1, 2, 3..."): agents load a fixed set regardless of task. Rejected because a reviewer doesn't need migration rules, an implementer doesn't need escalation triggers, and orchestrators don't need all sub-files simultaneously.
- **Just-in-time loading** (chosen): minimal global context + conditional loading guided by "Always" / "On demand" sections in each role file + phase-triggered sub-file loading in orchestrators.

## Consequences

- Agents see less irrelevant context, improving adherence to what IS loaded.
- Token cost is reduced — especially for simple tasks that don't need governance deep-dives.
- Role files must explicitly state WHEN to load each dependency, not just WHAT exists. This is enforced by the "Context loading" section pattern.
- If an agent fails to load a needed file, it may miss a rule. Mitigation: the "Always" tier ensures minimum viable context; governance blockquote in each role file reminds of core rules.
- New role files must follow the "Always / On demand" pattern rather than listing everything upfront.
