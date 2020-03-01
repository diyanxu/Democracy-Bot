# bot.py
import os
import discord
import random
import time
import asyncio

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
server = os.getenv('DISCORD_GUILD')

client = discord.Client()
annieId = 416352129897463819

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
    # Try catch to open file and log messages
    print(message.content)
    try:
        with open("msg_log.txt", "a") as f:
            f.write(f"User: {message.author}, Message: {message.content}, Time: {int(time.time())}\n")
            print("Message logged")
    except Exception as e:
        print(e)


    # TODO: This is currently hard coded should change so it reads from a file
    # This DOES NOT work with emotes which is big problem
    toxic = {':(', '😦', '😭', ':c', ':C', '😢', '😤', '>:c', '>:C', '😠', 'fortnite'}

    # Checks if annie is the user
    if message.author.id == annieId:
        for response in toxic:
            if response in message.content:
                await message.channel.send(f'Stop being toxic!')
                break

client.run(token)