import discord
client = discord.Client()

prefix = ["+"]

@client.event
async def on_ready():
	print("Bot connecté !")

@client.event
async def on_message(message):
	args = message.content.split(" ")
	if args[0] == prefix[0] + 'infos':
		await message.channel.send('Infos : \nNom : ' + client.user.name + "\nID : " + str(client.user.id) + "\nPréfix : " + prefix[0])
	if args[0] == prefix[0] + "prefix":
		if len(args) > 1:
			prefix[0] = args[1]
			await message.channel.send("Préfix changé pour : " + args[1])
		else:
			await message.channel.send("Veuillez mettre un préfix !")
client.run("<Token>")
