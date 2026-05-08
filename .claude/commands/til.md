---
description: Today I Learned — reflect on a session, capture trials/errors, open questions, and push a summary into the wiki log
allowed-tools: ["AskUserQuestion", "Read", "Write", "Edit"]
---

# /til — Today I Learned

Guide Danning through a structured reflection on the current session, then write the summary into `wiki/log.md`.

## Step 1: Learning Intention

Ask what they set out to learn or accomplish today:

Use AskUserQuestion:
- Question: "What was your learning intention coming into this session? What were you trying to figure out or get done?"
- Header: "Intention"
- Options: (offer 3 common framings + other)
  - "Explore something new" — first contact with a tool, concept, or workflow
  - "Go deeper on something I started" — building on a prior session
  - "Get something working" — practical goal, less about learning
  - Other (free text)

Wait for the answer. Store it.

## Step 2: Trials and Errors

Reflect on what actually happened — the messy middle. Based on the conversation so far, draft a short summary of:
- What was tried
- What didn't work and why (errors, unexpected behavior, wrong assumptions)
- What eventually worked and what the key unlock was

Then show the user this draft and ask them to confirm or correct it:

Use AskUserQuestion:
- Question: "Here's my summary of the trials and errors from this session — does this capture it, or should I change anything? [show draft inline in the description]"
- Header: "Trials & Errors"
- Options:
  - "Looks right" — proceed as is
  - "Adjust it" — user will provide corrections in free text
  - "Skip this section" — don't include in wiki

## Step 3: Open Questions & Follow-Ups

Ask what's still unresolved:

Use AskUserQuestion:
- Question: "What's still fuzzy, unresolved, or worth revisiting in a future session?"
- Header: "Open Questions"
- multiSelect: true
- Options based on what came up in the session (infer from conversation), e.g.:
  - "How X actually works under the hood"
  - "Edge cases I didn't test"
  - "A related thing I want to try next"
  - Other (free text)

Wait for the answer. If they select options, also ask for any free-form detail with a follow-up question.

## Step 4: Write to Wiki

Read `wiki/log.md` to see the existing format, then prepend a new entry at the top (after the `---` separator, before the previous most-recent entry). Follow the existing style exactly.

**Entry format:**

```markdown
## YYYY-MM-DD — TIL: [short title derived from what was learned]

**Intention:** [what they came in wanting to learn/do]

**What was learned:**
[2-4 bullet points: key insight, technique, or fact — phrased as takeaways, not task descriptions]

**Trials and errors:**
[2-4 bullet points: what failed, what was confusing, what the unlock was]

**Open questions / follow-ups:**
[bullet list of unresolved things, or "None" if they said so]
```

Use today's date from `$CURRENT_DATE` or infer from context.

After writing, confirm: "Logged to wiki/log.md. Here's your TIL entry." and show the final text.

## Tone

Be warm and genuinely curious — this is a reflection ritual, not a debrief. Ask like a collaborator who was in the session with them, not like a form to fill out.
