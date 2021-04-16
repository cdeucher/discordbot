# bot.py
import os
import discord
import requests
import json
import random
from dotenv import load_dotenv

load_dotenv()
_TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!meme':
        meme_number=random.randrange(1, 50)
        response   = requests.get("http://alpha-meme-maker.herokuapp.com/memes/"+str(meme_number))
        topText    = response.json()['data']['topText']
        bottonText = response.json()['data']['bottomText']
        image      = response.json()['data']['image']

        responsex  = requests.get("https://pt.wikipedia.org/wiki/Especial:Aleat%C3%B3ria")
        print(responsex.url)

        print(image)
        await message.channel.send(str(topText)+" \n "+" \n "+ responsex.url + " \n " +image)

client.run(_TOKEN)
