# 🥀 Wingman AI

> AI-powered dating intelligence for better conversations, smarter decisions, and more confident next moves.

Wingman AI is a modular dating intelligence platform designed to analyze conversation screenshots, understand interaction patterns, retrieve relevant relationship guidance, and turn those signals into practical next-step recommendations.

Instead of focusing on a single message in isolation, Wingman looks at the broader conversation and evaluates signals such as warmth, reciprocity, engagement, flirt energy, message energy, and conversation direction.

The platform combines **OCR, NLP signal analysis, Conversation DNA, local RAG retrieval, decision support, response strategy generation, date planning, and SQLite-based history** into one application.

Built collaboratively by **Aasveer Singh & Akshita Sharda**.

---

## 🧠 The Idea Behind Wingman

Dating conversations can be difficult to interpret because context matters.

A single:

> "okay"

can mean something completely different depending on everything that happened before it.

Wingman is built around a simple principle:

> **Read patterns, not single messages.**

The system attempts to understand the overall interaction by combining multiple conversational signals rather than making a decision from one isolated message.

The resulting analysis is transformed into a structured **Decision Brief** that can help the user understand:

- What the conversation currently feels like
- How engaged the interaction appears to be
- What conversational patterns are visible
- What the user could consider doing next
- Which response strategies may fit the situation
- What supporting guidance exists in the local knowledge base

---

# ✨ What Wingman Can Do

Wingman is organized around several intelligence and decision-support modules.

### 📸 Screenshot Intelligence

Upload a conversation screenshot and Wingman processes it through an analysis pipeline.

```text
Screenshot
    ↓
OCR
    ↓
Text Extraction
    ↓
NLP Signal Analysis
    ↓
Conversation DNA
    ↓
RAG Retrieval
    ↓
Decision Brief
    ↓
Recommended Next Move
