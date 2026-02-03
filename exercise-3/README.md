 
# Exercise 3 — Mini RAG (Retrieval-Augmented Generation)

## Objective
In this exercise, you will build a **knowledge-aware AI assistant** using
**Retrieval-Augmented Generation (RAG)**.

Unlike a normal chatbot, this assistant will answer questions
**using your own documents**, not just general knowledge.


## What You Will Learn

- What RAG is and why enterprises use it
- How embeddings convert text into vectors
- How similarity search works
- How AWS Bedrock fits into RAG systems
- Why RAG ≠ model training


## Architecture Overview
```bash
Local Documents (.txt)
↓
Text Chunking
↓
Amazon Titan Text Embeddings v2
↓
In-Memory Vector Store
↓
Similarity Search (Top-K)
↓
Amazon Nova Lite (Bedrock)
↓
Grounded Answer

```


## Prerequisites

### 1. Python Version
Python **3.10 or later**

Check:
```bash
python --version
```
### 2. AWS Credentials
Ensure the following environment variables are set:

AWS_ACCESS_KEY_ID

AWS_SECRET_ACCESS_KEY

AWS_DEFAULT_REGION=us-east-1

## Installation
```bash
pip install -r requirements.txt
```

## Folder Structure
```bash
Exercise-3/
├── documents/
│   ├── ai_basics.txt
│   ├── aws_bedrock.txt
│   └── rag_overview.txt
├── rag_assistant.py
├── requirements.txt
└── README.md
```
## How to Run
```bash
python rag_assistant.py
```
Then ask questions like:

What is Amazon Bedrock?

What is Retrieval-Augmented Generation?

Why do enterprises use RAG?

Type exit to quit.

## Key Concept Reminder
In production, embeddings are stored in systems like OpenSearch or Aurora.
In this lab, we use in-memory vectors to focus on the core RAG logic.

## Learning Outcomes
By completing this exercise, you will understand:

How documents become searchable knowledge

How LLMs are grounded using retrieval

How AWS Bedrock supports enterprise RAG systems

## End of Lab
You have now built:

A text chatbot

A voice assistant

A document-aware AI assistant (RAG)


## Congratulations 🎉

