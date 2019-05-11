import discord 
from discord.ext import commands
bot = commands.Bot(commands.when_mentioned_or('.'))

@bot.event
async def on_ready():
	print("Bot Connecté")

@bot.command(pass_context=True)
async def ping(ctx):
    await ctx.message.channel.send("pong !")
    
client.run("<Token>")

#Ou

import discord
client = discord.Client()

@client.event
async def on_ready():
	print("Bot connecté !")

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	if message.content == '!infos':
		await message.channel.send('Infos : \nNom : ' + client.user.name + "\nID : " + str(client.user.id))
    
client.run("<Token>")
