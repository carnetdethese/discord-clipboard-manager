import discord
import utilities
import yaml
import pyperclip

with open("config.yaml") as f:
    cfg = yaml.load(f, Loader=yaml.FullLoader)

device = cfg['device']

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):

    if message.author == client.user:
        print("Clipboard received from MacOs.") if device == "android" else print("Clipboard received from Android.")

        token = bytes(message.content, "UTF-8")
        decodedMessage = utilities.decrypt(token, utilities.key).decode()

        utilities.setClipboardAndroid(decodedMessage) if device == "android" else pyperclip.copy(decodedMessage)
        return
    
    print("Message received, but not from the right user.")

@bot.command()
async def delete_all(ctx):
    if ctx.author.id == utilities.discord_user:
        # Fetch messages from the channel and delete them
        async for message in ctx.channel.history(limit=None):
            await message.delete()
        await ctx.send("All messages have been deleted.")
    else:
        await ctx.send("You don't have permission to use this command.")

client.run(utilities.discord_token)

