import os
import discord
from discord.ext import commands

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Bot online")

@bot.event
async def on_member_join(member):
    if len(member.roles) == 1:
        await member.kick(reason="Everyone only")

bot.run(TOKEN)