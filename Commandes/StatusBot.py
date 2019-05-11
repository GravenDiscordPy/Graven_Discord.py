import discord

client = discord.Client()

@client.event
async def on_ready():
	print("Bot connecté !")

@client.event
async def on_message(message):
	if message.content == '!deco':
		await client.change_presence(status=discord.Status("offline"))
  if message.content == '!co':
    await client.change_presence(status=discord.Status("online"))

client.run("<Token>")
