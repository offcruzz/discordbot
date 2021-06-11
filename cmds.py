import discord
from discord.ext import commands
from discord.ext.commands.core import command 
import random
from random import randrange
import asyncio
import secret

token = secret.token()
prefix = secret.prefix()
client = commands.Bot(command_prefix = prefix)

@client.event 
async def on_ready():
    activity = discord.Game(name='discord.gg/race  ',type=3)
    await client.change_presence(status=discord.Status.dnd, activity=activity)
    print('Bot by cruzz#5071 \n')
    print('Bot online!\n') 
    print(f'Nome: {client.user}\n') 

@client.command()
async def kick(ctx, membro : discord.Member, *,motivo=None):
    if ctx.author.guild_permissions.kick_members:
     canal = client.get_channel(id=765013430142238750)
     msg = f'{ctx.author.mention} expulsou {membro.mention} por {motivo}'
     await membro.send(f'Você foi kickado do servidor pelo motivo {motivo}')
     await membro.kick()
     await canal.send(msg)

@client.command()
async def ban(ctx, membro : discord.Member, *,motivo=None):
    if ctx.author.guild_permissions.ban_members:
     canal = client.get_channel(id=765013430142238750)
     msg = f'{ctx.author.mention} baniu {membro.mention} por {motivo}'
     await membro.send(f'Você foi banido do servidor pelo motivo {motivo}')
     await membro.ban()
     await canal.send(msg) 

@client.command()
async def crias(message):
    var = randrange(4)
    if var == 1:
        await message.channel.send('CRUS CV CRIA \n'
        'https://media.discordapp.net/attachments/728284661393915956/848009389180190780/unknown.png')
    if var == 2:
        await message.channel.send('ROBS CV CRIA \n'
        'https://cdn.discordapp.com/attachments/728284661393915956/848009704156168212/Screenshot_20210528-222742_PicsArt.jpg')
    if var == 3:
        await message.channel.send('BUTOLHOS CV CRIA \n'
        'https://media.discordapp.net/attachments/728284661393915956/847999933062578196/Screenshot_20210528-214657_PicsArt-min_1.jpg?width=679&height=676')

@client.event  #erro id comando
async def on_message(message):
    if message.content.lower().startswith("!erroid"):
        suporte = client.get_channel(839215821808861184)
        
        msgre = await message.reply(f'Está com erro para liberar seu ID? Abra um ticket em {suporte.mention}\n'
        'Deletando essa mensagem em 20 segundos <a:loading:852902244680073246>')

        await asyncio.sleep(20)

        await msgre.delete()

        await message.delete()

    if message.content.lower().startswith("!infopvp"):
        comandos = client.get_channel(766425223560953856)

        inf = await message.channel.send(f'{message.author.mention} /pvp 1 (Pistolas)\n'
        '/pvp 2 (Fuzil)\n'
        '/pvp 3 (Pistolas e Fuzis)\n'
        'após dar o comando você vai ser redirecionado para o mundo de pvp\n'
        'Para sair é só dar /pvp off\n'
        f'Mais informações em {comandos.mention} \n'
        'Deletando essa mensagem em 30 segundos <a:loading:852902244680073246>')

        await asyncio.sleep(30)

        await inf.delete()

        await message.delete()

    if message.author != client.user:
        if (message.channel.id == 764980720556572673):
            if 'https' in message.content.lower():
                print('ok')
            else:
                print(f'{message.author} tentou mandar mensagem sem link no canal de sugestoes de carros!')
                
                warn = await message.reply('Neste canal só é permitido mandar links!\n'
                'Mande apenas o link do veículo que você deseja sugerir!\n'
                'Essa mensagem será deletada em 20 segundos <a:loading:852902244680073246>')
                
                await asyncio.sleep(20)
                
                await message.delete()
                
                await warn.delete() 

    await client.process_commands(message)

client.run(token)