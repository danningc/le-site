# Danning's Personal Wiki

This is a compiled knowledge base representing what Danning has learned and studied. Use it to answer questions about topics, people, concepts, and projects Danning has engaged with.

---

## Acquired Metabolism

# Acquired Metabolism

The phenomenon where an organism gains access to metabolic capabilities from another species through ecological interaction — rather than encoding those capabilities in its own DNA.

## Why It Matters

Biology typically treats metabolism as fixed by genetics. Acquired metabolism complicates this: an organism's functional capabilities are partly determined by *who it interacts with*, not just what's in its genome.

This reframes the organism as partially open — a metabolic borrower — and blurs the line between individual and ecosystem.

## How It Is Acquired

Interactions that enable acquired metabolism range across the spectrum:

| Interaction | Example |
|---|---|
| Predation | Marine microbes stealing chloroplasts from eaten algae (kleptoplasty) |
| Mutualism | Trees partnering with fungi to access soil nutrients (mycorrhizae) |

## Consequences

- **Niche expansion:** Organisms can exploit resources or environments they couldn't access on their own
- **Evolutionary diversification:** New metabolic possibilities open new evolutionary trajectories
- **Biodiversity maintenance:** Metabolic interdependencies create stable ecological webs

## Examples in Detail

**Kleptoplasty (chloroplast theft)**
Certain marine microbes consume photosynthetic algae and retain the functional chloroplasts. For a period after eating, the microbe can photosynthesize — gaining a plant-like metabolism through predation.

**Mycorrhizal mutualisms**
Fungi colonize tree roots and extend their hyphal networks deep into soil, feeding the tree phosphorus and nitrogen. The tree feeds the fungus sugars. Both partners access metabolism the other provides.

## Related
- [[Holly Moeller]]
- [[Ecological Mutualism]]

---

## AI Agents

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

---

## Human-AI Teamwork

# Human-AI Teamwork

The study and practice of humans and AI agents collaborating on tasks, especially complex decision-making.

## Why It Matters

Human-AI teams are increasingly used in high-stakes settings (government, military, medicine). Getting this right matters — a poorly designed AI teammate can make human decisions *worse* even if the AI is highly capable on its own.

## What Makes Human-AI Teams Work

Key insight from [[Aaron S. Benjamin]]: teams work best when both sides can express and coordinate **metacognitive states** — signals about confidence, uncertainty, and competence.

An AI that says "I'm 90% confident" is easier to collaborate with than one that just says "The answer is X." The confidence signal lets the human know when to defer and when to push back.

## Key Findings

- Humans paired with **metacognitively sophisticated agents** (those that express calibrated confidence) outperform humans paired with naive agents
- Confidence calibration in neural networks is an open engineering problem — current methods vary in scalability and accuracy
- **Counterintuitive:** agents that slightly *reduce* accuracy to accommodate human [[metacognitive illusions]] can produce better team outcomes than maximally accurate agents

## Open Problems
- How to scale confidence calibration across different neural network architectures
- How to embed metacognitive signals in AI communication naturally (not just as a number)
- How to assess metacognitive capacity for team settings specifically

## Related
- [[Metacognition]]
- [[Confidence Calibration]]
- [[Aaron S. Benjamin]]

---

## Imagination

# Imagination

The capacity to conceive of things beyond direct experience — possibilities, counterfactuals, fictions.

## Common Misconception

The popular view: imagination is the special province of childhood. Adults lose it as they accumulate knowledge and convention.

The evidence: the opposite is closer to true.

## Knowledge as the Foundation of Imagination

From [[Andrew Shtulman]]'s research on cognitive development:

- Young children are **imitators**, not innovators
- When facing novel problems, they default to familiar patterns and struggle to think outside them
- Their pretend play simulates real life — mundane scenarios, routine behaviors — not fantastical invention
- Creativity in children is bounded by what they consider *probable* or *normal*

The reason: they lack sufficient knowledge of reality. You need a rich model of how the world works before you can meaningfully depart from it.

> "The key to expanding the imagination is not forgetting what you know but learning something new."
> — [[Andrew Shtulman]]

## Implications

