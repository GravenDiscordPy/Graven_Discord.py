import discord 
from discord.ext import commands

bot = commands.Bot(commands.when_mentioned_or('.'))

@bot.command(pass_context=True)
async def ping(ctx):
    await ctx.message.channel.send("pong !")

#Voici une commande basique /\ /\ 
#Nous allons voir comment transformé le simple message par un embed 

@bot.command(pass_context=True)
async def ping(ctx):
    e = discord.Embed #on assigne un embed a une variable
    await ctx.message.channel.send("pong !")

###########################################

@bot.command(pass_context=True)
async def ping(ctx):
    e = discord.Embed(title="Pong", description="!!!!!!") #Voici comment ajoute un titre et une descrption
    await ctx.message.channel.send("pong !")

###########################################

@bot.command(pass_context=True)
async def ping(ctx):
    e = discord.Embed(title="Pong", description="!!!!!!")
    await ctx.message.channel.send(embed=e)# On dit qu'on envoie une embed et que l'emebed est 'e' (la variable)
    
###########################################

#Embed avancé
@bot.command(pass_context=True)
async def infos(ctx):
    e = discord.Embed(title="Infos",colour=discord.Colour.from_rgb(174,244,254),description='Nom : ' + client.user.name + "\nID : " + str(client.user.id) + "\nPréfix : " + prefix[0]).set_image(url=client.user.avatar_url)
    await ctx.message.channel.send(embed=e)
    #Embed avec un titre, une description, une couleur et une image

bot.run("<Token>")
