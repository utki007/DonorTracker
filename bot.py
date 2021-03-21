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

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

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


@bot.command()
async def displayembed(ctx):
	"""Embed Example"""
	embed= discord.Embed(
		title = 'title',
		description = 'this is a description.',
		colour = discord.Colour.blue()
	)

	embed.set_footer(text='this is a footer')
	embed.set_image(url='https://cdn.discordapp.com/avatars/301657045248114690/b5bb4614040fefbb7e8c4126f5badc75.png?size=256')
	embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/794601058860793859.png?v=1')
	embed.set_author(name='Utkarsh Narain',icon_url='https://cdn.discordapp.com/emojis/807430397260202024.gif?v=1')
	embed.add_field(name='heading 1',value='vwb fwebfu fewb',inline=False)
	embed.add_field(name='heading 1',value='vwb fwebfu fewb',inline=True)
	embed.add_field(name='heading 1',value='vwb fwebfu fewb',inline=True)

	await ctx.send(embed=embed)


@bot.command('kick a user')
async def kick(ctx,member: discord.Member, *,reason=None):
	await member.kick(reason=reason)

@bot.command('ban a user')
async def unban(ctx,*,member):
	banned_users = await ctx.guild.bans()
	member_name,number_discriminator =member.split('#')

	for ban_entry in banned_users:
		user = ban_entry.user

		if(user.name,user.discriminator) == (member_name,number_discriminator):
			await ctx.guild.unban(user)
			await ctx.send(f'Unbanned! {user.mention}')
			return




bot.run('ODEwMDQxMjYzNDUyODQ4MTc5.YCd3tw.gJALdEngQ9WLwzNbHGdhADiFuWU')
