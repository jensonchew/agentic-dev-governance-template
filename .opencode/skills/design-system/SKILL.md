---
name: design-system
description: Use for UI design or UI review when the repo has an organization design system. Replace this file with your own tokens and rules.
---

# Design System Skill (template)

Use this skill when designing or reviewing web UI in a repository that defines
an organization design system.

**This file is a placeholder.** After forking, replace it with your org's
approved design tokens, typography, colour palette, and component rules—or
delete it and point `ui-designer` / `ui-reviewer` at another skill.

## Purpose

- keep UI work aligned to documented design rules
- promote consistent visual hierarchy
- reduce one-off UI treatments
- encourage reusable component-based design

## What to document in your replacement

When you customize this skill, include:

1. **Brand tone** — voice and visual personality (professional, minimal, etc.)
2. **Colour palette** — primary, secondary, semantic (success, error), contrast rules
3. **Typography** — font stacks for headings, body, and UI labels
4. **Logo / wordmark** — usage constraints (do not invent rules; link to official brand guide)
5. **Layout patterns** — headers, spacing scale, grid
6. **Components** — buttons, forms, tables, dialogs, states (loading, empty, error)
7. **Accessibility** — focus, contrast, keyboard flows

## UX guidance

Design and review should favour:

- clear task flow and visible hierarchy
- obvious primary action
- explicit status and feedback
- consistent validation and error handling
- responsive practicality

## Do not

- invent an unrelated visual language without org approval
- overuse accent colours
- create one-off components when a reusable one is feasible
- restyle protected brand assets without authority

## Output expectation

When using this skill, outputs should usually identify:

- reusable components involved
- intended hierarchy and required states
- brand constraints affecting implementation
- any places where the design system needs explicit extension
