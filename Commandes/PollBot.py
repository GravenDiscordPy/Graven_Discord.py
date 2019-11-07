import discord 
from discord.ext import commands

bot = commands.Bot(commands.when_mentioned_or('.'))

@bot.event
async def on_ready():
    print("Bot connecté")

@bot.command()  
async def help_poll(ctx):
    embed_help_poll = discord.Embed(title='Aimez vous ce bot ?', description=':one:  Enormement\n\n:two:  Bien\n\n:three:  Moyen\n\n:four:  Bof\n\n:five:  Vraiment pas ouf')
    await ctx.message.channel.send('Voici comment faire un sondage:\n```.poll "Votre question" Nombre de choix (Max  9) "Un choix" "Un autre" "Encore un"```\nExemple :\n`.poll "Aimez vous ce bot ?" 5 "Enormement" "Bien" "Moyen" "Bof" "Vraiment pas ouf"`', embed=embed_help_poll)

@bot.command()
async def poll(ctx, question, nb_choice, *choices):

    emojis = [":one:", ":two:", ":three:", ":four:", ":five:", ":six:", ":seven:", ":eight:", ":nine:"]  # les emojis de 1 à 9
    choices = list(choices)
    final_choice = ''
    for i in range(int(nb_choice)):
        final_choice = final_choice + emojis[i] + '  ' + choices[i] + '\n' + '\n'

    embed = discord.Embed(title=question, description=final_choice)
    await ctx.message.channel.send('Etes vous satisfait ?', embed=embed)


bot.run("<Token>")