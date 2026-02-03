# Exercise 2 - Voice AI Assistant (STT + LLM)

## Objective

In this exercise, you will convert your text-based AI assistant into a **voice-enabled AI assistant** using **AWS services** and **local system capabilities**.

You will:

- Speak to the AI using your microphone
- Convert speech to text using **Amazon Transcribe**
- Send the text to **Amazon Bedrock (Nova Lite)**
- Hear the AI’s response spoken back using **local Windows Text-to-Speech**

This demonstrates a **real-world Applied AI pipeline** without heavy setup or complex infrastructure.

---

## Architecture Overview

Microphone
↓
Amazon Transcribe (Speech → Text)
↓
Amazon Bedrock (Nova Lite)
↓
Text Response
↓
Windows Local Text-to-Speech

> Note: In production systems, cloud TTS (e.g., Amazon Polly) is often used.  
> For this lab, we use **local TTS** to keep the setup fast and reliable.

---

## Prerequisites

### 1. Python Version

Ensure Python **3.10 or later** is installed.

Check:

```bash
python --version
```
### 2. AWS Credentials

You must have AWS credentials set as environment variables:

AWS_ACCESS_KEY_ID

AWS_SECRET_ACCESS_KEY

AWS_DEFAULT_REGION=us-east-1

(These will be provided during the training.)

### 3. Optional (Recommended)

Set your student ID to avoid S3 file collisions:

Windows (PowerShell):

setx STUDENT_ID student01
If not set, files will be stored under unknown-student/.

## Installation

Install required Python packages:
```bash
pip install -r requirements.txt
```
## How to Run

From the Exercise-2 directory:
```bash
python exercise2_voice_ai_assistant.py
```
## What Will Happen

The program records 5 seconds of audio from your microphone

Audio is uploaded to a shared S3 bucket

Amazon Transcribe converts speech to text

The text is sent to Nova Lite (Bedrock)

The AI generates a response

The response is spoken aloud using Windows Text-to-Speech

Example
🎙️ Recording for 5 seconds... Speak now
🗣️ You said: What is Artificial Intelligence?
🤖 AI Assistant: Artificial Intelligence is the ability of machines to perform tasks
that normally require human intelligence.
🔊 Speaking response...

## Common Issues & Fixes

Microphone Not Working
Ensure microphone access is enabled in Windows settings

Try plugging in a headset

Permission Errors
Ensure AWS credentials are correctly set

Ensure the IAM user has access to:

Amazon Transcribe

Amazon Bedrock

S3 PutObject on the workshop bucket

## Learning Outcomes

By completing this exercise, you will understand:

How speech interfaces work in AI systems

How AWS services are combined in real applications

How to design lightweight, reliable AI pipelines

## Next

Proceed to Exercise-3, where we will introduce Retrieval-Augmented Generation (RAG).

