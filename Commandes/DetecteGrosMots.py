import discord

client = discord.Client()

motsinterdits = ["putain","pute","fdp","con","connard"] # Liste de mots interdits

@client.event
async def on_ready():
	print("Bot connecté !")

@client.event
async def on_message(message):
	args = message.content.split(" ")
	for mot in args:
		if mot in motsinterdits:
			await message.channel.send("Warn !")
			return

client.run("<Token>")
