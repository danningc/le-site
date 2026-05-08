# Wiki Log

Chronological record of all ingest sessions and major updates.

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
