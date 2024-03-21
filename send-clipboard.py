#!/usr/bin/env python3
import sys
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_dir)
import pyperclip
import requests
import utilities

# Encrypting the clipboard before sending it to Discord.

if utilities.device == "android":
    token = utilities.encrypt(bytes(sys.argv[1]), utilities.key)
else:
    token = utilities.encrypt(bytes(pyperclip.paste(), "UTF-8"), utilities.key)

url = f'https://discord.com/api/webhooks/{utilities.webhook_id}/{utilities.webhook_token}'
data = {'content': token.decode()}
headers = {"Content-Type": "application/json"}
response = requests.post(url, headers=headers, json=data)