- Learning more does not constrain imagination — it expands it
- The "beginner's mind" ideal (empty mind = free imagination) may be backwards
- Expertise and imagination are not in tension; expertise is a prerequisite

## Open Questions
- At what point does knowledge start to *constrain* rather than enable? (Is there a ceiling effect?)
- How does this interact with [[Metacognition]] — does knowing what you don't know also expand imagination?

## Related
- [[Andrew Shtulman]]
- [[Cognitive Development]]

---

## Metacognition

# Metacognition

"Thinking about thinking." The ability to monitor and regulate one's own knowledge, confidence, and uncertainty.

## Forms of Metacognitive Information

Metacognitive information can be expressed:
- **Explicitly:** stated confidence levels, explanations, admissions of uncertainty
- **Implicitly:** tone of voice (prosody), nonverbal cues, hedging language

## Role in Group Decision-Making

In human teams, metacognitive exchange is load-bearing — it allows people to:
- Delegate tasks to whoever is most competent
- Weight each other's contributions appropriately
- Produce collaborative assessments better than any individual could

## Metacognitive Illusions

Humans are sometimes *miscalibrated* — confident when wrong, or uncertain when right. These illusions are systematic. See [[Confidence Calibration]].

Interestingly, AI agents can be designed to *accommodate* these illusions (rather than correct them), which can improve teamwork outcomes even at the cost of some raw accuracy. Source: [[Aaron S. Benjamin]].

## In Human-AI Teamwork

For human-AI teams to work well, both sides need aligned means of expressing metacognitive states. An AI that gives answers without confidence signals is harder to work with than one that communicates uncertainty — even if its answers are equally accurate.

See: [[Human-AI Teamwork]], [[Confidence Calibration]]

---

## Vector Embeddings & Semantic Memory

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

---

## Aaron S. Benjamin

# Aaron S. Benjamin

Cognitive psychologist at the **University of Illinois Urbana-Champaign**. Runs a lab focused on metacognition — particularly how people monitor and regulate their own knowledge and uncertainty.

## Research Focus

His recent work extends into **human-AI teamwork**: how can AI agents express metacognitive states (confidence, uncertainty) in ways that make human-AI teams more effective?

## Key Ideas
- Metacognitive exchange is central to effective group decision-making
- AI agents should be *metacognitively sophisticated*, not just accurate
- Counterintuitive finding: agents that slightly compromise accuracy to accommodate human [[metacognitive illusions]] can improve team outcomes

## Sources
- [[Metacognition in Human-AI Teamwork (Benjamin)]] — talk abstract

---

## Andrew Shtulman

# Andrew Shtulman

Cognitive developmental psychologist at **Occidental College**. Studies how children understand and reason about the world — including the relationship between knowledge, belief, and imagination.

## Key Argument

Children are not naturally imaginative in the way adults romanticize. They are imitators. Their creativity is capped by their model of what is normal. Imagination grows with knowledge, not against it.

## Sources
- [[Imagination and Cognitive Development (Shtulman)]] — talk abstract

---

## Holly Moeller

# Holly Moeller

Biologist at **University of California, Santa Barbara**. Studies how organisms acquire metabolic capabilities from other species — and what this means for ecological diversity and evolution.

## Key Argument

Metabolism is not purely genetic. Species routinely borrow metabolic functions from others through ecological interactions (mutualism, predation). This "acquired metabolism" is a major driver of niche expansion and biodiversity.

## Methods
Combines field work, lab experiments, and mathematical modeling — with an emphasis on models as the bridge between observation and mechanistic understanding.

## Sources
- [[Acquired Metabolism (Moeller)]] — talk abstract

---

## 5-Day AI Agent Course

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

---

## "Metacognition in Human-AI Teamwork (Benjamin)"

# Metacognition in Human-AI Teamwork

**Author:** [[Aaron S. Benjamin]]
**Affiliation:** University of Illinois Urbana-Champaign
**Format:** Talk abstract

## Summary

Benjamin argues that effective group decision-making depends on the exchange of *metacognitive information* — signals about one's own confidence, mastery, and uncertainty. This exchange happens explicitly (stated confidence, explanations) and implicitly (prosody, nonverbal cues). His lab's research applies this insight to human-AI teams, asking: can AI agents communicate metacognitive states in ways that make teams work better?

