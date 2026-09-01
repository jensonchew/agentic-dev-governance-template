---
name: setup
description: >
  Initialize or reconfigure the agent system for a specific tech stack.
  Generates stack-specific engineering rules, repository context, and
  agent permission configurations from a user-provided stack description.
  Use when setting up a new repository, changing the tech stack, or
  onboarding agents to an existing codebase.
---

# Repository Setup

Configure the agent system for your specific tech stack and repository.

## What this skill does

1. Collects information about your repository's tech stack
2. Generates `REPOSITORY-CONTEXT.md` with correct paths, commands, and conventions
3. Generates `.agents/instructions-stack.md` with language and framework-specific engineering rules
4. Identifies which agent bash permissions need updating for your build tools
5. Identifies which skill packs are relevant to your stack

## How to use

The user can invoke this skill in two ways:

### Descriptive mode
The user provides a natural language description of their stack:
```
/setup We have a Go backend with Chi router, React frontend with Vite,
PostgreSQL with sqlc, and Jest for testing
```

### Interactive mode
The user invokes with no arguments or minimal context:
```
/setup
```
In this case, walk through the interview questions below.

Start with one short routing question before the detailed interview:

**What kind of stack are we setting up?**

1. Frontend-led
   - React + TypeScript
   - React + Python
   - React + Go
   - Angular + TypeScript
2. Enterprise .NET
   - .NET + Angular
   - .NET + .NET frontend or no frontend
3. Custom / other

Then continue with a short, natural conversation tailored to the chosen family.

## Interview questions

When information is missing, ask these questions. Group related questions
to minimize back-and-forth. Do not ask about things the user already stated.

