# importing the required libraries
# importing the required libraries
import discord
from discord.ext import commands
import random
import time
import os
import pymongo
import dns
import pandas as pd
import numpy as np

description = '''This is what I have been programmed to do'''
bot = commands.Bot(command_prefix='?', description=description,)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(aliases=['pong'],description='ping the bot mofo')
async def ping(ctx):
	"""Bot Is dead"""
	await ctx.send(f'Pong! {round(bot.latency*1000)}ms')

bot.run(os.environ['BOT_TOKEN'])
# bot.run('ODEwMDQxMjYzNDUyODQ4MTc5.YCd3tw.gJALdEngQ9WLwzNbHGdhADiFuWU')
