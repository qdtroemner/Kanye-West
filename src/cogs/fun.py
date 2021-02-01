import discord
from discord.ext import commands
from discord.ext.commands.core import command

import requests
import io

from deps import kanye_secrets as secrets
from deps import earthview
from deps import spotify
from deps import this_x_does_not_exist
from random import choice, random

class Fun(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.spotify_client = spotify.Spotify()
		self.ZERO_WIDTH_SPACE = "​"

	#@commands.cog.listener()
	"""
	@commands.command(aliases=['ping-pong', 'pp', 'playpong'])
	async def pingpong(self, ctx, * arg):
		if arg and arg is not None:
			direction = # match nearest to direction string
	"""

	@commands.command(aliases=['googleearth', 'map', 'world'])
	async def earth(self, ctx):
		await ctx.send(earthview.get_random_earthview())

	@commands.command(aliases=['person', 'tpdne'])
	async def human(self, ctx):
		async with ctx.typing():
			image_data = this_x_does_not_exist.generate_person()
			await ctx.send(file=discord.File(fp=image_data, filename="human.jpg"))
	
	@commands.command(aliases=['apartment', 'house', 'building'])
	async def rental(self, ctx):
		async with ctx.typing():
			image_data = this_x_does_not_exist.generate_rental()
			await ctx.send(file=discord.File(fp=image_data, filename="rental.jpg"))

	@commands.command(aliases=['gato', 'kitten'])
	async def cat(self, ctx):
		async with ctx.typing():
			image_data = this_x_does_not_exist.generate_cat()
			await ctx.send(file=discord.File(fp=image_data, filename="cat.jpg"))

def setup(bot):
	bot.add_cog(Fun(bot))