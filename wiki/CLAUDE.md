# Wiki Schema

This is a personal wiki maintained with Claude Code. It stores compiled knowledge from ingested sources, personal notes, and synthesis.

## Structure

```
wiki/
├── CLAUDE.md        ← this file: schema and instructions
├── index.md         ← master catalog of all pages
├── log.md           ← chronological log of ingests and updates
├── raw/             ← source material (never edit these)
│   ├── articles/
│   ├── books/
│   ├── notes/
│   └── pdfs/
├── pages/           ← wiki knowledge pages
│   ├── people/      ← individuals
│   ├── places/      ← locations, cities, countries
│   ├── concepts/    ← ideas, frameworks, vocabulary
│   ├── projects/    ← things I'm working on
│   └── synthesis/   ← cross-cutting analysis and conclusions
└── sources/         ← one summary page per ingested source
```

## Page Format

Every page in `pages/` and `sources/` must start with this frontmatter:

```markdown
---
title: Page Title
type: person | place | concept | project | synthesis | source
public: true | false
tags: [tag1, tag2]
updated: YYYY-MM-DD
---
```

- `public: true` means this page may be shown on the public-facing website
- `public: false` means this page is private and should never be published

## Conventions

- Use `[[Page Title]]` to link between pages (wiki-link style)
- Every new page must be added to `index.md`
- Every ingest session must be logged in `log.md`
- Cross-references should go both ways: if page A links to B, B should link back to A
- Prefer updating existing pages over creating new ones when the topic already exists

## Workflows

### Ingest
When asked to ingest a source:
1. Read the source file from `raw/`
2. Create a summary page in `sources/` (one page per source)
3. Create or update relevant pages in `pages/`
4. Update `index.md` with any new pages
5. Append an entry to `log.md`

A single source typically touches multiple existing pages — update them all.

### Query
When asked a question:
1. Answer from the compiled wiki pages (not raw sources)
2. If the answer is strong and reusable, offer to save it as a new synthesis page

### Quiz
When asked to quiz:
1. Read the wiki pages to identify concepts, claims, and people ingested so far
2. Ask 3–5 questions that test *understanding*, not recall — avoid questions answerable by just remembering a name or label
3. Good question types:
   - "Explain X in your own words"
   - "Why does X imply Y?"
   - "What's the difference between X and Y?"
   - "Give an example of X that wasn't in the source"
   - "What would have to be true for this claim to be wrong?"
4. Wait for answers one question at a time (do not dump all questions at once)
5. After each answer, give honest feedback: what was right, what was shallow, what was missing
6. After all questions, give an overall assessment of where understanding is solid vs. where it's still surface-level
7. Optionally offer to log a quiz summary to `log.md`

The goal is to surface name-dropping vs. genuine understanding. Push back on vague answers. Ask follow-ups if an answer is incomplete.

### Lint
When asked to lint:
1. Check for broken `[[links]]` (pages referenced but not existing)
2. Flag contradictions between pages
3. Flag orphaned pages (not linked from anywhere)
4. Flag pages with no `updated` date or missing frontmatter

## Confidence Signals

In any response, distinguish clearly between three levels of confidence:

| Signal | Usage |
|---|---|
| **Direct** | Explicitly stated in a source — high confidence |
| **Inferred** | Not stated, but follows logically from what is — medium confidence |
| **Uncertain** | Plausible but not well-supported — flag it explicitly |

### How to apply this per workflow

**Ingest:** When writing source summaries or concept pages, flag any interpretation that goes beyond what the author explicitly said. Use phrasing like "the author implies..." or "this is my reading, not stated directly."

**Query:** Before answering, state how confident you are and why — e.g., "this is directly from Shtulman's abstract" vs. "I'm inferring this from the combination of Benjamin and Moeller."

**Quiz:** When giving feedback, distinguish between:
- "You were wrong — the source says X"
- "The source was ambiguous on this — reasonable to be unsure"
- "That's actually an open question not answered by anything ingested yet"

### Why this matters

Without confidence signals, the user cannot calibrate how much to trust a response. They may defer on something Claude is guessing at, or doubt something Claude is certain of. Expressing calibrated uncertainty is load-bearing for good collaboration — not a sign of weakness.

## Public/Private Rule

Never include content from pages marked `public: false` in any public-facing output. When building the public site interface, only pull from pages where `public: true`.
