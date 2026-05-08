---
title: 5-Day AI Agent Course
type: project
public: false
tags: [ai, agents, crewai, course, learning]
updated: 2026-05-06
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
| Day 3 | Multi-agent crews | TBD |
| Day 4 | Advanced patterns | TBD |
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

## Learning Questions

- Can I enforce memory importance scores rather than leaving it to the LLM?
- How does the agent decide *what* to memorize vs. discard mid-conversation?
- What's the practical limit of backstory size before RAG tools are needed instead?

## Related

- [[AI Agents]] — core concepts behind what was built
- [[Vector Embeddings & Semantic Memory]] — how memory retrieval works under the hood