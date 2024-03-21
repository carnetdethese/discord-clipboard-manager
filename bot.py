import discord
from discord.ext import commands
import utilities
import pyperclip

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

print(utilities.discord_user)

@bot.command()
async def delete_all(ctx):
    if ctx.author.id == int(utilities.discord_user):
        async for message in ctx.channel.history(limit=None):
            await message.delete()
        await ctx.send("All messages have been deleted.")
    else:
        await ctx.send(utilities.no_permission)

    print(ctx.author.id)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user and message.content != utilities.no_permission:
        print("Clipboard received from MacOs.") if utilities.device == "android" else print("Clipboard received from Android.")

        token = bytes(message.content, "UTF-8")
        decodedMessage = utilities.decrypt(token, utilities.key).decode()

        utilities.setClipboardAndroid(decodedMessage) if utilities.device == "android" else pyperclip.copy(decodedMessage)
        return
    
    print("Message received, but not from the right user.")
    
    await bot.process_commands(message)

bot.run(utilities.discord_token)

