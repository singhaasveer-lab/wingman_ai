# 🥀 Wingman AI

### Dating intelligence for better conversations and better decisions.

Wingman AI is a modular dating intelligence platform that analyzes conversation screenshots, extracts interaction signals, retrieves relevant relationship guidance, and turns those signals into practical next-step recommendations.

Built as a collaborative project by **Asveer & Akshita**.

---

## What Wingman Does

Wingman is designed around one principle:

> **Read patterns, not single messages.**

Instead of treating one text message as the whole story, Wingman looks at broader conversational signals such as:

- Warmth
- Reciprocity
- Engagement
- Flirt energy
- Message energy
- Conversation direction

It then combines those signals with locally retrieved knowledge to produce a structured decision brief.

---

## Core Features

### 📸 Screenshot Intelligence
Upload a conversation screenshot and Wingman runs an end-to-end analysis pipeline:

**Screenshot → OCR → NLP signals → Conversation DNA → RAG → Decision Brief**

The analysis produces:

- Conversation vibe
- Confidence score
- Conversation archetype
- Conversation DNA signals
- Executive interpretation
- Recommended next move
- Evidence-backed guidance
- Response strategies

### ✍️ Reply Lab
Generate response strategies based on:

- Intent
- Communication style
- Boldness
- Message length

The lab turns conversation analysis into practical response options rather than a single generic reply.

### 🎯 Decision Mode
A dedicated decision layer for questions such as:

- Should I text?
- Should I ask them out?
- Should I wait?
- Should I clarify something?
- Should I move on?

Wingman uses the available conversation evidence to provide a recommendation and reasoning.

### 🥂 Date Ideas
Generates structured date plans based on:

- Situation
- Vibe
- Budget
- Activity type
- Time
- Objective

The recommendation engine is local and does not require Google Maps or a live location API.

### 💡 Dating Intelligence
A local knowledge center backed by RAG.

Wingman retrieves relevant principles from `knowledge_base.json` using:

**TF-IDF + cosine similarity**

This keeps recommendations grounded in a curated local knowledge base rather than relying entirely on free-form generation.

### ❤️ Reply Vault & History
Save useful replies and preserve previous conversation analyses using SQLite.

---

## System Architecture

```text
                    ┌─────────────────────┐
                    │    Streamlit UI     │
                    │     Wingman App     │
                    └──────────┬──────────┘
                               │
             ┌─────────────────┼─────────────────┐
             │                 │                 │
             ▼                 ▼                 ▼
       Screenshot         Reply Lab        Decision Mode
       Intelligence
             │
             ▼
        Screenshot
             │
             ▼
          OCR Layer
       (Tesseract OCR)
             │
             ▼
      NLP Signal Analysis
             │
             ▼
      Conversation DNA
             │
             ▼
        Local RAG Layer
   TF-IDF + Cosine Similarity
             │
             ▼
       Decision Brief
             │
             ▼
        Next-Move Strategy

        ┌─────────────────────────────┐
        │          SQLite             │
        │     Saved Replies + History │
        └─────────────────────────────┘

        ┌─────────────────────────────┐
        │          FastAPI            │
        │      Backend / API Layer    │
        └─────────────────────────────┘