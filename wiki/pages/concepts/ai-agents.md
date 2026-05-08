---
title: AI Agents
type: concept
public: true
tags: [ai, agents, crewai, llm, automation]
updated: 2026-05-06
---

# AI Agents

An AI agent is a software entity that can reason, plan, use tools, and take actions autonomously to accomplish a goal — rather than just responding to a single prompt like a chatbot.

## Anatomy of an Agent

Every agent is defined by four things:

| Component | What it does |
|-----------|-------------|
| **Role** | Who the agent is ("Personal Digital Twin", "Research Analyst") |
| **Goal** | What it's trying to achieve |
| **Backstory** | Context and personality that shapes its responses |
| **LLM** | The language model doing the actual reasoning |

Tools and memory are layered on top. Without them, an agent is just a prompted chatbot. With them, it can take actions in the world and remember across time.

## How Agents Differ from Chatbots

- A chatbot responds to one prompt, then forgets
- An agent can break a task into steps, call tools between steps, observe results, and adjust — all without human intervention
- An agent can persist memory across conversations

## Multi-Agent Orchestration (Crew)

In [[CrewAI]], a **Crew** is a collection of agents + tasks. Each agent handles one specialty; a process manager (sequential or hierarchical) routes tasks between them. Crews enable parallelism and separation of concerns — e.g., a researcher agent gathering data, a writer agent drafting, an editor agent reviewing.

## Tools

Tools extend what an agent can do beyond reasoning:

- **Built-in tools** (CrewAI): DirectoryRead, FileRead, SerperDev (web search), BrowserbaseLoad
- **Custom tools**: subclass `BaseTool`, define an `args_schema` (Pydantic), implement `_run()`
- Tools are invoked by the LLM whenever the task warrants it — the agent decides when to call them

## Agent as a Book / Knowledge Interface

A backstory can contain substantial knowledge — e.g., the full text of a book, a corpus of personal notes. This turns the agent into a queryable interface over that knowledge. The LLM does retrieval and synthesis; the backstory is the knowledge base. (Practical limit: backstory lives in context, so very large knowledge sources should use RAG tools + memory instead.)

## Personal Digital Twin

An agent whose backstory encodes a person's values, history, preferences, and style. Responds to questions as if it were that person. Useful for:
- Letting others query your knowledge/opinions without your time
- Building a reader-facing interface for a book or body of work
- Externalizing and exploring your own thinking

## Related

- [[Vector Embeddings & Semantic Memory]] — how agents remember across conversations
- [[Human-AI Teamwork]] — how humans and agents collaborate effectively
- [[5-Day AI Agent Course]] — hands-on project where these concepts were built
