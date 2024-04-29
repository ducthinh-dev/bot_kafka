import os
from dotenv import load_dotenv
import discord
from datetime import datetime

from utils import Ninjas


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
ninjas = Ninjas()


@client.event
async def on_ready():
    print(f"{get_current()} {client.user} on duty 🫡")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("/hello"):
        print(f"{get_current()} {message.author} said hello")
        await message.channel.send("Hello!")

    if message.content.startswith("/jokes"):
        print(f"{get_current()} {message.author} said jokes")
        res = ninjas.jokes()
        if res.status_code == 200:
            reply = res.json()[0]["joke"]
        else:
            reply = "Oops, there was an error 🥲"
        await message.channel.send(reply)


def get_current():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


load_dotenv()
TOKEN = os.environ.get("SLOTH_TOKEN")
client.run(TOKEN)
