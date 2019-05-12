import discord

client = discord.Client()

@client.event
async def on_ready():
	print("Bot connecté !")

@client.event
async def on_message(message):
  if message.content == "!infos":
    if len(message.mentions) > 0:
      await message.channel.send("Son pseudo est " + message.mentions[0].name)
      
client.run("<Token>")
