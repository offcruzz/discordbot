import discord
from discord.ext import commands
from discord.ext.commands.core import command 
from discord.utils import get
from random import randrange
import asyncio
import json
from datetime import date
from discord.ext import tasks
from itertools import cycle

with open('config.json', 'r') as f:
    config = json.loads(f.read())
    token = config['token']
    prefix = config['prefix']
client = commands.Bot(command_prefix = prefix)

status = cycle(['discord.gg/race', 'Developed by cruzz#5071'])

@client.event 
async def on_ready():
    change_status.start()
    print('Bot by cruzz#5071 \n')
    print('Bot online!\n') 
    print(f'Nome: {client.user}\n') 

@tasks.loop(seconds=40)
async def change_status():
  await client.change_presence(status=discord.Status.dnd,activity=discord.Game(next(status)))

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

@client.event 
async def on_message(message):
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
            if 'https' in message.content.lower() and len(message.content.lower()) >= 35:
                await message.add_reaction('<a:checkcria:851528307035734047>')
                await message.add_reaction('<a:no:853287194855866388>')
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

@client.command()
async def renovar(ctx):
    guild = ctx.guild
    roleID = 764970354661654559
    serverowner = get(guild.roles, id=roleID)
    userID = 438833835107680257
    cruzz = await client.fetch_user(userID)
    msg = await ctx.channel.send(f'Olá {ctx.author.mention} <a:yeah:853284163590684672>\n'
    'Seu pedido de renovação foi enviado com sucesso! <a:fun:853284209707057182>\n'
    f'Aguarde ate que um {serverowner.mention} entre em contato com você!\n'
    f'Essa mensagem será deletada em 30 segundos <a:runing:853343341864681502>')

    await cruzz.send(f'Olá {cruzz.mention} <a:yeah:853284163590684672>\n'
    f'O membro {ctx.author.mention} solicitou a renovação do plano de divulgação <a:fun:853284209707057182>\n'
    'Entre em contato o mais rápido possivel <a:yeah:853284163590684672>')

    await asyncio.sleep(30)
    
    await ctx.message.delete()

    await msg.delete()

@client.command()
async def encerrar(ctx):
    guild = ctx.guild
    roleID = 764970354661654559
    serverowner = get(guild.roles, id=roleID)
    userID = 438833835107680257
    cruzz = await client.fetch_user(userID)
    msg = await ctx.channel.send(f'Olá {ctx.author.mention} <a:yeah:853284163590684672>\n'
    'Seu pedido de finalização da divulgação foi enviado com sucesso! <a:fun:853284209707057182>\n'
    f'Aguarde ate que um {serverowner.mention} entre em contato com você!\n'
    f'Essa mensagem será deletada em 30 segundos <a:runing:853343341864681502>')

    await cruzz.send(f'Olá {cruzz.mention} <a:yeah:853284163590684672>\n'
    f'O membro {ctx.author.mention} solicitou o cancelamento do plano de divulgação <a:fun:853284209707057182>\n'
    'Entre em contato o mais rápido possivel <a:yeah:853284163590684672>')

    await asyncio.sleep(30)

    await ctx.message.delete()

    await msg.delete()

@client.command()
async def stop(ctx, membro : discord.Member):
    if ctx.author.guild_permissions.ban_members:
        userID = 438833835107680257
        cruzz = await client.fetch_user(userID)
        re = await ctx.channel.send(f'Olá {ctx.author.mention}\n'
        'A divulgação foi encerrada com sucesso <a:fun:853284209707057182>\n'
        'Iniciando o processo de exclusão desse canal em 30 segundos <a:sad:853284248692981822>')

        await asyncio.sleep(30)

        await ctx.message.delete()

        await re.edit(content= ('Excluindo o canal <a:runing:853343341864681502> '))

        await asyncio.sleep(15)

        await ctx.channel.delete()

        await membro.send(f'Olá {membro.mention} <a:yeah:853284163590684672>\n'
        f'Seu canal de divulgação foi encerrado com sucesso conforme solicitado <a:sad:853284248692981822>\n'
        f'Caso ache que isso seja um engano, contate o {cruzz.mention} <a:fun:853284209707057182>')

@client.command()
async def erroid(ctx, membro : discord.Member):
    suporte = client.get_channel(839215821808861184)
    
    await membro.send(f'Olá {membro.mention} <a:yeah:853284163590684672>\n'
    f'Está com problemas para liberar seu ID? <a:sad:853284248692981822>\n'
    f'Abra um ticket em {suporte.mention}  <a:runing:853343341864681502>')
    
    resp = await ctx.channel.send(f'Olá {ctx.author.mention} <a:yeah:853284163590684672>\n'
    f'A mensagem de erro de id foi enviada com sucesso para {membro.mention}! <a:checkcria:851528307035734047>\n')
    f'Irei deletar minha mensagem em 10 segundos! <a:runing:853343341864681502>'
    
    await asyncio.sleep(10)
        
    await resp.delete()    

@client.command()
async def start(ctx, membro : discord.Member, mes=None, *,day=None):
    logs = client.get_channel(854093350004064326)
    guild = ctx.guild
    roleID = 764970354661654559
    serverowner = get(guild.roles, id=roleID)
    hj = date.today()
    data = date(2021, int(mes), int(day))
    futuro = date.fromordinal(data.toordinal()-1) 

    first = await ctx.channel.send(f'{ctx.author.mention} Recebendo os dados inseridos <a:runing:853343341864681502>')

    await asyncio.sleep(7)

    await first.edit(content= f'{ctx.author.mention}\n'
    'Ano Inserido:<a:seta:853284272395124766> 2021\n'
    f'Mês Inserido:<a:seta:853284272395124766> {mes}\n'
    f'Dia Inserido:<a:seta:853284272395124766> {day}')

    await asyncio.sleep(10)

    await first.delete()

    await ctx.message.delete()

    await logs.send(f'Olá {serverowner.mention} <a:yeah:853284163590684672>\n'
    f'O plano de divulgação do membro: {membro.mention} iniciou hoje dia {hj} <a:fun:853284209707057182>\n'
    'Fiquem atentos a quantidade de everyone e dias de duração! <a:runing:853343341864681502>')

    while True:
        if hj == futuro:
            await ctx.author.send(f'Olá {ctx.author.mention}\n'
                                  f'Falta apenas um dia para o final do plano de divulgação do membro {membro.mention}')
        else:
            print(f'{client.user} Ainda não é dia de avisar aos {serverowner.mention}')
       
        if data == hj:
            await membro.send(f'Olá {membro.mention} <a:yeah:853284163590684672>\n'
            f'Seu plano de divulgação em Race Ultimate chegou ao fim <a:sad:853284248692981822>\n'
            f'Caso queria renovar, digite .renovar em seu canal de divulgação! <a:checkcria:851528307035734047>\n'
            f'Caso não queira renovar, digite .encerrar em seu canal de divulgação! <a:no:853287194855866388>\n'
            f'Essa mensagem é automatica, caso ache que isso é um erro, contate o {ctx.author.mention} <a:fun:853284209707057182>')

            await ctx.author.send(f'Olá {ctx.author.mention} <a:yeah:853284163590684672>\n'
            f'O plano de divulgação do {membro.mention} chegou ao fim <a:sad:853284248692981822>\n'
            f'Aguarde a decisão do {membro.mention} para ver o que deve ser feito! <a:fun:853284209707057182>')
            break
        else:
            print(f'{client.user} diz: Ainda não é dia de encerrar a divulgação! :)')

            await asyncio.sleep(86400)

client.run(token)
