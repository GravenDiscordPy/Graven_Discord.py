import discord

client = discord.Client()

prefix = ["!"]

@client.event
async def on_ready():
	print("Bot connecté !")
  
@client.event
async def on_message(message):
	args = message.content.split(" ")
  if args[0] == prefix[0] + 'del':
		await message.delete()
	if args[0] == prefix[0] + "purge":
		if len(args) > 1 and args[1].isdigit():
			await message.channel.purge(limit=int(args[1])+1)
		else:
			await message.channel.send("Veuillez mettre un nombre !")
      
client.run("<Token>")
