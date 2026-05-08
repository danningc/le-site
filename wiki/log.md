# Wiki Log

Chronological record of all ingest sessions and major updates.

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
