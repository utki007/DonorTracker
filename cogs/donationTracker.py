# importing the required libraries
import discord
from discord.ext import commands,tasks

class donationTracker(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Inside donationTracker')

    @commands.command()
    async def check(self,ctx):
	    "Bot Is dead"
	    await ctx.send(f'Pong!')





def setup(client):
    client.add_cog(donationTracker(client))