# importing the required libraries
import discord
from discord.ext import commands, tasks
import os
import pandas as pd
import numpy as np
import pymongo
import dns
import time
import asyncio


class donationTracker(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.a = "loser"
        self.myclient = pymongo.MongoClient(
            'mongodb+srv://utki009:Utkarsh2697@cluster0.5wndm.mongodb.net/TGK?retryWrites=true&w=majority')
        self.mydb = self.myclient['TGK']
        self.mycol = self.mydb["donorBank"]

    @commands.Cog.listener()
    async def on_ready(self):
        # Send a nice message
        print(f'donobank loaded')

    @commands.command()
    async def adono(self,ctx, member: discord.Member, amount: int):

        # if ctx.author.guild_permissions.administrator:
        myquery = {"_id": member.id}
        info = self.mycol.find(myquery)
        flag = 0
        dict = {}
        for x in info:
            dict = x
            flag = 1

        if flag == 0:
            await self.create_donor(member)
            newvalues = {"$set": {"bal": amount}}
        else:
            newvalues = {"$set": {"bal": dict["bal"]+amount}}
            dict["bal"] = dict["bal"]+amount

        # updating the value
        self.mycol.update_one(myquery, newvalues)
        await ctx.message.add_reaction("<a:tick:823850808264097832>")

        # showing donor balance
        self.bal = "bal"
        display = discord.Embed(
            title=f"__{member.name} Donator Bank__",
            description=f"{member.mention} has added {amount:,} to their donor balance. thanks for your dono.  \n\n"
                        f"{member.mention} Total Donation **{dict[self.bal]:,}** \n",
            colour=member.colour
        )

        display.set_footer(
            text=f"{self.client.user.name} | Developed by utki007 and Jay", icon_url=self.client.user.avatar_url)

        await ctx.send(embed=display)


        # for logging
        logg = discord.Embed(
            title="__Gambler's Kingdom Logging Registry__",
            description=f"{ctx.author.mention} added **{amount:,}** to {member.mention} bal [here]({ctx.message.jump_url})",
            colour=ctx.author.colour
        )

        logg.set_footer(
            text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url)

        channel = self.client.get_channel(823601745002496000)
        await channel.send(embed=logg)




        

    async def create_donor(self,user):
        dict = {}
        dict["_id"] = user.id
        dict["name"] = user.name
        dict["bal"] = 0
        self.mycol.insert_one(dict)

def setup(client):
    client.add_cog(donationTracker(client))
