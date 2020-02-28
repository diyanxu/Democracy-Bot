# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
server = os.getenv('DISCORD_GUILD')

client = discord.Client()



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
    toxic = {':(', ':frowning:', ':sob:', ':c', ':C', ':cry:', ':triumph:', '>:c', '>:C', ':angry:'}
    
    print(message.content)
    for response in toxic:
        if message.content == response:
            await message.channel.send('Stop being toxic!')

client.run(token)