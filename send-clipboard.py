#!/usr/bin/env python3
import sys
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_dir)
import pyperclip
import requests
import secret_vars

# Encrypting the clipboard before sending it to Discord.
token = secret_vars.encrypt(bytes(pyperclip.paste(), "UTF-8"), secret_vars.key)

url = f'https://discord.com/api/webhooks/{secret_vars.webhook_id}/{secret_vars.webhook_token}'
data = {'content': token.decode()}
headers = {"Content-Type": "application/json"}
response = requests.post(url, headers=headers, json=data)


