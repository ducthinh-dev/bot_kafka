import os
from dotenv import load_dotenv
import discord

from utils import Ninjas


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
ninjas = Ninjas()


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("/hello"):
        await message.channel.send("Hello!")


@client.event
async def on_jokes(message):
    if message.author == client.user:
        return

    if message.content.startswith("/jokes"):
        res = ninjas.jokes()
        if res.status_code == 200:
            reply = res.json()[0]["joke"]
        else:
            reply = "Oops, there was an error 🥲"
        await message.channel.send(reply)


load_dotenv()
TOKEN = os.environ.get("SLOTH_TOKEN")
client.run(TOKEN)
