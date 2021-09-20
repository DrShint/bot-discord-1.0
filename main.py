import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True

testing = False

client = commands.Bot(command_prefix = "!", case_insensitive = True, intents=intents)

client.remove_command('help')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming('Developed by: 𝔻𝕣. 𝕊𝕙𝕚𝕟𝕥'))
    print('Bot is ready.')

client.run('TOKEN')
