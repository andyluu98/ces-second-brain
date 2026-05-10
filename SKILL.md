---
name: ces-second-brain
description: "Operate any Obsidian vault as a living, self-rewriting second brain. Use whenever the user asks Claude to read, write, update, search, or manage their Obsidian vault — save notes from conversation, create daily entries, update kanban boards, log dev work, manage people notes, capture decisions, track deals, or maintain any vault structure. Also triggers when the user bootstraps a new vault, runs a vault health check, or generates a _CLAUDE.md operating manual so all Claude surfaces share the same vault rules. Use proactively whenever the conversation produces vault-worthy info — decisions made, people met, projects started, tasks completed, lessons learned. Skill responds to the user in Vietnamese and writes vault notes in Vietnamese by default."
license: MIT
---

# ces second brain

> Claude operates your Obsidian vault as a self-rewriting knowledge base. Sources rewrite existing pages instead of just appending, and contradictions reconcile when found.
> Everything worth remembering gets saved. Every update propagates everywhere it belongs.

## Vietnamese mode (default)

Respond to the user in **Vietnamese**. Write all vault notes in **Vietnamese** (heading, body, summary). Tag values use Vietnamese without diacritics, kebab-case (e.g. `quyet-dinh`, `du-an`, `nguoi`, `y-tuong`). Preamble uses `## Cho Claude tương lai` instead of `## For future Claude`. Recency markers in Vietnamese: `(tính đến 2026-05, source.com)`. Keep frontmatter keys (`date`, `tags`, `type`, `ai-first`, `status`, `timeline`), `[[wikilink]]` targets that already exist, source URLs verbatim, command names (`/obsidian-save`), and code blocks unchanged.

---

## Output model

The skill produces **markdown notes in chat**. The user copies them into their Obsidian vault, or pastes paths back if they want updates. The skill does not auto-write files unless filesystem tools are available in the host environment (Claude Code, Claude Desktop with filesystem MCP). Behave gracefully either way.

When filesystem access is available, follow the original "never create in isolation" rule and propagate updates. When not available, output every note as a fenced markdown block with a clear filename header so the user can save it manually.

---

## Quick start

### First time talking to a user with a vault

1. Ask the user where their vault root is, or what folder structure they use, if not stated.
2. If they have a `_CLAUDE.md` at vault root and they paste it, follow its rules exactly — they override the defaults below.
3. If no vault exists yet, offer the bootstrap flow (Section "Bootstrap a new vault" below).

### Bootstrap a new vault (no scripts required)

When the user wants a fresh vault, generate the folder structure and starter files as a tree of markdown blocks the user can paste in. Ask 3 questions first:

1. Tên của bạn? (xuất hiện trong _CLAUDE.md)
2. Bạn muốn dùng vault để làm gì chính? executive (lãnh đạo) / builder (lập trình) / creator (sáng tạo) / researcher (nghiên cứu) / general (đa năng)
3. Cấu trúc vault? wiki-style (LLM-first) hoặc obsidian-style (duyệt thủ công)

Then output: `_CLAUDE.md`, `index.md`, `log.md`, `SOUL.md` (skeleton), `CRITICAL_FACTS.md` (skeleton), and the chosen folder skeleton. User creates folders + pastes files into Obsidian.

See `references/claude-md-template.md` for the `_CLAUDE.md` template and `references/vault-schema.md` for the full folder + frontmatter schema per preset.

---

## Core operating principles

### AI-first vault rule (applies to every note)

Every note Claude writes — across all 26 commands — must follow `references/ai-first-rules.md`:

1. **Self-contained context** — each note explains itself; don't rely on backlinks alone
2. **`## Cho Claude tương lai` preamble** — 2-3 sentence summary so Claude can decide relevance in 10 seconds
3. **Rich, consistent frontmatter** — `type`, `date`, `tags`, `ai-first: true`, plus type-specific fields
4. **Recency markers per claim** — "Mem0 raised $24M (tính đến 2026-04, mem0.ai)"
5. **Sources preserved verbatim** — every external claim has its source URL inline
6. **Cross-links mandatory** — every person/project/idea/decision uses `[[wikilinks]]`
7. **Confidence levels** — `stated | high | medium | speculation` where applicable

