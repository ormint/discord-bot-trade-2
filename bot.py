import os
import discord
from discord.ext import commands
import asyncio

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Bot online")

@bot.event
async def on_member_join(member):
    await asyncio.sleep(6)

    if len(member.roles) == 1:
        await member.kick(reason="Everyone only")

async def keep_alive():
    while True:
        await asyncio.sleep(3600)

bot.loop.create_task(keep_alive())

bot.run(TOKEN)