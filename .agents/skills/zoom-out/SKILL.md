---
name: zoom-out
description: Zoom out to a higher-level view of an unfamiliar area of the codebase. Maps relevant modules, call paths, and domain relationships so you understand how a piece fits into the bigger picture before making changes.
---

# Zoom Out

Use when you are unfamiliar with a section of the code, need to understand how it is called, or want a map of the surrounding domain before implementing or reviewing.

## When to use

- You are about to modify something and do not know its call graph or dependents
- You have been asked to review a change in an area you have not read before
- A spec references modules you haven't loaded yet
- You need to communicate the blast radius of a change to the orchestrator

## Workflow

1. **Identify the focal point**: the file, function, module, or concept the user named
2. **Trace upward**: find all direct callers or consumers of the focal point
3. **Trace outward**: find peer modules at the same abstraction layer
4. **Identify dependencies**: find what the focal point itself depends on
5. **Map domain vocabulary**: name each module using the project's own terminology (from `REPOSITORY-CONTEXT.md` or code comments), not generic names
6. **Summarize the shape**: one paragraph describing how the focal point fits into the wider system

## Output format

### Focal point
`<file or module path>` — one-line description of its responsibility

### Called by
- `<caller path>` — why it calls this, what it expects back

### Depends on
- `<dependency path>` — what is used and why

### Peers at same layer
- `<peer path>` — how it relates

### Domain map summary
A short paragraph (3–6 sentences) describing the focal point's role in the system using the project's own vocabulary. Name the bounded context, the abstraction layer, and any known invariants or constraints that affect how this area can be changed.

### Blast radius note
If changes to the focal point are being considered, briefly state what would break or need updating.

## Rules

- use the project's own names — do not rename or reframe modules
- load `REPOSITORY-CONTEXT.md` if available to confirm naming conventions
- if the focal point is not found, say so and suggest the closest match
- do not guess at responsibilities — read the code before describing it
- keep the map concise; omit transitive dependencies unless they are materially relevant
