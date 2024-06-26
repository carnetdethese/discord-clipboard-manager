import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet
import requests
import yaml

# Loading secrets
load_dotenv()

webhook_id = os.getenv("WEBHOOK_ID")
webhook_token = os.getenv("WEBHOOK_TOKEN")
key = os.getenv("ENCRYPTION_KEY")
discord_user = int(os.getenv("DISCORD_USER"))
discord_token = os.getenv("DISCORD_TOKEN")
tasker_port = int(os.getenv("TASKER_PORT"))

no_permission = "You don't have permission to use this command."

with open("config.yaml") as f:
    cfg = yaml.load(f, Loader=yaml.FullLoader)

device = cfg['device']

# Encryption function using Fernet
def encrypt(message: bytes, key: bytes) -> bytes:
    return Fernet(key).encrypt(message)

# Decryption function.
def decrypt(token: bytes, key: bytes) -> bytes:
    return Fernet(key).decrypt(token)

def setClipboardAndroid(message):
    url = f'http://localhost:{tasker_port}/clipboard'  # Tasker's HTTP server endpoint - Tasker will then add the string to the clipboard on Android. TODO - find a better way to add it to the clipboard. Maybe using Termux API? 
    data = {'message': message}
    response = requests.post(url, json=data)
    return response

def sendingClipboard(token):
    url = f'https://discord.com/api/webhooks/{webhook_id}/{webhook_token}'
    data = {'content': token.decode()}
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, json=data)
    return response