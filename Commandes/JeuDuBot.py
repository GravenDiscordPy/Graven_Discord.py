import discord

client = discord.Client()

@client.event
async def on_ready():
	print("Bot connecté !")
	await client.change_presence(activity=discord.Game(name="!help")) # La description du bot sera "Joue à !help"
  
client.run("<Token>")
