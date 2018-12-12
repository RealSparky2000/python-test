import discord
from discord.ext import commands

TOKEN = process.env.SECRET

client = commands.Bot(command_prefix = 'm.')

@client.event
async def on_ready():
    print ("Bot Is Ready!")

client.run(TOKEN)