import discord
from discord.ext import commands
from discord.ext.commands.core import command

import requests
from deps import kanye_secrets as secrets
from deps import spotify
from random import choice, random, randint

class Music(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.spotify_client = spotify.Spotify()
		self.ZERO_WIDTH_SPACE = "​"

	#@commands.cog.listener()

	def random_query(self):
		chars = "abcdefghijklmnopqrstuvwxyz0123456789."
		return choice(list(chars))

	@commands.command(aliases=["yetrack", "ys", "yt"])
	async def yesong(self, ctx):
		async with ctx.typing():
			search_url = "https://api.spotify.com/v1/search"
			headers = {}
			parameters = {
				"q": "Kanye West",
				"type": "track",
				"offset": randint(0, 2000)
			}
			data = self.spotify_client.get(search_url, headers=headers, params=parameters)
			tracks = data['tracks']['items']
			track = choice(tracks)

			name = track['name']
			artists = track['artists']
			artist_name = ""
			for artist in artists:
				if artist != artists[-1]:
					artist_name += artist['name'] + "; "
				else:
					artist_name += artist['name']
			album = track['album']['name']
			album_url = track['album']['external_urls']['spotify']
			album_cover = track['album']['images'][0]['url']
			track_url = track['external_urls']['spotify']
			thumbnail = ctx.author.avatar_url

			embed = discord.Embed(title=name, description=artist_name, url=track_url, colour=discord.Colour.from_hsv(random(), 1, 1))
			embed.set_image(url=album_cover)
			embed.set_author(name=album, url=album_url)
			#embed.set_thumbnail(url=thumbnail)
		await ctx.send(embed=embed)

	@commands.command(aliases=["rsong", "rs", "rt", "randomtrack"])
	async def randomsong(self, ctx):
		async with ctx.typing():
			search_url = "https://api.spotify.com/v1/search" 
			headers = {}
			parameters = {
				"q": self.random_query(),
				"type": "track",
				"offset": randint(0, 2000)
			}
			data = self.spotify_client.get(search_url, headers=headers, params=parameters)
			tracks = data['tracks']['items']
			track = choice(tracks)

			name = track['name']
			artists = track['artists']
			artist_name = ""
			for artist in artists:
				if artist != artists[-1]:
					artist_name += artist['name'] + "; "
				else:
					artist_name += artist['name']
			album = track['album']['name']
			album_url = track['album']['external_urls']['spotify']
			album_cover = track['album']['images'][0]['url']
			track_url = track['external_urls']['spotify']
			thumbnail = ctx.author.avatar_url

			embed = discord.Embed(title=name, description=artist_name, url=track_url, colour=discord.Colour.from_hsv(random(), 1, 1))
			embed.set_image(url=album_cover)
			embed.set_author(name=album, url=album_url)
			#embed.set_thumbnail(url=thumbnail)
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Music(bot))