import discord
from dotenv import load_dotenv
import os
import re
import random

def add_repititions(s: str) -> str:
    input = list(s)
    rep_idxs = [m.start() for m in re.finditer('\*', s)]

    if len(rep_idxs) == 0:
        return s

    for i in rep_idxs:
        input[i] = ""
        input += input[i - 1] * random.randint(0, 10)
    
    return ''.join(input)

greetings =  [
    "welcome*",
    "hai*",
    "hello*",
    "hi*hi*",
    "hi*",
    "hi*e*",
]

emotions = [
    "^.^",
    "!*",
    ":3",
    ">:3",
]


load_dotenv()
                
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

    # TODO: Once discord.py has application emoji support
    # emotions.append([i if i.available else None for i in client.emojis])

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    

client.run(os.getenv('DISCORD_BOT_TOKEN'))