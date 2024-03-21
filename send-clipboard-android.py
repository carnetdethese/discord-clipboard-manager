from cryptography.fernet import Fernet
import sys
import requests
import utilities

token = utilities.encrypt(bytes(sys.argv[1]), utilities.key)

url = f'https://discord.com/api/webhooks/{utilities.webhook_id}/{utilities.webhook_token}' # Url of Discord channel.
data = {'content': token.decode()}
headers = {"Content-Type": "application/json"} 
response = requests.post(url, headers=headers, json=data)