import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

from llm_client import getResponse

load_dotenv()
discTk = os.getenv('DISCORD_TOKEN')

#handler = logging.FileHandler(filename='rimuru.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
#rimuru = discord.Client(intents=intents)
rimuru = commands.Bot(command_prefix='--', intents=intents)

@rimuru.event
async def on_ready():
    print(f'bot on air -- {rimuru.user.name}')

@rimuru.event
async def on_message(message):
    if message.author == rimuru.user:
        return
    async with message.channel.typing():
        response = await getResponse(message.content, message.channel.id, message.author.display_name, message.author.id)
        await message.reply(response)

    await rimuru.process_commands(message)

@rimuru.command()
async def slime(ctx):
    await ctx.send("Hello! I'm rimuru the slime, a discord bot created by König Adler.")
    await ctx.send("I am just a prototype in development used to test features and mechanics...")

rimuru.run(discTk)#, log_handler=handler, log_level=logging.DEBUG)