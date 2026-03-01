import os
import discord
from discord.ext import commands

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user} online!")


@bot.event
async def on_member_remove(member):
    try:
        await member.send(
"""You have been removed from the server for v4n1ty protection. If you want to tr4de, enter this server .

https://t.me/darkbring
https://discord.gg/rRN9X8RjfB"""
        )
    except:
        print("DM göndərilə bilmədi.")


bot.run(TOKEN)