import discord
from discord.ext import commands
import pyperclip
import secret_vars

# Discord Bot

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.author.name == "android":
        print("Clipboard received from Android device.")
        token = bytes(message.content, "UTF-8")
        decodedMessage = secret_vars.decrypt(token, secret_vars.key).decode()
        pyperclip.copy(decodedMessage)
        return

    print("Message received, but not from the right user.")

    await bot.process_commands(message)

@bot.command()
async def delete_all(ctx):
    if ctx.author.id == secret_vars.discord_user:
        # Fetch messages from the channel and delete them
        async for message in ctx.channel.history(limit=None):
            await message.delete()
        await ctx.send("All messages have been deleted.")
    else:
        await ctx.send("You don't have permission to use this command.")

bot.run(secret_vars.discord_token)
