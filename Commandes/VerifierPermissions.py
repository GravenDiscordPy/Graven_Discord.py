import discord

client = discord.Client()

@client.event
async def on_ready():
	print("Bot connecté !")

# Permissions : 'add_reactions', 'administrator', 'all', 'all_channel', 'attach_files', 'ban_members', 'change_nickname'
# 'connect', 'create_instant_invite', 'deafen_members', 'embed_links', 'external_emojis', 'general', 'handle_overwrite'
# 'is_strict_subset', 'is_strict_superset','is_subset', 'is_superset', 'kick_members', 'manage_channels', 'manage_emojis'
# 'manage_guild', 'manage_messages', 'manage_nicknames', 'manage_roles', 'manage_webhooks', 'mention_everyone', 'move_members'
# 'mute_members', 'none', 'priority_speaker', 'read_message_history', 'read_messages', 'send_messages', 'send_tts_messages'
# 'speak', 'text', 'update', 'use_voice_activation', 'value', 'view_audit_log', 'voice'

@client.event
async def on_message(message):
	if message.content == "!admin":
		if message.author.guild_permissions.administrator:
			await message.channel.send("Vous êtes admin, bravo !")
		else:
			await message.channel.send("Vous n'avez pas les permissions !")
      
client.run("<Token>")
