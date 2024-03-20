import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet

# Loading secrets
load_dotenv()

webhook_id = os.getenv("WEBHOOK_ID")
webhook_token = os.getenv("WEBHOOK_TOKEN")
key = os.getenv("ENCRYPTION_KEY")
discord_user = os.getenv("DISCORD_USER")
tasker_port = os.getenv("TASKER_PORT")

# Encryption function using Fernet
def encrypt(message: bytes, key: bytes) -> bytes:
    return Fernet(key).encrypt(message)

# Decryption function.
def decrypt(token: bytes, key: bytes) -> bytes:
    return Fernet(key).decrypt(token)