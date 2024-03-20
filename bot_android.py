import discord
import requests
import secret_vars

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.author.name == "mac":
        print("Clipboard received from Mac.")
        token = bytes(message.content, "UTF-8")
        decodedMessage = secret_vars.decrypt(token, secret_vars.key).decode()
        url = f'http://localhost:{secret_vars.tasker_port}/clipboard'  # Replace with Tasker's HTTP server endpoint - Tasker will then add the string to the clipboard on Android. TODO - find a better way to add it to the clipboard. Maybe using Termux API? 
        data = {'message': decodedMessage}
        response = requests.post(url, json=data)
        print(response) 
        return
    
    print("Message received, but not from the right user.")

client.run(secret_vars.discord_token)