## Three Research Projects

**1. Human team decision-making**
Examined what makes metacognitive exchange between humans successful in general-knowledge and estimation tasks. Identified the critical components that help vs. hurt group performance.

**2. Confidence calibration in neural networks**
Developed algorithms to scale confidence assessments from neural networks that are: scalable, architecture-agnostic, and calibrated similarly to human confidence ratings.

**3. Human + metacognitive agent outperforms human + naive agent**
In estimation tasks, humans paired with agents that express calibrated confidence outperform humans paired with agents that give answers without confidence signals.

**Bonus finding (counterintuitive):**
AI agents can *enhance* teamwork by deliberately compromising the accuracy of their advice to accommodate human [[metacognitive illusions]]. Slightly less-accurate-but-better-communicated advice beats maximally accurate but poorly calibrated advice.

## Key Insight

Human-AI teams will only reach full potential when both sides have *aligned means* of expressing and coordinating metacognitive states. Confidence signals are not a nice-to-have — they are load-bearing for collaboration.

## Related Pages
- [[Aaron S. Benjamin]]
- [[Metacognition]]
- [[Human-AI Teamwork]]
- [[Confidence Calibration]]

---

## "Acquired Metabolism (Moeller)"

# Acquired Metabolism

**Author:** [[Holly Moeller]]
**Affiliation:** University of California, Santa Barbara
**Format:** Talk abstract

## Summary

Metabolism is usually thought of as fixed — encoded in an organism's DNA. Moeller challenges this: many species *borrow* metabolic capabilities from other species through ecological interactions, from mutualism to predation. This "acquired metabolism" allows organisms to expand their ecological niche, driving evolutionary diversification and maintaining biodiversity.

## Two Case Studies

**1. Chloroplast-stealing marine microbes (kleptoplasty)**
Certain marine microbes steal functional chloroplasts from the algae they eat, temporarily gaining the ability to photosynthesize. The microbe expands its metabolic repertoire through predation.

**2. Tree-fungal mutualisms (mycorrhizae)**
Trees partner with fungi, gaining access to the fungi's nutrient-acquisition metabolism (phosphorus, nitrogen from soil). The fungus gains sugars. Both expand what they can "do" metabolically.

## Methods
Moeller's lab combines:
- Field observations and specimen collection
- Laboratory experiments
- Mathematical models (emphasized as central)

The argument is that the synergy between these approaches — not any one alone — reveals the mechanisms underlying acquired metabolism.

## Central Claim

Metabolism is not hard-wired. It is partially *social* — obtained through interaction. This blurs the boundary between individual and ecosystem, and is a key driver of biodiversity.

## Related Pages
- [[Holly Moeller]]
- [[Acquired Metabolism]]
- [[Ecological Mutualism]]

---

## "Imagination and Cognitive Development (Shtulman)"

# Imagination and Cognitive Development

**Author:** [[Andrew Shtulman]]
**Affiliation:** Occidental College
**Format:** Talk abstract

## Summary

Shtulman challenges the common belief that imagination peaks in childhood. His argument, grounded in cognitive development research: children are actually *imitators*, not innovators. Their creativity is bounded by what they consider normal, typical, or probable — and their pretend play tends to simulate real life rather than invent fantastical scenarios.

The root cause: children lack knowledge. It is *knowledge of what is real* that enables imagining what is possible. More knowledge → more imaginative range, not less.

## Central Claim

> "The key to expanding the imagination is not forgetting what you know but learning something new."

This directly contradicts the "beginner's mind" intuition (that knowing less frees you to imagine more).

## Key Points

- Children default to imitation when facing novel challenges — they struggle to think outside established patterns
- Pretend play is mostly mundane: children rehearse real behaviors, not fanciful ones
- Creativity is constrained by one's model of what is normal/probable
- Knowledge of reality is the *foundation* for contemplating possibility
- Imagination is not innate and fixed — it grows with learning

## Related Pages
- [[Andrew Shtulman]]
- [[Imagination]]
- [[Cognitive Development]]