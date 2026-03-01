import os
import discord
from discord.ext import commands

# TOKEN Railway Variables-dən gəlir
TOKEN = os.getenv("TOKEN")

print("TOKEN:", TOKEN)  # yoxlama üçün

# Intentlər
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Bot açıldı
@bot.event
async def on_ready():
    print(f"{bot.user} online!")

# Serverə girənləri kick edir
@bot.event
async def on_member_join(member):
    if len(member.roles) == 1:
        await member.kick(reason="Everyone only")

# BOTU BAŞLAT
bot.run(TOKEN)