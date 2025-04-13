import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# Carregar as variáveis do arquivo .env
load_dotenv()

# Obter o token do Discord a partir do arquivo .env
token = os.getenv('DISCORD_TOKEN')

# Criação do cliente Discord
client = discord.Client()

@client.event
async def on_ready():
    print(f'Logado como {client.user}')

@client.event
async def on_message(message):
    if message.content == "!ping":
        await message.channel.send("Pong!")

# Rodar o bot (self bot) com bot=False
client.run(token, bot=False)
