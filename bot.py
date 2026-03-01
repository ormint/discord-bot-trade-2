import os
import discord
from discord.ext import commands

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user} online!")


@bot.event
async def on_member_remove(member):
    try:
        await member.send(
            "If you want to trade join this server https://discord.gg/rRN9X8RjfB"
        )
    except:
        print("DM closed or failed")


@bot.event
async def on_member_ban(guild, user):
    try:
        await user.send(
            "If you want to trade join this server https://discord.gg/rRN9X8RjfB"
        )
    except:
        print("DM closed or failed")


bot.run(TOKEN)