import boto3
from botocore.config import Config

# -------------------------------------------------
# Bedrock client (Nova Lite)
# -------------------------------------------------
client = boto3.client(
    "bedrock-runtime",
    region_name="us-east-1",
    config=Config(
        read_timeout=3600,
        connect_timeout=3600,
        retries={"max_attempts": 1}
    )
)

MODEL_ID = "us.amazon.nova-lite-v1:0"

# -------------------------------------------------
# System prompt (assistant behavior)
# -------------------------------------------------
system = [
    {"text": "You are an AI assistant. Keep answers clear, concise, and helpful."}
]

# -------------------------------------------------
# Conversation memory
# -------------------------------------------------
messages = []

# -------------------------------------------------
# Inference config
# -------------------------------------------------
inference_config = {
    "maxTokens": 300,
    "temperature": 0.7,
    "topP": 0.9
}

print("\n?? AI Assistant (Powered by Amazon Nova Lite)")
print("Type 'exit' or 'quit' to end the conversation.\n")

# -------------------------------------------------
# Conversation loop
# -------------------------------------------------
while True:
    user_input = input("You: ").strip()

    if user_input.lower() in ["exit", "quit"]:
        print("\nAI Assistant: Goodbye ??\n")
        break

    # Add user message to conversation
    messages.append({
        "role": "user",
        "content": [{"text": user_input}]
    })

    # Call Bedrock Converse API
    response = client.converse(
        modelId=MODEL_ID,
        system=system,
        messages=messages,
        inferenceConfig=inference_config
    )

    # Extract assistant response
    chunks = response["output"]["message"]["content"]
    assistant_text = "".join(part.get("text", "") for part in chunks)

    # Print response
    print("\nAI Assistant:", assistant_text, "\n")

    # Add assistant reply to conversation memory
    messages.append({
        "role": "assistant",
        "content": [{"text": assistant_text}]
    })

