import discord
from discord.ext import commands
from discord.flags import Intents
import os

intents = discord.Intents.all()
intents.members = True

lista_ban = ()
testing = False

client = commands.Bot(command_prefix = "!", case_insensitive = True, intents=intents)

client.remove_command('help')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

#Possivel sistema de ban
'''@commands.command(name='ban')
async def ban(ctx, coisa):
    user = ctx.message.mentions[0]
    if user.name in lista_ban:
        if ctx.message.author.name in lista_ban[user.name]:
            await ctx.message.channel('Você já votou!')
        else:
            get_list = lista_ban[user.name]
            get_list.append(ctx.message.author.name)
            lista_ban[user.name] = get_list
            await ctx.message.channel.send(f'Voto computado com sucesso! Ban **{user.name}** **{len(lista_ban[user.name])}/5**')
            await ctx.message.channel.send(lista_ban)
            if len(lista_ban[user.name]) >= 5:
                await ctx.message.channel.send(f'O **{user.name}** foi banido com sucesso!')
                await user.kick()
    else:
        lista_ban[user.nam] = [context.message.author.name]
        await ctx.message.channel.send(f'Voto computado com sucesso! Ban **{user.name}** **1/5**')'''    

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming('Developed by: 𝔻𝕣. 𝕊𝕙𝕚𝕟𝕥'))
    print(client.guilds)
    print('Bot online.')

client.run('TOKEN')
