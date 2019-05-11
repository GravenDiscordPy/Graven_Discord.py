import discord
from random import choice

listeimages = ["test.jpg","image.png"] #Les images doivent être dans le fichier, sinon "images/test.jpg" par exemple.

client = discord.Client()

@client.event
async def on_ready():
  print("Bot connecté !")

async def on_message(message):
	if message.author == client.user:
		return
	if message.content == '!image':
	  await message.channel.send(file=discord.File(choice(listeimages)))
	
client.run("<Token>")
