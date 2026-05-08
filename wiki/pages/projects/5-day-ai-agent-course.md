---
title: 5-Day AI Agent Course
type: project
public: false
tags: [ai, agents, crewai, course, learning, deployment]
updated: 2026-05-08
---

# 5-Day AI Agent Course

A hands-on course from MIT IAP / NANDA for building AI agents from scratch using CrewAI and an LLM of choice.

**Repo:** [https://github.com/MIT-NANDA/5-day-course](https://github.com/MIT-NANDA/5-day-course) (cloned locally to `~/5-day-course`)
**Started:** 2026-05-06
**LLM used:** Claude Haiku (`claude-haiku-4-5-20251001`) — swapped in from the default GPT-4o-mini

## What Each Day Builds

| Day | Topic | What I built |
|-----|-------|-------------|
| Day 1 | Basic agent | Personal Digital Twin — agent with backstory encoding who I am |
| Day 2 | Memory + Tools | Same twin extended with 4 memory types, image analysis, calculator, web search |
| Day 3 | Deploy + API | FastAPI wrapper around the twin; deployed to Railway; `/query` endpoint live |
| Day 4 | A2A communication | Added `/a2a` endpoint; NANDA agent registry; agent-to-agent routing via `@agent-id` |
| Day 5 | Capstone | TBD |

## Day 1: Basic Agent

Built a personal AI twin in CrewAI. Learned:
- The Agent/Task/Crew pattern
- How `role`, `goal`, `backstory` shape an agent's persona
- How to wire a custom LLM (Claude via LiteLLM)
- The difference between Claude Code (my coding assistant) and the Claude API (what agents call at runtime)

## Day 2: Memory + Tools

Extended the twin with memory and tools. Learned:
- Four memory types: Short-Term, Long-Term, Entity, Contextual
- The LLM itself decides what to store in memory and at what importance score
- Memory is stored in LanceDB as 384-dimensional vector embeddings
- Retrieval = cosine similarity × importance + recency
- Tools: built-in (DirectoryRead, FileRead, SerperDev, BrowserbaseLoad) and custom (`BaseTool` subclass)
- Replaced OpenAI-specific tools (DALL-E, VisionTool) with Claude-native alternatives
- Wrote `inspect_memory.py` to browse/clear the LanceDB memory store

## Technical Setup Notes

- CrewAI requires Python 3.10+; macOS system Python is 3.9 — needed `brew install python@3.11`
- Anthropic does not offer a public embeddings API; used local ONNX embedder (MiniLM-L6-v2, 384 dims)
- CrewAI telemetry (OpenTelemetry) conflicts with custom `Memory` objects — disabled with `OTEL_SDK_DISABLED=true`
- Memory backend: CrewAI 1.14+ uses LanceDB (not ChromaDB/SQLite)
- `to_arrow()` works; `to_pandas()` fails due to pyarrow/pandas version conflicts

## Day 3: Deploy via FastAPI

Wrapped the CrewAI agent in a FastAPI app and deployed to Railway. Learned:
- FastAPI + uvicorn as the serving layer; Railway reads `railway.json` for start command
- The agent exposes `POST /query` for direct questions and `GET /health` for uptime checks
- CrewAI re-creates a new `Crew` per request (with memory), not a persistent process
- Memory uses an ONNX embedder locally (avoids OpenAI dependency for embeddings)
- `ANTHROPIC_API_KEY` must be set as a Railway env var; missing or wrong key gives `anthropic.APIConnectionError` — not an auth error in the message, which is confusing

## Day 4: A2A Communication

Added agent-to-agent communication on top of the Day 3 base. Learned:
- A2A = HTTP POST between agents; no special protocol, just a `/a2a` endpoint convention
- NANDA registry (`nest.projectnanda.org`) lets agents discover each other by username
- Strict endpoint separation: `/query` is for humans, `/a2a` is for agents only — no silent fallbacks; wrong usage returns a real error
- Agent identity is configured in code (username, name, description), not env vars
- A2A is useful for multi-agent pipelines, but for simple automation, calling Claude API directly is usually better (no deployment overhead per sub-agent)

## Live Deployment: Migrating to le_site (2026-05-08)

Moved the agent from the course repo into the personal site repo (`le_site`), so wiki and agent live together. Key decisions and lessons:

**Architecture:**
- Agent code lives in `le_site/agent/` — Railway deploys from that subdirectory (Root Directory = `agent`)
- Static site (`index.html`, `chat.html`) served from GitHub Pages — no server needed
- Wiki knowledge compiled into `agent/wiki_context.md` at build time, injected into agent backstory

**Wiki-as-knowledge-base pattern:**
- `build_wiki_context.py` reads all `wiki/pages/` and `wiki/sources/` markdown files and concatenates them into a single file
- That file is committed to the repo and loaded by `main.py` at startup via `Path(__file__).parent / "wiki_context.md"`
- Baking it into the backstory means the agent always has it — no tool calls needed at query time
- Trade-off: requires redeploy when wiki updates (solved by GitHub Actions)

**Automation with GitHub Actions:**
- A workflow triggers on any push that changes `wiki/**`
- It runs `build_wiki_context.py`, commits the updated `wiki_context.md`, which triggers Railway to redeploy
- Loop time: ~3-4 minutes from wiki push to live agent update; fully automatic

**Lessons from Railway setup:**
- GitHub App must have explicit repo access — "all repositories" or add repo individually in GitHub → Settings → Applications
- Root Directory setting in Railway tells it which subdirectory to build from
- `railway.json` should live inside the root directory (i.e., inside `agent/`)
- Custom domain set on `danningc.github.io` repo redirects all `*.github.io` URLs — not just that repo

**Chat UI improvements:**
- Agent responses rendered with `marked.js` for proper markdown formatting
- `white-space: pre-wrap` must be removed from agent bubbles (conflicts with HTML rendering); keep it only for user messages

## Learning Questions

- Can I enforce memory importance scores rather than leaving it to the LLM?
- How does the agent decide *what* to memorize vs. discard mid-conversation?
- What's the practical limit of backstory size before RAG tools are needed instead?

## Related

- [[AI Agents]] — core concepts behind what was built
- [[Vector Embeddings & Semantic Memory]] — how memory retrieval works under the hood