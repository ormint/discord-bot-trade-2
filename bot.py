import os
import discord
from discord.ext import commands
import asyncio

# TOKEN Railway Variables-dən gəlir
TOKEN = os.getenv("TOKEN")

# INTENTS
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


# BOT ONLINE
@bot.event
async def on_ready():
    print(f"{bot.user} online!")
    bot.loop.create_task(keep_alive())


# SERVERƏ GİRƏNİ KICK
@bot.event
async def on_member_join(member):
    await asyncio.sleep(5)

    if len(member.roles) == 1:
        await member.kick(reason="Everyone only")


# RAILWAY SÖNDÜRMƏSİN DEYƏ
async def keep_alive():
    while True:
        await asyncio.sleep(300)


# BOT START
bot.run(TOKEN)