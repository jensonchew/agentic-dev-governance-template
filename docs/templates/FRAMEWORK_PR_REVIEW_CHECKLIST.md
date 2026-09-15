# Framework PR Review Checklist

Use this checklist when reviewing framework-level changes.

## Scope

- Is this a framework change, not a repo-specific one?

## Portability

- Does it stay framework-agnostic?
- Does it avoid hidden stack assumptions?

## Value

- Does it improve reuse, clarity, or safety?

## Governance fit

- Does it match the charter split and repo conventions?
- Is it discoverable from `AGENTS.md` or `REPOSITORY-CONTEXT.md` if needed?

## Maintenance

- Is it lightweight enough to stay current?
- Does it need a checklist, skill, or doc pointer?

## Verification

- Are the relevant checks green?
- Is the PR small enough to review confidently?
