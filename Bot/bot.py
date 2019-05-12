import discord
from random import choice
import json

client = discord.Client()


load = open("prefix.json","r")
prefix = json.loads(load.read())
load.close()
listeimages=[""]
motsinterdits = [""]

@client.event
async def on_ready():
	print("Bot connecté !")
  
@client.event
async def on_message(message):
	try: pref = prefix[str(message.guild.id)]
	except: pref = "!"
	args = message.content.lower().split(" ")
	for mot in args:
		if mot in motsinterdits:
			await message.channel.send("Warn !")
			return
	if not (len(args[0]) > len(pref) and pref == args[0][:len(pref)]): return
	else:
		comm = args.pop(0)[len(pref):]

		if comm == "help":
			await message.channel.send(embed=discord.Embed(title="Help",colour=discord.Colour.from_rgb(174,244,254),description="info\nPurge\nPrefix\nHug\nAvatar\nKick\nBan\nPseudo"))
		
		if comm == "info":
			await message.channel.send(embed=discord.Embed(title="Infos",colour=discord.Colour.from_rgb(174,244,254),description='Nom : ' + client.user.name + "\nID : " + str(client.user.id) + "\nPréfix : " + pref).set_image(url=client.user.avatar_url))
		
		if comm == "quit":
			await client.logout()

		if comm == "purge":
			if message.author.guild_permissions.manage_messages:
				if len(args) > 0 and args[0].isdigit():
					await message.channel.purge(limit=int(args[0])+1)
					await message.channel.send(content=args[0] + " messages supprimés !",delete_after=5)
				else:
					await message.channel.send("Veuillez mettre un nombre !")
			else:
				await message.channel.send("Vous n'avez pas les permissions !")

		if comm == "prefix":
			if message.author.guild_permissions.administrator:
				if len(args) > 0:
					prefix[str(message.guild.id)] = args[0]
					load = open("prefix.json","w")
					load.write(json.dumps(prefix))
					load.close()
					await message.channel.send("Préfix changé pour : " + args[0])
				else:
					await message.channel.send("Veuillez mettre un préfix !")
			else:
				await message.channel.send("Vous n'avez pas les permissions !")

		if comm == "hug":
			if len(message.mentions) > 0:
				await message.channel.send(content=message.author.mention + " fait un câlin à " + message.mentions[0].mention,file=discord.File(choice(listeimages)))

		if comm == "avatar":
			if len(message.mentions) > 0: perso = message.mentions[0]
			else: perso = message.author
			await message.channel.send(embed=discord.Embed(title=perso.name,colour=discord.Colour.from_rgb(174,244,254)).set_image(url=perso.avatar_url))

		if comm == "kick":
			if message.author.guild_permissions.administrator:
				if len(message.mentions) > 0:
					if message.mentions[0].dm_channel == None:
						await message.mentions[0].create_dm()
					await message.mentions[0].dm_channel.send("Vous avez été kické du serveur " + message.guild.name)
					await message.mentions[0].kick()
			else:
				await message.channel.send("Vous n'avez pas les permissions !")

		if comm == "ban":
			if message.author.guild_permissions.administrator:
				if len(message.mentions) > 0:
					if message.mentions[0].dm_channel == None:
						await message.mentions[0].create_dm()
					await message.mentions[0].dm_channel.send("Vous avez été banni du serveur " + message.guild.name)
					await message.mentions[0].ban()
			else:
				await message.channel.send("Vous n'avez pas les permissions !")

		if comm == "pseudo":
			if message.author.guild_permissions.administrator:
				if len(message.mentions) > 0 and len(args) > 1:
					await message.mentions[0].edit(nick=" ".join(message.content.split(" ")[2:]))
					await message.delete()
					await message.channel.send(content="Pseudo de " + message.mentions[0].name + " changé pour " + message.mentions[0].nick,delete_after=5)
			else:
				await message.channel.send("Vous n'avez pas les permissions !")

client.run("<Token>")
