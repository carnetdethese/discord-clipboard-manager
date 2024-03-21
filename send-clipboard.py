#!/usr/bin/env python3
import sys
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_dir)
import pyperclip
import utilities

# Encrypting the clipboard before sending it to Discord.

if utilities.device == "android":
    token = utilities.encrypt(bytes(sys.argv[1]), utilities.key)
else:
    token = utilities.encrypt(bytes(pyperclip.paste(), "UTF-8"), utilities.key)

response = utilities.sendingClipboard(token)
