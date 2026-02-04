# Indus AI Week

## Applied AI on AWS — Indus AI Week

Hands-on AI Training for Future Engineers
Powered by INIT  (AWS Official Partner)

## 📌 About This Repository

This repository contains the official hands-on lab material for the
“Applied AI on AWS” training delivered during Indus AI Week.

The training is designed for final-year Computer Science students and focuses on practical, real-world use of Generative AI on AWS, not theory alone.

All exercises are:

✅ Beginner-friendly

✅ Production-inspired

✅ AWS-native

✅ Non-commercial & educational

## 🎯 Training Objectives

By completing these labs, participants will learn:

How modern AI assistants are built using AWS Bedrock

How voice interfaces work using Speech-to-Text

How enterprises use Retrieval-Augmented Generation (RAG)

How AI systems are designed safely and realistically

This training emphasizes clarity, simplicity, and correct architecture.

## 🧠 Learning Path (Progressive)

The repository is structured into three hands-on exercises, each building on the previous one.
```bash
indusai/
├── Exercise-1/
├── Exercise-2/
├── Exercise-3/
└── README.md
```


These credentials will be provided to you during the session (via printed QR code).
## 📱➡️💻 How to Tranfer Printed QR Data from Mobile to PC (Using CopyPaste.me)

The AWS credentials are provided via a printed QR code.
Follow the steps below exactly to transfer the scanned data from your mobile phone to your PC.

### 1️⃣ Scan the Printed QR Code

Use your mobile phone camera or any QR scanner app
Scan the printed QR code provided to you
The QR code contains encoded text data (credentials)

### 2️⃣ Copy the Scanned Data on Your Phone

After scanning, the QR scanner will show text content
Select all the text
Copy it to your phone’s clipboard

### 3️⃣ Open CopyPaste.me on Your PC/ Laptop

Open your browser
Go to:
https://copypaste.me
The website will open a QR Code interface
Scan the QR on the copypaste.me
This will open the same website on your phone 

### 4️⃣ Paste the QR Data into CopyPaste.me
Tap on the Text input field
Paste the copied QR code data
Click the Send button


### 5️⃣ Retrieve the Data on Your PC

The text you sent from your phone will now appear on the PC screen
Copy the text from the PC browser
Paste it into a Notepad to be used in command terminal 

## 🔐 AWS Credentials Setup (Windows Command Prompt)
### Step 1️⃣ Open Command Prompt

Press Win + R
Type cmd
Press Enter

### Step 2️⃣ Set AWS Environment Variables

Copy the values from your QR code and run the following commands
(replace values with your own):
```bash
set AWS_ACCESS_KEY_ID=YOUR_ACCESS_KEY_HERE
set AWS_SECRET_ACCESS_KEY=YOUR_SECRET_KEY_HERE
set AWS_DEFAULT_REGION=us-east-1
```

#### ⚠️ Important Notes

Do NOT wrap values in quotes

These variables apply to the current Command Prompt window only

If you close the window, you must set them again

### Step 3️⃣ Verify AWS Credentials

Run:
```bash
aws sts get-caller-identity
```

If credentials are correct, you will see output similar to:

Account: xxxxxxxxxxxx
Arn: arn:aws:iam::xxxxxxxxxxxx:user/ai-student-01

## 🧪 Python Virtual Environment Setup (Recommended)

Using a virtual environment keeps your system clean and avoids conflicts.

### Step 1️⃣ Navigate to the Project Folder
cd applied-ai-on-aws

### Step 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
```

This creates a folder named venv.

### Step 3️⃣ Activate the Virtual Environment
```bash
venv\Scripts\activate
```

You should see:

(venv) C:\path\to\applied-ai-on-aws>

### Step 4️⃣ Install Dependencies

Run this inside each exercise folder:

pip install -r requirements.txt

### Step 5️⃣ Run the Exercises

Example:

cd Exercise-1
python bedrock_conversational_assistant.py

### ❌ Common Issues & Fixes
'python' is not recognized

Python is not added to PATH
Reinstall Python and check Add Python to PATH

## Python Libraries (to be installed via pip)

```bash
pip install boto3 sounddevice scipy pyttsx3 numpy
```
## 🧪 Exercises Overview
### 🔹 Exercise 1 — Text-Based AI Assistant

Goal: Build a conversational AI using Amazon Bedrock (Nova Lite)

You will:

Interact with a Large Language Model (LLM)

Understand prompts and conversation context

Tune inference parameters

📁 Folder: Exercise-1/

### 🔹 Exercise 2 — Voice AI Assistant

Goal: Add voice interaction to your AI assistant

You will:

Speak to the AI using your microphone

Convert speech to text using Amazon Transcribe

Generate spoken responses using local system TTS

Experience a real voice-enabled AI pipeline

📁 Folder: Exercise-2/

### 🔹 Exercise 3 — Mini RAG (Knowledge AI)

Goal: Build a document-aware AI assistant

You will:

Load local documents

Create embeddings using Titan Text Embeddings v2

Perform similarity search

Generate answers grounded in your own data

📁 Folder: Exercise-3/

## ☁️ AWS Services Used

This training uses the following AWS services, exactly as they are used in real projects:

Amazon Bedrock

Nova Lite (Text Generation)

Titan Text Embeddings v2

Amazon Transcribe (Speech-to-Text)

No infrastructure management, no vector databases, no heavy frameworks —
the focus is on core AI concepts.

## 🔐 AWS Credentials & Security

AWS credentials are provided only for the duration of the session

Permissions are strictly limited

No participant needs:

An AWS account

A credit card

Console access

All usage is temporary, controlled, and educational.

## 🧑‍🎓 Intended Audience

Final-year Computer Science students

AI / ML beginners

Students exploring careers in:

Cloud Computing

Artificial Intelligence

Software Engineering

## 🎓 About Indus AI Week

Indus AI Week is a govt-driven initiative aimed at:

Spreading AI awareness

Building practical skills

Preparing youth for the future of technology

This repository is part of that mission.

##  🏢 About INIT

INIT is a software company and is an AWS Official Partner delivering:

Cloud & AI solutions

Enterprise platforms

Industry-focused AI systems

This training is provided purely for educational and awareness purposes.

## 📣 Acknowledgements

Some concepts and inspiration are drawn from:

Industry best practices

Public research

Community contributions in the AI ecosystem

##  🚀 How to Get Started

### 👉 Start with Exercise-1/README.md
Follow exercises in order for the best learning experience.

### 📬 Contact & Follow-up

Participants may receive:

Slides

Additional learning resources

Further reading material

via the communication channels (Please fill in the google form: https://forms.gle/SwV415hehPbvd3u1A ) .

## ⭐ Final Note

The goal of this training is not to turn you into an AI expert in one day —
but to give you the confidence to build, explore, and learn responsibly.

#Happy learning 🚀
