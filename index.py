from selfcord import Client
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

client = Client()

@client.event
async def on_ready():
    print(f"Logado como {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user and message.content == "!ping":
        await message.channel.send("Pong!")

client.run(token, bot=False)
