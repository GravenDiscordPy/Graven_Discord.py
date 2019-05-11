import discord 
from discord.ext import commands
bot = commands.Bot(commands.when_mentioned_or('.'))

@bot.event
async def on_ready():
	print("Bot Connecté")

@bot.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()
    await ctx.message.channel.send("Connection au salon vocal !")

@bot.command(pass_context=True)
async def leave(ctx):
	try:
		await ctx.message.guild.voice_client.disconnect()
		await ctx.message.channel.send("Déconnection du salon vocal !")
	except:
		return await ctx.message.channel.send("Je ne suis connecté à aucun salon vocal !")
    
#On as toujours pas trouvé comment lui faire lire de la musique sans installer des trucs bizarres

bot.run("<Token>")
