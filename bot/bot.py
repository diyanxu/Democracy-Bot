# bot.py
import os
import discord
import random

from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
token = os.getenv('DISCORD_TOKEN')
server = os.getenv('DISCORD_GUILD')


bot = commands.Bot(command_prefix = '.')
client = discord.Client()

@bot.command(name = 'flip')
async def coin_flip(message):
    number = random.randint(0, 100)
    if number == 0 or number == 100:
        await message.channel.send('The coin landed on it\'s side, How unfortunate you owe me $1000')
    elif number <= 51:
        await message.channel.send('The coin landed on Heads')
    else:
        await message.channel.send('The coin landed on Tails')

# First active function once bot starts
@client.event
async def on_ready():

    # Initial console message to display connected
    print(f'{client.user} has connected to Discord!')

    # Checks all connected server and lists all members in givne server
    # TODO: This is printing to get info will need to be removed later
    for guild in client.guilds:
        print(f'{client.user} has connected to ' + guild.name + ', Server ID is: ' + str(guild.id))
        print('Members in server are: ')
        for member in guild.members:
            print(' - ' + member.name)


# First replay to message command
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    # TODO: This is currently hard coded should change so it reads from a file
    # This DOES NOT work with emotes which is big problem
    toxic = {':(', ':frowning:', ':sob:', ':c', ':C', ':cry:', ':triumph:', '>:c', '>:C', ':angry:'}
    
    print("Messaged typed: " + message.content)
    for response in toxic:
        if message.content == response:
            await message.channel.send('Stop being toxic!')

bot.run(token)
client.run(token) 