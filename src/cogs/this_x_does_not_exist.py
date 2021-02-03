import discord
from discord.ext import commands
from discord.ext.commands.core import command

from deps import spotify

import requests
from io import BytesIO

class This_X_Does_Not_Exist(commands.Cog, name="This X Does Not Exist"):
	def __init__(self, bot):
		self.bot = bot
		self.spotify_client = spotify.Spotify()
		self.ZERO_WIDTH_SPACE = "​"

	#@commands.cog.listener()
	async def x_does_not_exist(self, ctx, url, name):
		async with ctx.typing():
			req = requests.get(url)
			image_data = BytesIO(req.content)
			await ctx.send(file=discord.File(fp=image_data, filename=name))

	@commands.command(aliases=['person', 'tpdne'])
	async def human(self, ctx):
		await self.x_does_not_exist(ctx, "https://thispersondoesnotexist.com/image", "human.jpg")
	
	@commands.command(aliases=['apartment', 'house', 'building'])
	async def rental(self, ctx):
		await self.x_does_not_exist(ctx, "https://thisrentaldoesnotexist.com/img-new/hero.jpg", "rental.jpg")

	@commands.command(aliases=['gato', 'kitten'])
	async def cat(self, ctx):
		await self.x_does_not_exist(ctx, "https://thiscatdoesnotexist.com/", "cat.jpg")

	@commands.command(aliases=['arte', 'painting'])
	async def art(self, ctx):
		await self.x_does_not_exist(ctx, "https://thisartworkdoesnotexist.com/", "art.jpg")
	
	@commands.command(aliases=['horsie'])
	async def horse(self, ctx):
		await self.x_does_not_exist(ctx, "https://thishorsedoesnotexist.com/", "horse.jpg")

	"""@commands.command(aliases=['town'])
	async def city(self, ctx):
		await x_does_not_exist(ctx, "http://thiscitydoesnotexist.com/", "city.jpg")
		
	@commands.command(aliases=['automobile'])
	async def car(self, ctx):
		await x_does_not_exist(ctx, "https://www.thisautomobiledoesnotexist.com/", "car.jpg")"""

def setup(bot):
	bot.add_cog(This_X_Does_Not_Exist(bot))