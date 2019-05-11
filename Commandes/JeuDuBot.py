import discord

client = discord.Client()

prefix = ["!"]

@client.event
async def on_ready():
	print("Bot connecté !")
	await client.change_presence(activity=discord.Game(name="!help")) # La description du bot sera "Joue à !help"

# Cette partie est si l'on souhaite changer le jeu auquel joue le bot
# Conseil : Ne mettez pas de commande pour changer le jeu, car cela change le jeu du bot sur tout les serveurs ou il est
@client.event
async def on_message(message):
	args = message.content.split(" ")
	if args[0] == prefix[0] + "jeu":
		if len(args) > 1:
			await client.change_presence(activity=discord.Game(name=args[1]),status=discord.Status("offline"))
			await message.channel.send("Jeu changé pour : " + args[1])
		else:
			await message.channel.send("Veuillez mettre un jeu !")

client.run("<Token>")
