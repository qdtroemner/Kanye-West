import discord
from discord.ext import commands
from discord.ext.commands.core import command

import requests
import io

from deps import kanye_secrets as secrets
from deps import spotify
from deps import this_x_does_not_exist
from random import choice, random

class This_X_Does_Not_Exist(commands.Cog, name="This X Does Not Exist"):
	def __init__(self, bot):
		self.bot = bot
		self.spotify_client = spotify.Spotify()
		self.ZERO_WIDTH_SPACE = "​"

	#@commands.cog.listener()

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

	@commands.command(aliases=['arte', 'painting'])
	async def art(self, ctx):
		async with ctx.typing():
			image_data = this_x_does_not_exist.generate_art()
			await ctx.send(file=discord.File(fp=image_data, filename="art.jpg"))
	
	@commands.command(aliases=['horsie'])
	async def horse(self, ctx):
		async with ctx.typing():
			image_data = this_x_does_not_exist.generate_horse()
			await ctx.send(file=discord.File(fp=image_data, filename="art.jpg"))

def setup(bot):
	bot.add_cog(This_X_Does_Not_Exist(bot))