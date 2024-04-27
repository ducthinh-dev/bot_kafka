import os
from dotenv import load_dotenv
import discord


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@client.event
async def add_reaction(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.add_reaction('Hello!')

load_dotenv()
TOKEN = os.environ.get("SLOTH_TOKEN")
client.run(TOKEN)
