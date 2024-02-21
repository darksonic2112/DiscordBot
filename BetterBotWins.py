# bot.py
import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.all()
intents.typing = True
intents.presences = True
intents.members = True

client = discord.Client(intents=intents)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '99!':
        print('Triggered the 99! condition')
        brooklyn_99_quotes = [...]
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException
@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

bot.run(TOKEN)