### Never create in isolation

Every write must ask: *where else does this belong?*

| You create/update... | Also update... |
|---|---|
| A new project note | Kanban board (Backlog), today's daily note |
| A task completed | Kanban board (Done), project note, daily note |
| A person note | Daily note (mention interaction), People index |
| A dev log | Daily note, project note (Recent Activity) |
| A decision made | Project note (Key Decisions), daily note |
| Any vault write | `log.md` (timestamped entry), `index.md` (if new note) |

When operating without filesystem access, list these "also update" notes for the user so they propagate manually.

### Bi-temporal facts — never overwrite, always append

When a fact changes (role, company, status, location, tool), NEVER delete the old value. Add a new entry to `timeline:` frontmatter array with both event time AND transaction time:

```yaml
timeline:
  - fact: "CTO tại Single Grain"
    from: 2024-01-01
    until: 2026-04-07
    learned: 2026-02-23
    source: "[[2026-02-23]]"
  - fact: "Architect tại Single Grain"
    from: 2026-04-07
    until: present
    learned: 2026-04-07
    source: "[[2026-04-07]]"
```

Top-level fields (`role:`, `status:`, `company:`) reflect CURRENT state. The `timeline:` preserves history.

### CRITICAL_FACTS.md — always loaded

A tiny file (~120 tokens) at vault root. Contains: timezone, current manager, current location, current company and role, plus any fact that's true RIGHT NOW and relevant to every interaction. Update whenever a critical fact changes. Keep under 150 tokens.

### Search before creating

Before creating any new note, search for an existing one. Duplicate notes are vault rot. Merge or update instead.

### Match the vault's voice

Read existing notes in the same folder before writing new ones. Match frontmatter schema, heading style, list formatting, tone. Never introduce new conventions — extend what's already there.

### Frontmatter is mandatory

Every note gets frontmatter. At minimum:

```yaml
---
date: 2026-03-24
tags:
  - <note-type>
ai-first: true
---
```

See `references/vault-schema.md` for full frontmatter specs by note type.

---

## Write rules (summary)

See `references/write-rules.md` for the complete guide. Highlights:

- **Links**: `[[Note Name]]` for internal links. Always link people, projects, jobs mentioned in a note.
- **Dates**: ISO format (`YYYY-MM-DD`) in frontmatter. Vietnamese format (`24 tháng 3`) acceptable in body text.
- **Naming**: `YYYY-MM-DD — Title.md` for dated notes. `Title.md` for evergreen notes.
- **Status values**: `active` / `planning` / `completed` / `archived` / `on-hold` for projects. `in-progress` / `done` / `waiting` for tasks. (Keep English for Dataview compatibility.)
- **Kanban**: Items: `- [ ] 🔴 **Title** · @{YYYY-MM-DD}\n\tDescription [[Link]]`

---

## The `_CLAUDE.md` file

`_CLAUDE.md` lives at the vault root and persists Claude's operating rules across every session. Without it, Claude has to re-learn vault conventions every conversation.

**Precedence rule:** `_CLAUDE.md` wins on all vault-specific rules (folder names, naming conventions, frontmatter fields, auto-save behavior, private folders). Skill defaults apply only where `_CLAUDE.md` is silent.

**Contents:** vault's folder map, frontmatter schemas, naming conventions, what to auto-save vs. ask first, people and projects with special handling, links to key files (boards, dashboard, templates).

To generate one for an existing vault, run `/obsidian-init` — Claude scans the vault and outputs the file as a markdown block for the user to save.

---

## Commands

These slash commands work on any Claude surface that loads this skill (claude.ai, Claude Desktop, Claude Code). Each one is smart — it reads context, searches before writing, and propagates everywhere changes belong.

