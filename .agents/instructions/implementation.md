# Implementation Rules

## Scope control

Implementers must:
- modify only approved files and scope
- keep changes small and reviewable
- avoid unrelated cleanup, renames, or refactors
- justify any new dependency or major pattern change

Do not:
- redefine requirements
- change public contracts unless explicitly required
- mix feature work with unrelated maintenance

## Language and framework rules

Follow the language-specific and framework-specific rules defined in:
1. `.agents/instructions-stack.md` (if it exists)
2. `REPOSITORY-CONTEXT.md` stack conventions section

If neither file defines rules for the relevant language or framework,
follow the existing patterns visible in the repository and escalate
when conventions are unclear.

## Package manager discipline

Use the package manager defined in `REPOSITORY-CONTEXT.md`.
Do not introduce alternative package managers, lockfiles, or workflow
guidance unless the user explicitly changes the repository standard.
