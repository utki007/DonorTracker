# importing the required libraries
import discord
from discord.ext import commands
import random
import time

description = '''This is what I have been programmed to do'''

intents = discord.Intents.default()
intents.members = False

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command(aliases=['pong'],description='ping the bot mofo')
async def ping(ctx):
	"""Bot Is dead"""
	await ctx.send(f'Pong! {round(bot.latency*1000)}ms')

@bot.command(aliases=['clear'])
async def purge(ctx,amount=5):
	await ctx.channel.purge(limit=amount+1)

@bot.command()
async def say(ctx,text: str):
	await ctx.channel.purge(limit=1)
	await ctx.send(text)




bot.run('ODEwMDQxMjYzNDUyODQ4MTc5.YCd3tw.gJALdEngQ9WLwzNbHGdhADiFuWU')