**Name matching:** If a name argument has a typo or is approximate, search the vault for the closest match, show what was found, and confirm before proceeding. Never silently create a note with a misspelled name.

### Operations — Claude remembers

#### `/obsidian-save`

The master save command. Reads the entire conversation and extracts everything worth preserving.

Steps:
1. Scan the conversation, identify vault-worthy items: decisions, tasks, people, projects, ideas, learnings, mentions
2. Group by type
3. For each group, output a markdown block: filename + full note content following AI-first rule
4. List propagation targets (kanban boards, daily note, linked notes) the user should also update
5. Provide a clean summary of what was saved and where it should go

#### `/obsidian-daily`

Creates or updates today's daily note. Output the note as a markdown block. Include sections for: tasks in progress, people mentioned, decisions made, what's being worked on. If the note exists, inject new content into the right sections.

#### `/obsidian-log`

Logs a work or dev session. Infer the project from conversation. Fill in: date, project, work done, problems, decisions, next steps. Output as `Dev Logs/YYYY-MM-DD — Project Name.md`. List the project note's Recent Activity section + today's daily note as propagation targets.

#### `/obsidian-task [description]`

Adds a task to the right kanban board. Infer priority (🔴/🟡/🟢), due date, linked project, linked person. Output the kanban card line + task note (if substantial). List the project note + today's daily note as propagation targets.

#### `/obsidian-person [name]`

Creates or updates a person note. Search vault for fuzzy match. Output `People/Full Name.md` with full frontmatter. Fill in: role, company, context, relationship strength, last interaction date.

#### `/obsidian-decide [topic]`

Extracts decisions from the conversation. For each, output the project note's Key Decisions section update with date and reasoning.

#### `/obsidian-capture [idea]`

Quick idea capture. Search Ideas/ for related notes. Output `Ideas/Title.md` with minimal frontmatter (`date`, `tags: [y-tuong]`). Add a brief mention to today's daily note.

#### `/obsidian-find [query]`

Smart vault search. If filesystem access is available, run search. Otherwise, ask the user to paste the relevant notes or run the search themselves and paste results. Return matches with context: title, folder, excerpt, type. Group by type if ambiguous.

#### `/obsidian-recap [today|week|month]`

Summarizes a time period. Default: week. If filesystem available, list daily notes in range. Otherwise, ask user to paste them. Synthesize into a clean narrative — not a raw dump.

#### `/obsidian-review`

Generates a structured weekly or monthly review. Sections: What I accomplished, Key decisions, People I worked with, What I learned, What to carry forward. Output as `Reviews/YYYY-MM-DD — Weekly Review.md`.

#### `/obsidian-board [board name]`

Shows or updates a kanban board. Read state, identify overdue items, infer changes from conversation. Output the updated board markdown.

#### `/obsidian-project [name]`

Creates or updates a project note. Output `Projects/Project Name.md` with full frontmatter (`date`, `tags: [du-an]`, `status: active`, `job`). List propagation: kanban board card + today's daily note.

#### `/obsidian-health`

Runs a vault health check (heuristic, no Python). Asks the user to paste `index.md` and `log.md` (last 20 entries) so Claude can audit. Reports findings grouped by severity (critical / warning / info): broken links, duplicates, stale tasks, missing frontmatter, contradictions, concept gaps, stale claims, orphans.

#### `/obsidian-init`

Bootstraps `_CLAUDE.md` for the vault. Asks the user about: folder structure (or paste current structure), templates they use, kanban boards, naming conventions. Outputs a complete `_CLAUDE.md` using `references/claude-md-template.md`. The user pastes it into vault root.

#### `/obsidian-ingest`

Ingests a source (URL, PDF text, transcript, screenshot description) into the vault. One source touches many pages.

