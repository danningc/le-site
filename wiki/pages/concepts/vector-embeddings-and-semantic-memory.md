---
title: Vector Embeddings & Semantic Memory
type: concept
public: true
tags: [ai, memory, embeddings, vectors, lancedb, crewai]
updated: 2026-05-06
---

# Vector Embeddings & Semantic Memory

Vector embeddings are how AI systems convert meaning into math — turning text into a list of numbers so that semantically similar things end up numerically close to each other.

## What an Embedding Is

A sentence like *"Danning is afraid of falling on slabs"* gets converted into a 384-dimensional vector — a list of 384 floating-point numbers:

```
[-0.0061, 0.0412, 0.0961, 0.0623, 0.0414, -0.0416, ...]
```

Each number is a coordinate in "meaning-space." The model (ONNX/MiniLM-L6-v2) learned these coordinates from billions of text examples, so concepts that co-occur in similar contexts end up in similar regions of that space.

## Cosine Similarity

To compare two memories, the system computes **cosine similarity** — the angle between two vectors in 384D space.

| Score | Meaning |
|-------|---------|
| ~1.0  | Nearly identical meaning |
| ~0.3–0.6 | Related (same domain, person, theme) |
| ~0.0 | Unrelated |
| Negative | Conceptually opposite |

Real example from a [[5-Day AI Agent Course]] session:

| Pair | Cosine similarity |
|------|------------------|
| "Danning fears falling on slabs" vs "Danning is learning French" | **0.38** — both are personal, about Danning |
| "Danning fears falling on slabs" vs "The user works for B Lab" | **−0.07** — unrelated domains |

## Memory Retrieval Ranking

When an agent retrieves a memory for a query, the final rank combines three factors:

```
final_score = (semantic_similarity × weight_s)
            + (importance × weight_i)
            + (recency × weight_r)
```

A highly important memory that's only moderately similar can beat a very similar but low-importance one.

## Memory Types in CrewAI

[[AI Agents]] in CrewAI have four memory types:

| Type | Scope | How it works |
|------|-------|-------------|
| **Short-Term** | Current session | RAG over recent conversation turns |
| **Long-Term** | Across sessions | Persists facts the agent judges important |
| **Entity** | Across sessions | Tracks people, places, concepts and their attributes |
| **Contextual** | Combined | Fuses all three for coherent, context-aware retrieval |

The agent (LLM) decides what to store and at what importance score (0–1) — you don't assign these manually. The LLM reads the conversation and generates structured memory entries as a background step.

## Storage Backend

CrewAI 1.14+ uses **LanceDB** (an Apache Arrow-native vector database) to store memories. Each row contains:
- `content` — the text of the memory
- `vector` — the 384-dim embedding
- `importance` — 0.0–1.0 score
- `scope` — which memory type
- `created_at`, `last_accessed` — timestamps

## Local vs API Embeddings

Embedding is compute-intensive. Options:
- **Local/ONNX** (used here): runs on CPU, no API key, free, slightly slower
- **OpenAI embeddings**: API call per memory, costs money
- **Anthropic**: does not currently offer a public embeddings API — use local or third-party

## Why This Matters for Agent Design

The quality of memory retrieval depends entirely on embedding quality. If the model puts semantically unrelated things close together, the agent will hallucinate false connections. The choice of embedder is as load-bearing as the choice of LLM.

## Related

- [[AI Agents]] — how agents use memory to personalize responses
- [[Human-AI Teamwork]] — confidence signals in AI systems
