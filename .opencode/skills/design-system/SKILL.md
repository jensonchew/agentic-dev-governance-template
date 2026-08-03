---
name: design-system
description: 'Use for UI design or UI review work that must follow the A*STAR web design scheme and promote consistent, reusable components.'
---

# Design System Skill

Use this skill when designing or reviewing web UI for this repository.

This skill defines the operational rules derived from the approved A*STAR
web design guide. Follow these rules unless the task explicitly states an
approved exception. :contentReference[oaicite:1]{index=1}

## Purpose

Use this skill to:
- keep UI work aligned to A*STAR brand rules
- promote consistent visual hierarchy
- reduce one-off UI treatments
- encourage reusable component-based design
- support practical implementation in product UIs

## Brand tone

The brand voice is:
- Passionate
- Inspiring
- Authentic

In UI terms:
- be clear, modern, and professional
- avoid clutter and visual gimmicks
- prefer confidence and clarity over decorative styling
- keep interactions direct and understandable :contentReference[oaicite:2]{index=2}

## Colour rules

### Core palette
- Primary blue: `#003087`
- Secondary red: `#DA291C`
- Secondary orange: `#FF6720`
- Secondary purple: `#5C068C`
- White: `#FFFFFF`
- Black: `#000000` :contentReference[oaicite:3]{index=3}

### Usage
- default to a blue-dominant palette
- use secondary colours as accents, highlights, or categorisation
- follow the blue:red:orange:purple ratio of `3:1:1:1` when multiple accent colours are needed
- prefer colour tints for hierarchy instead of introducing extra colours
- use RGB / HEX values for web work only
- prefer white text on dark brand backgrounds
- use black text only when necessary for readability :contentReference[oaicite:4]{index=4}

### Practical UI guidance
- primary CTA: blue by default
- destructive or urgent action: red where appropriate
- highlights or secondary emphasis: orange
- limited secondary accent or categorisation: purple
- avoid pages where all four brand colours compete equally
- avoid decorative colour use without semantic or structural purpose

## Typography rules

### Font stack
- Nunito: headings, titles, buttons, CTA
- Open Sans: body text, labels, captions
- M Plus Rounded 1c: Chinese text where needed :contentReference[oaicite:5]{index=5}

### Practical UI guidance
- page titles and section headings should use Nunito
- body content, labels, helper text, and captions should use Open Sans
- buttons and CTA labels should use Nunito and remain easy to scan
- keep body text in a readable range similar to 14–16px
- keep labels and captions in a readable range similar to 12–14px
- do not mix additional display fonts into the UI without approval :contentReference[oaicite:6]{index=6}

### A*STAR wordmark rule
- the `*` in `A*STAR` must be treated carefully and consistently
- do not substitute the branded logo or wordmark with improvised typography where official logo treatment is required :contentReference[oaicite:7]{index=7}

## Logo and brand element rules

- use the full-colour logo on light backgrounds
- use reversed white logo on dark or coloured backgrounds
- use the logomark only for compact spaces such as favicons or avatars
- do not distort, recolour, rotate, add shadows, or restyle the logo
- preserve required clear space around the logo
- do not place the logo on visually busy backgrounds without sufficient contrast :contentReference[oaicite:8]{index=8}

## Layout and visual hierarchy

### Blue bar
- the blue bar is a core brand element for headers or footers
- use it consistently, not decoratively
- use the tagline only where the design explicitly calls for it
- do not overload content-heavy screens with oversized brand bars :contentReference[oaicite:9]{index=9}

### Colour blocking
- use colour blocks to organise information and priority
- hierarchy should generally follow: blue, then red, then orange, then purple
- use tint variation to separate sections or emphasis lightly :contentReference[oaicite:10]{index=10}

### Watermark / star icon
- use only as a subtle supporting element
- keep it low emphasis
- do not rotate it
- do not place text or busy content over it :contentReference[oaicite:11]{index=11}

## Component design guidance

Design for reuse:
- prefer shared buttons, cards, forms, banners, tables, filters, tabs, dialogs, and status panels
- avoid screen-specific variants when a shared component pattern would work
- prefer a small set of repeatable spacing, heading, and action patterns
- keep interaction patterns consistent across pages

When proposing new UI:
- identify whether an existing reusable component can be extended
- create a new reusable component only when reuse is likely
- avoid visually different solutions for the same interaction type

## UX guidance

Design and review should favour:
- clear task flow
- low cognitive load
- visible hierarchy
- obvious primary action
- explicit status and feedback
- consistent validation and error handling
- responsive practicality
- accessibility basics

Always think through these states where relevant:
- default
- hover / focus
- active / selected
- disabled
- loading
- empty
- error
- success
- validation feedback

## Icons and illustration

- prefer flat, outlined icon styles
- keep icon line weights consistent
- avoid 3D, glossy, or ornamental icon styles
- use icons to support comprehension, not decoration alone :contentReference[oaicite:12]{index=12}

## Do not

- do not invent an unrelated visual language
- do not overuse accent colours
- do not create one-off components when a reusable one is feasible
- do not add decorative effects that weaken the corporate look
- do not use inconsistent typography roles
- do not restyle protected brand assets
- do not choose novelty over consistency

## Output expectation for design work

When using this skill, outputs should usually identify:
- the reusable components involved
- the intended hierarchy
- the states that must exist
- any brand constraints affecting implementation
- any places where the design system may need explicit extension