Steps:
1. Accept the source content (text or URL the user fetched and pasted)
2. Classify: article, PDF, transcript, video, raw text
3. Extract: entities (people, companies, tools), concepts, claims, action items, notable quotes
4. Output: original source as `Knowledge/YYYY-MM-DD — Title.md` + updates for each affected People/Projects/Ideas/Knowledge note
5. Each ingest should touch 5-15 notes. Compile knowledge once, distribute everywhere.

#### `/obsidian-synthesize`

Automatic synthesis — the vault thinks for itself. Scans recent activity (user pastes `log.md` last 20 entries) and finds patterns: same concept in 2+ unrelated sources, entity convergence, concept evolution, orphan rescue. Output synthesis pages as `wiki/concepts/Synthesis — Title.md`.

#### `/obsidian-reconcile`

Finds and resolves contradictions across the vault. User pastes relevant notes. For each contradiction: clear winner (rewrite outdated, add History section), ambiguous (create `wiki/decisions/Conflict — Topic.md`), or evolution (update to current with historical context).

#### `/obsidian-export`

Exports a clean structured snapshot any tool can consume. Output as JSON or markdown index of all notes the user has shared so far.

#### `/obsidian-adr`

Generates a decision record for a structural decision. Output `Knowledge/ADR-YYYY-MM-DD — Title.md` with: Decision, Context, Options Considered, Rationale, Consequences, Related links.

#### `/obsidian-visualize`

Generates a visual canvas map of the vault. Output an Obsidian Canvas JSON the user can import: hub nodes centered, color-coded by type, orphans highlighted.

#### `/obsidian-learn`

Reviews vault learnings. User pastes Knowledge/ + recent reviews. Claude prunes stale lessons, surfaces active patterns, suggests promotions to rules in `_CLAUDE.md`.

### Thinking — Claude thinks with you

#### `/obsidian-challenge`

Red-teams the user's current idea against their own vault history. User pastes relevant past decisions, dev logs, archived notes. Claude returns a structured Red Team analysis: position, counter-evidence cited from vault, blind spots, verdict.

#### `/obsidian-emerge`

Surfaces unnamed patterns from recent notes. User pastes last 30 days of daily notes + dev logs. Claude returns a Pattern Report: recurring themes, emotional patterns, unnamed conclusions, emerging directions — each with cited evidence.

#### `/obsidian-connect [topic A] [topic B]`

Bridges two unrelated domains. User pastes notes from each domain. Claude finds shared links, tags, people, semantic overlap. Returns 3-5 concrete connections — structural analogies, transfer opportunities, collision ideas.

#### `/obsidian-graduate`

Promotes an idea fragment into a full project. User pastes the idea note + related context. Claude generates a complete project spec in `Projects/`: goals, key tasks (phased), open questions, related notes. Updates the original idea note: `status: graduated`.

### Context engine — Claude knows you

#### `/obsidian-world`

Loads identity, values, priorities, current state in one shot using progressive context levels:

1. **L0 (~200 tokens)** — User pastes `SOUL.md` + `CORE_VALUES.md`
2. **L1 (~1-2K tokens)** — User pastes `index.md` + `log.md` (last 10 entries)
3. **L2 (~2-5K tokens)** — User pastes `Home.md`/`Dashboard.md`, today's daily note, last 3 daily notes, active kanban boards
4. **L3 (on demand, ~5-20K tokens)** — Active project notes, recently mentioned people

Present a brief status after L0-L2 (do NOT load L3 unless needed): persona, current priorities, open threads, overdue items, today so far. If identity files don't exist, offer to create them by asking 5-7 quick questions.

---

## Reference files

- `references/ai-first-rules.md` — Complete AI-first vault rule with frontmatter schemas + preamble templates per note type
- `references/vault-schema.md` — Folder structure + frontmatter specs for all note types
- `references/write-rules.md` — Detailed writing, linking, formatting rules
- `references/claude-md-template.md` — Template for generating a vault's `_CLAUDE.md`
- `references/claude-md-assistant-template.md` — Template for assistant mode (managing a vault on behalf of someone else)
