# bot.py
# Importing packages
import os
import discord
import random
import time
import asyncio

from discord.ext import commands
from dotenv import load_dotenv

# loading .env file to obtain bot token
load_dotenv()
token = os.getenv('DISCORD_TOKEN')
server = os.getenv('DISCORD_GUILD')

# Creates client
client = discord.Client()

# Global ver of for annie's ID
annieId = 416352129897463819

# TODO want to implement background function for one discord that will assgin roles every 30 mins
# to a rank based of the users credit value

# TODO what is left for the credit system is to figure out a way to store and track the credit
# values of all users, this could be done by haveing a folder with text or json files that keep
# the user info of every indiviual user based on user ID

# TODO to implement a kick counter and such there might be a on_user_leave or smth similar
# to on_new_user for the client that we can override to implement will also need a way to track this
# could be similar to the way for credit

# TODO other things to implement are prob minigames, dailies
# NOTE: dailies will give user currency (jr. Chickens) and they can 'obtain' more credit
# User can also user currency to gamble at the 'fair' games


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
    
# Function used to check the sent message and assign score value based on contents of message
# If certain phrased is detected then the person will either gain or lose points
def checkMessage(str message)
    score = 0
    authorizedUsers = {176024137330982912}
    negativePhrases = {}
    postivePhrase = {}
    manualScore = {'rej.drift'}

    # checks for if a 'banned' phrase was said
    for response in negativePhrases:
        if response in message.content:
            score -= 5
    
    # checks for if a 'good' phrase was said
    # should modify so user can only gain x amount of points per day
    # while points user can lose in infinite
    for response in postivePhrase:
        if response in message.content:
            score += 5

    # checks for maunal update of phrase
    # TODO for maunal updates must have bot check if authorized user is using it
    # TODO this might be bad since the manual trigger will need a target
    # implementing this only for rej.drift
    for response in manualScore:
        # This might be incorrect syntax
        if message.author.id in authorizedUsers:
            if response in message.content:
                score -= 10

    return score



client.run(token)