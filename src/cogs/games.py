import discord
from discord.ext import commands
from discord.ext.commands.core import command

import requests
from deps import kanye_secrets as secrets
from deps import spotify
from deps import lyrics as _lyrics
from deps import gif
from deps import tweets
from random import choice, random

import googlemaps

class Games(commands.Cog):
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

	@commands.command(aliases=['mp', 'streetview', 'sv'])
	async def map(self, ctx):
		pass

def setup(bot):
	bot.add_cog(Games(bot))