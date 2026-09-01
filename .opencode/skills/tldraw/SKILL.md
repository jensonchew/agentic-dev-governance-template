---
name: tldraw
description: Use for visual brainstorming, system mapping, workflow sketches, and collaborative whiteboarding. Best when a problem benefits from spatial exploration or quick diagramming before code or docs are finalized.
---

# Tldraw

Use Tldraw when a task benefits from drawing ideas out before committing to a text artifact.

## Best fit

- Early-stage product or architecture exploration
- System boundary sketches
- User journey and workflow mapping
- Component relationship diagrams
- Collaborative workshop notes

## Use it when

- The user wants to explore multiple options visually
- The structure is easier to reason about spatially than in prose
- You need a low-friction artifact for shared discussion
- A diagram may evolve before it becomes documentation

## Avoid it when

- The output needs to live primarily in markdown docs
- The diagram must be syntax-checkable in source control
- The task is mostly a structured, textual explanation
- The repository does not have a workflow for storing Tldraw artifacts

## Workflow

1. Start with the smallest useful sketch.
2. Label only the important entities, flows, or boundaries.
3. Keep the layout simple enough to revisit later.
4. Convert the result into markdown, Mermaid, or repo notes if the artifact needs to be durable.

## Good practices

- Prefer clarity over completeness
- Use visual grouping to separate concerns
- Keep annotations short
- Treat the drawing as an intermediate design artifact unless the user explicitly wants it as the final deliverable

## Cross-repo use

- Keep this skill repo-agnostic
- Do not assume a specific frontend stack or diagram storage convention
- If a target repo has its own design-doc process, adapt the final artifact to that repo's format
