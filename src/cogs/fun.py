import discord
from discord.ext import commands
from discord.ext.commands.core import command

import requests
import io

from deps import kanye_secrets as secrets
from deps import earthview
from deps import spotify
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

def setup(bot):
	bot.add_cog(Fun(bot))