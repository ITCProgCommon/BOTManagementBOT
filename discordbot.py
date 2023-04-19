import discord
from discord.ext import tasks, commands

intents = discord.Intents.default()

client = commands.Bot(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print(f"{client.user}でログインしました")


token = ""
client.run(token)
