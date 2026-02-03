# Exercise 1 - Text-Based AI Assistant (Amazon Bedrock)

## Objective

In this exercise, you will build and run a **text-based conversational AI assistant** using **Amazon Bedrock** with the **Nova Lite** model.

This exercise introduces:

- How to call a foundation model on AWS
- How conversational context is maintained
- How prompt design affects AI responses

This is the foundation for later exercises (Voice AI and RAG).

---

## Architecture Overview

User (Text Input)
↓
Amazon Bedrock (Nova Lite)
↓
AI Response (Text)

---

## Prerequisites

### 1. Python Version

Ensure Python **3.10 or later** is installed.

Check:

```bash
python --version
### 2. AWS Credentials
You must have AWS credentials configured as environment variables:

AWS_ACCESS_KEY_ID

AWS_SECRET_ACCESS_KEY

AWS_DEFAULT_REGION=us-east-1

(These credentials will be provided during the training.)

## Installation
Install required Python packages:

pip install -r requirements.txt
## How to Run
From the Exercise-1 directory:

python bedrock_conversational_assistant.py
## How It Works
You type a question or prompt

The input is sent to Amazon Bedrock

The Nova Lite model generates a response

The conversation context is preserved

The AI replies back in text

## Example Interaction
🤖 AI Assistant (Powered by Amazon Nova Lite)

You: What is Artificial Intelligence?
AI Assistant: Artificial Intelligence is the ability of machines to perform tasks
that normally require human intelligence, such as learning and problem-solving.

You: Give a real-life example
AI Assistant: A common example is recommendation systems used by Netflix or YouTube.
Type exit or quit to end the conversation.

## Things to Try (Hands-On)
Change the system prompt to alter the assistant’s behavior

Modify temperature to make responses more creative

Ask follow-up questions to see how context is retained

## Learning Outcomes
By completing this exercise, you will understand:

How to interact with an LLM using AWS Bedrock

How conversational AI maintains context

How prompt parameters affect model output

## Next Step
Proceed to Exercise-2, where you will add voice interaction (Speech-to-Text) to the assistant.
```