### Core stack (required)
1. **Backend**: What language and framework are you using? (e.g., C# + ASP.NET, Go + Chi, Python + FastAPI, Java + Spring Boot, Node + Express, TypeScript + NestJS, Rust + Actix)
2. **Frontend**: If there is one, what framework are you using? (e.g., Angular, React, Vue, Svelte, Next.js, none)
3. **Repository type**: Is this a monorepo or separate repos?

### Suggested stack choices

Offer a small number of common choices first, then allow custom input:

- React frontend + TypeScript backend
- React frontend + Python backend
- React frontend + Go backend
- Angular frontend + TypeScript backend
- TypeScript-only app or service
- .NET backend + Angular frontend (custom enterprise option)
- .NET backend + .NET frontend toolchain or no frontend (fallback enterprise option)

If none of the above fit, ask the user to describe their stack in their own words.

### Family-specific follow-ups

- If the user picks a React-based family, ask briefly about routing, state, and styling.
- If the user picks a TypeScript-only app or service, ask whether it is backend-only, frontend-only, or shared library code.
- If the user picks a .NET enterprise option, ask whether Angular is required or whether the fallback .NET frontend/no-frontend path is preferred.
- If the user picks Custom / other, ask only the missing questions needed to define the stack clearly.

### Tone

- Keep the conversation short and practical
- Ask one grouped question at a time
- Do not force users through questions they already answered
- Use examples to guide, not to constrain

### Architecture (required)
4. **Backend structure**: How are backend projects/modules organized? (e.g., layered Api/Application/Core/Infrastructure, hexagonal, feature-folders, flat)
5. **Frontend structure**: How is the frontend organized? (e.g., feature-level folders, pages router, app router, nx workspace)

### Data (ask if not stated)
6. **Database**: What database and access layer? (e.g., PostgreSQL + EF Core, MySQL + Prisma, MongoDB + Mongoose, PostgreSQL + sqlc)
7. **Migrations**: How are schema changes managed? (e.g., EF migrations, Flyway, Alembic, Prisma migrate, raw SQL)

### Testing (ask if not stated)
8. **Backend testing**: What test framework and tools? (e.g., xUnit + Moq, pytest, Go testing, JUnit + Mockito)
9. **Frontend testing**: What test framework? (e.g., Jest, Vitest, Karma, Playwright for e2e)
10. **Integration testing**: Any container-based testing? (e.g., Testcontainers, docker-compose test)

### Build and tooling (ask if not stated)
11. **Package manager**: What package manager for frontend? (e.g., npm, yarn, pnpm, bun)
12. **Build commands**: What are the main build/test/lint commands?
13. **Local run**: How do you run the stack locally?

### Optional context
14. **Messaging/background jobs**: Any message queues or job systems?
15. **External integrations**: Critical external services?
16. **Known issues**: Any baseline issues agents should know about?

## Generation rules

After collecting information, generate the following files:

### 1. REPOSITORY-CONTEXT.md

Fill in all template sections with the user's actual values. For any section
the user did not provide information, leave the placeholder with a note:
`<not yet configured — run /setup to update>`

Pay special attention to:
- **Agent bash permissions** section: generate the correct command patterns for the user's build tools
- **Canonical commands**: use the actual commands, not placeholders
- **Architecture notes**: describe what's actually in the repo, not aspirational state

### 2. .agents/instructions-stack.md

Generate stack-specific engineering rules. This file supplements the universal
rules in `instructions.md`.

Structure:
```markdown
# Stack-Specific Engineering Rules

Generated by `/setup` on <date>.
Stack: <backend> + <frontend>

## Backend rules
<language-specific coding rules>

## Frontend rules
<framework-specific coding rules>

## Persistence rules
<database and ORM specific rules>

## Testing rules
<stack-specific testing expectations>

## Build and validation
<stack-specific build expectations>
```

Use these reference patterns for common stacks:

#### C# / .NET
- nullable reference types respected
- async/await throughout, no sync-over-async (.Result, .Wait())
- record types for DTOs and value objects where existing pattern uses them
- file-scoped namespaces when repository uses them
- preserve existing namespace conventions

#### Go
- follow existing package structure
- error handling: check and return errors, do not panic in library code
- use context.Context for cancellation and deadlines
- prefer table-driven tests
- respect existing linting rules (golangci-lint config)

#### Python
- type hints on all public function signatures
- follow existing code style (black, ruff, or project formatter)
- use existing async patterns (asyncio, sync) consistently
- virtual environment and dependency management per project convention

#### Java / Kotlin
- follow existing code style and formatting
- preserve existing dependency injection patterns
- respect existing exception handling conventions
- follow existing package naming and structure

#### TypeScript / JavaScript (backend)
- preserve strict mode and TypeScript strictness settings
- follow existing patterns for error handling
- respect existing module system (ESM vs CJS)

#### TypeScript / JavaScript (frontend)
- preserve existing frontend framework conventions for TypeScript usage
- keep framework-specific behavior in the relevant framework section (Angular, React, Vue, etc.)
- respect existing lint, typecheck, and build commands for the frontend toolchain

#### Angular
- preserve existing workspace structure and conventions
- prefer feature-level organization
- prefer standalone components when existing patterns use them
- keep business rules out of presentation components
- preserve existing routing, form, HTTP, and signals patterns

#### React
- follow existing component patterns (functional components, hooks)
- preserve existing state management approach (Redux, Zustand, Context, etc.)
- respect existing routing patterns (React Router, Next.js, etc.)
- follow existing styling approach (CSS modules, Tailwind, styled-components, etc.)

#### Vue
- follow existing composition API or options API patterns
- preserve existing state management (Pinia, Vuex)
- respect existing routing patterns
- follow existing component structure (SFC, script setup)

### 3. Agent permission updates

After generating the files, identify which agent role files need their
bash permission patterns updated. List the changes needed but do not
modify agent files directly — present them to the user for approval.

Common patterns:
- Context Mapper: replace `dotnet build*` with stack build command
- design-analyst: replace `dotnet build*` with stack build command
- Reviewer: replace `dotnet build*`, `dotnet test*`, `ng build*`, `ng test*`, `yarn*` with stack equivalents
- Implementer: already has `"*": allow`, no change needed

## Validation checklist

Before presenting the generated files, verify:
- [ ] All canonical commands are real commands, not placeholders
- [ ] Architecture description matches user's actual structure
- [ ] Agent bash permissions match the actual build/test tools
- [ ] Package manager is correct
- [ ] No hardcoded .NET/Angular assumptions remain unless that's the actual stack
- [ ] instructions-stack.md rules are specific to the stated stack, not generic
- [ ] REPOSITORY-CONTEXT.md agent tooling section is preserved

## After generation

Tell the user:
1. Review the generated files
2. Approve the agent permission changes
3. If code-memory-mcp is available, run `stats` to verify the memory tier recognizes the repo
4. Run `/setup` again any time the stack changes materially
