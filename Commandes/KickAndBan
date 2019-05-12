import discord

client = discord.Client()

@client.event
async def on_ready():
	print("Bot connecté !")

@client.event
async def on_message(message):
  if message.content == "!kick":
		if len(message.mentions) > 0:
			await message.mentions[0].kick()

	if message.content == "!ban":
		if len(message.mentions) > 0:
			await message.mentions[0].ban()
      
client.run("<Token>")
