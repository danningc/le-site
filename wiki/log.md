# Wiki Log

Chronological record of all ingest sessions and major updates.

---

## 2026-05-08 — TIL: Gmail MCP, cloud routines, and first Google Cloud setup

**Intention:** Get something working — set up Gmail MCP automation and a daily email digest routine.

**What was learned:**
- Gmail MCP tools map directly to Gmail's underlying model: `search_emails`, `read_email`, `modify_email`, `send_email` — "mark as read" is just `modify_email` removing the `UNREAD` label
- `/schedule` creates a cloud routine on Anthropic's infrastructure that keeps running after session close — the prompt must be fully self-contained since the remote agent starts with zero context
- Cron expressions are always UTC — always explicitly convert from local timezone before saving (Amsterdam CEST = UTC+2, so `0 6 * * *` = 8am local)
- Set up Google Cloud Console for the first time to enable MCP credentials — the steps worked but the mental model of how OAuth/project IDs/Claude connectors all link together is still forming

**Trials and errors:**
- First time setting up Google Cloud Console: followed Claude's steps and it worked, but the full picture of how GCP credentials connect to Claude's MCP connectors isn't internalized yet
- MCP tool discovery is trial-and-error — no upfront documentation on what tools exist or what parameters they expect; had to probe as we went

**Open questions / follow-ups:**
- How does Google Cloud Console actually connect to Claude / MCP? (OAuth flow, project IDs, credential types)
- Did the daily email routine (`0 6 * * *`) actually fire? First confirmation will come next morning.

---

## 2026-05-08 — Session: MCP tools and cloud automation

Created concept page: `pages/concepts/mcp-tools-and-cloud-automation.md`
Updated `index.md` with new concept.

**What was covered:**
- Gmail MCP: searched, read, and summarized 34 unread emails in one session; sent an email to a contact directly from Claude Code
- Marking emails as read = `modify_email` removing the `UNREAD` label — that's the underlying Gmail model
- `/loop` and `/schedule` skills: `/loop` for session-local recurring tasks; `/schedule` creates a RemoteTrigger cloud routine that survives session close
- Built a daily email summary routine: runs at 8am Amsterdam (6am UTC, `0 6 * * *`), searches unread emails, sends a digest to `danningch@gmail.com` with sender/subject/1-line summary/suggested action, asks user to reply with instructions
- Cloud routine anatomy: cron expression (UTC), self-contained prompt, MCP connections, Anthropic cloud environment — remote agent has no local access
- Timezone conversion: cron is always UTC; Amsterdam CEST = UTC+2

---

## 2026-05-08 — Session: Days 3 & 4 + live deployment of digital twin

Updated project page: `pages/projects/5-day-ai-agent-course.md`

**What was covered:**
- Day 3: FastAPI wrapper around CrewAI agent; deployed to Railway; `/query` endpoint; per-request Crew creation; ONNX embedder for memory
- Day 4: A2A communication protocol; NANDA registry; strict `/query` vs `/a2a` endpoint separation; when to use A2A vs direct Claude API calls
- Migrated agent from `5-day-course` repo to `le_site/agent/` — wiki and agent now live together
- Built `build_wiki_context.py`: compiles public+private wiki pages into a single file injected into agent backstory at startup
- Set up GitHub Actions workflow: auto-runs `build_wiki_context.py` and commits on any `wiki/**` change → triggers Railway redeploy (~3-4 min loop)
- Fixed markdown rendering in chat UI with `marked.js`
- Fixed Chinese name in backstory: 陈丹凝
- Debugged Railway: GitHub App repo access, Root Directory config, `danningc.github.io` domain redirect affecting all GitHub Pages

---

## 2026-05-06 — Learning session: Days 1 & 2 of 5-Day AI Agent Course
- Created project page: `pages/projects/5-day-ai-agent-course.md`
- Created concept page: `pages/concepts/ai-agents.md`
- Created concept page: `pages/concepts/vector-embeddings-and-semantic-memory.md`
- Updated `index.md` with new concepts and project

**What was covered:**
- Day 1: Agent/Task/Crew pattern in CrewAI; personal digital twin with Claude Haiku; role/goal/backstory as agent identity
- Day 2: Four memory types (short-term, long-term, entity, contextual); tools (built-in + custom); LanceDB storage backend; vector embeddings and cosine similarity for memory retrieval
- Hands-on: replaced all OpenAI tooling with Claude alternatives; wrote inspect_memory.py; explored actual 384-dim vectors from LanceDB to understand how semantic similarity works in practice

---

## 2026-05-05 — Quiz (Benjamin, Shtulman, Moeller)

**Questions asked:**
1. Why do people believe children are more imaginative, even if Shtulman is right?
2. Why would evolution favor chloroplast-stealing over evolving your own chloroplasts?
3. Why would a less accurate AI make a better teammate? (Benjamin's bonus finding)
4. What thread connects all three talks?

**Assessment:**
- Shtulman: identified playfulness vs. imagination distinction (solid), missed the specific mechanism (children's play is actually imitative, not whimsical)
- Moeller: right direction on flexibility, didn't articulate why borrowed metabolism beats permanent encoding (conditional access, no overhead)
- Benjamin bonus: didn't know — hardest question
- Synthesis: found a real thematic thread (growth, accumulation) but stayed abstract; the structural parallel (blank-slate intuition is wrong across all three) was just out of reach

**To work on:** explaining the *why* behind ideas, not just the *what*

## 2026-05-05 — Ingest: Moeller talk abstract (acquired metabolism + biodiversity)
- Added raw source: `raw/articles/moeller-acquired-metabolism.md`
- Created source summary: `sources/moeller-acquired-metabolism.md`
- Created person page: `pages/people/holly-moeller.md`
- Created concept page: `pages/concepts/acquired-metabolism.md`
- Updated `index.md`

## 2026-05-05 — Ingest: Shtulman talk abstract (imagination + cognitive development)
- Added raw source: `raw/articles/shtulman-imagination-cognitive-development.md`
- Created source summary: `sources/shtulman-imagination-cognitive-development.md`
- Created person page: `pages/people/andrew-shtulman.md`
- Created concept page: `pages/concepts/imagination.md`
- Updated `index.md`

## 2026-05-05 — Ingest: Benjamin talk abstract (metacognition + human-AI teamwork)
- Added raw source: `raw/articles/benjamin-metacognition-human-ai-teamwork.md`
- Created source summary: `sources/benjamin-metacognition-human-ai-teamwork.md`
- Created person page: `pages/people/aaron-benjamin.md`
- Created concept page: `pages/concepts/metacognition.md`
- Created concept page: `pages/concepts/human-ai-teamwork.md`
- Updated `index.md`

## 2026-05-05 — Wiki initialized
- Created wiki structure: `raw/`, `pages/`, `sources/`
- Wrote `CLAUDE.md` schema
- Wrote `index.md` and `log.md`
