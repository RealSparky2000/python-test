import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os 

Client = discord.Client ()
client = commands.bot(command_prefix='m.')
@client.event
async def on_ready() :
     print("Bot has been launched!")
     await client.change_presence(game=discord.Game(name="New me on Python"))
    
@client.event
async def on_message(message) :
  if message.content.startswith('m.python') :
  message = 'Yeah, i have been launched on Python 3.6.7 (discord.py)'.format(message)
  await client.send_message(message.channel, message)
  
  client.run(os.getenv(SECRET))
  
