import boto3
import time
import json
import sounddevice as sd
import scipy.io.wavfile as wav
import uuid
import os
from datetime import datetime
import pyttsx3
import urllib.request

# =================================================
# CONFIGURATION
# =================================================
REGION = "us-east-1"
MODEL_ID = "us.amazon.nova-lite-v1:0"
BUCKET_NAME = "applied-ai-workshop-audio"   # must exist
RECORD_SECONDS = 5
SAMPLE_RATE = 16000
LOCAL_AUDIO_FILE = "input.wav"

# Optional student identifier (prevents S3 collision)
STUDENT_ID = os.environ.get("STUDENT_ID", "unknown-student")
# =================================================

# AWS clients
bedrock = boto3.client("bedrock-runtime", region_name=REGION)
transcribe = boto3.client("transcribe", region_name=REGION)
s3 = boto3.client("s3", region_name=REGION)

# Local TTS engine (Windows)
tts_engine = pyttsx3.init()
tts_engine.setProperty("rate", 175)

# =================================================
# STEP 1: RECORD AUDIO
# =================================================
print("\n🎙️ Recording for 5 seconds... Speak now")

audio = sd.rec(
    int(RECORD_SECONDS * SAMPLE_RATE),
    samplerate=SAMPLE_RATE,
    channels=1
)
sd.wait()
wav.write(LOCAL_AUDIO_FILE, SAMPLE_RATE, audio)

print("✅ Recording complete")

# =================================================
# STEP 2: UPLOAD AUDIO TO S3 (NO COLLISION)
# =================================================
unique_id = uuid.uuid4().hex
timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")

s3_key = f"audio/{STUDENT_ID}/{timestamp}-{unique_id}.wav"

s3.upload_file(
    LOCAL_AUDIO_FILE,
    BUCKET_NAME,
    s3_key
)

media_uri = f"s3://{BUCKET_NAME}/{s3_key}"
print(f"☁️ Uploaded audio to S3: {s3_key}")

# =================================================
# STEP 3: TRANSCRIBE AUDIO
# =================================================
job_name = f"transcribe-{unique_id}"

transcribe.start_transcription_job(
    TranscriptionJobName=job_name,
    Media={"MediaFileUri": media_uri},
    MediaFormat="wav",
    LanguageCode="en-US"
)

print("🧠 Transcribing...")

while True:
    job = transcribe.get_transcription_job(
        TranscriptionJobName=job_name
    )
    status = job["TranscriptionJob"]["TranscriptionJobStatus"]

    if status in ["COMPLETED", "FAILED"]:
        break

    time.sleep(1)

if status == "FAILED":
    print("❌ Transcription failed")
    exit(1)

transcript_uri = job["TranscriptionJob"]["Transcript"]["TranscriptFileUri"]

with urllib.request.urlopen(transcript_uri) as f:
    transcript_json = json.loads(f.read())

user_text = transcript_json["results"]["transcripts"][0]["transcript"]
print(f"\n🗣️ You said: {user_text}")

# =================================================
# STEP 4: SEND TEXT TO NOVA LITE
# =================================================
system = [
    {"text": "You are a helpful AI assistant. Respond clearly and concisely."}
]

messages = [
    {"role": "user", "content": [{"text": user_text}]}
]

response = bedrock.converse(
    modelId=MODEL_ID,
    system=system,
    messages=messages,
    inferenceConfig={
        "maxTokens": 200,
        "temperature": 0.7,
        "topP": 0.9
    }
)

chunks = response["output"]["message"]["content"]
assistant_text = "".join(part.get("text", "") for part in chunks)

print(f"\n🤖 AI Assistant: {assistant_text}")

# =================================================
# STEP 5: LOCAL TEXT-TO-SPEECH (WINDOWS)
# =================================================
print("\n🔊 Speaking response...\n")
tts_engine.say(assistant_text)
tts_engine.runAndWait()

print("✅ Done")
