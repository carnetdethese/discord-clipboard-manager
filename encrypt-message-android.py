from cryptography.fernet import Fernet
import sys
import requests
import secret_vars

token = secret_vars.encrypt(bytes(sys.argv[1]), secret_vars.key)

url = f'https://discord.com/api/webhooks/{secret_vars.webhook_id}/{secret_vars.webhook_token}' # Url of Discord channel.
data = {'content': token.decode()}
headers = {"Content-Type": "application/json"} 
response = requests.post(url, headers=headers, json=data)