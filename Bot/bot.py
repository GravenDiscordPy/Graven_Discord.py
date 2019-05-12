import discord
from random import choice

client = discord.Client()

prefix = ["!"]
listeimages=[""]

@client.event
async def on_ready():
	print("Bot connecté !")
  
@client.event
async def on_message(message):
	args = message.content.split(" ")
	if not (len(args[0]) > len(prefix[0]) and prefix[0] == args[0][:len(prefix[0])]): return
	else:
		comm = args.pop(0)[len(prefix[0]):]

		if comm == "info":
			await message.channel.send(embed=discord.Embed(title="Infos",colour=discord.Colour.from_rgb(174,244,254),description='Nom : ' + client.user.name + "\nID : " + str(client.user.id) + "\nPréfix : " + prefix[0]).set_image(url=client.user.avatar_url))
		
		if comm == "quit":
			await client.logout()

		if comm == "purge":
			if message.author.guild_permissions.manage_messages:
				if len(args) > 0 and args[0].isdigit():
					await message.channel.purge(limit=int(args[0])+1)
				else:
					await message.channel.send("Veuillez mettre un nombre !")
			else:
				print("Vous n'avez pas les permissions !")

		if comm == "prefix":
			print(dir(message.author.guild_permissions))
			if message.author.guild_permissions.administrator:
				if len(args) > 0:
					prefix[0] = args[0]
					await message.channel.send("Préfix changé pour : " + args[0])
				else:
					await message.channel.send("Veuillez mettre un préfix !")
			else:
				print("Vous n'avez pas les permissions !")

		if comm == "hug":
			if len(message.mentions) > 0:
				await message.channel.send(content=message.author.mention + " fait un câlin à " + message.mentions[0].mention,file=discord.File(choice(listeimages)))

client.run("<Token>")
