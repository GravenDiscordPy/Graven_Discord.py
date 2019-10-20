import discord

client = discord.Client()

@client.event
async def on_ready():
	print("Bot connecté !")
  
@client.event
async def on_raw_reaction_add(payload):

    message_id = payload.message_id           # recuperer l'ID du message qui reçoit la réation


    if message_id == 634732408016601186:      # verifier que c'est bien le message que l'on veut
                                    
        if payload.emoji.name == "✅":
            role_id = 634732495849521163      # recuperer l'ID du role
        elif payload.emoji.name == "❌":
            role_id = 634732552342601740
        else:
            print("Pas de correspondance")

        guild_id = payload.guild_id           # recuperer l'ID du serveur
        guild = client.get_guild(guild_id)    # recuperer le serveur à partir de l'ID

        user_id = payload.user_id             # recuperer l'ID de l'user
        member = guild.get_member(user_id)    # recuperer le membre à partir de l'ID de l'user

        role = guild.get_role(role_id)        # recuperer le role à partir de l'ID du role

        await member.add_roles(role)

        

@client.event
async def on_raw_reaction_remove(payload):    # exactement la même chose
                                              # à part qu'il faut enlever le role au lieu de l'ajouter

    message_id = payload.message_id


    if message_id == 634732408016601186:
        
        if payload.emoji.name == "✅":
            role_id = 634732495849521163
        elif payload.emoji.name == "❌":
            role_id = 634732552342601740
        else:
            print("Aucun role ne correspond à cet emoji")
            print(payload.emoji.name)

        guild_id = payload.guild_id
        guild = client.get_guild(guild_id)
        user_id = payload.user_id
        member = guild.get_member(user_id)
        role = guild.get_role(role_id)

        await member.remove_roles(role)     # <------------ remove_roles() au lieu de add_roles()

client.run("<Token>")