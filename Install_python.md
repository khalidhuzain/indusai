# 🧰 Python Installation (Windows – If Not Already Installed)

## Only required if Python is not installed on your system

### Step 1️⃣ Check if Python Is Already Installed

Open Command Prompt and run:
```bash
python --version
```

If you see something like:

Python 3.10.x


✅ You can skip the installation.

### Step 2️⃣ Download Python (If Not Installed)

Open your browser

Go to: https://www.python.org/downloads/windows/

Download Python 3.10 or later (64-bit)

⚠️ Do NOT download Python 2.x

### Step 3️⃣ Install Python (IMPORTANT)

Run the installer and MUST check this box:

☑ Add Python to PATH

Then click:

Install Now


Wait for installation to complete.

### Step 4️⃣ Verify Installation

Close Command Prompt, open it again, then run:
```bash
python --version
pip --version
```

You should see both Python and pip versions printed.

### Step 5️⃣ (Optional but Recommended) Upgrade pip
python -m pip install --upgrade pip

✅ After Python Installation

You are now ready to proceed with the exercises.

Next steps:
```bash
pip install -r requirements.txt
python bedrock_conversational_assistant.py
```
## ⚠️ Common Issues & Fixes
❌ 'python' is not recognized as an internal or external command

➡ Python was installed without adding to PATH

Fix:

Re-run the Python installer

Select Modify

Check Add Python to PATH

Finish and reopen Command Prompt

❌ Permission Errors

➡ Run Command Prompt as Administrator
