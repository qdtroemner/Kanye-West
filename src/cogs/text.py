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

class Text(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.spotify_client = spotify.Spotify()
		self.ZERO_WIDTH_SPACE = "​"

	#@commands.cog.listener()
	@commands.command()
	async def quote(self, ctx):
		url = "https://api.kanye.rest/?format=text"
		req = requests.get(url)
		if req.status_code == 200:
			await ctx.send(req.text)

	@commands.command(aliases=["yetrack", "ys", "yt"])
	async def yesong(self, ctx):
		await ctx.send("Searching...")
		search_url = "https://api.spotify.com/v1/search"
		#"Bearer " + 
		headers = {}#"Authorization": secrets.SPOTIFY}
		parameters = {
			"q": "Kanye West",
			"type": "track",
			"limit": 50
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

	@commands.command(aliases=['l'])
	async def lyrics(self, ctx, *, arg):
		await ctx.send("Searching...")
		data = _lyrics.get_lyrics(arg)
		if not data or data is None:
			await ctx.send("Trouble getting info.")
		(lyrics, title, artist, genius_url, album_cover) = data
		pfp_url = ctx.author.avatar_url

		embed = discord.Embed(title=title, description=artist, url=genius_url, colour=discord.Colour.from_hsv(random(), 1, 1))
		for verse in lyrics:
			embed.add_field(name=self.ZERO_WIDTH_SPACE, value=verse, inline=False)
		if album_cover is not None:
			embed.set_image(url=album_cover)
		embed.set_thumbnail(url=pfp_url)
		try:
			await ctx.send(embed=embed)
		except discord.errors.HTTPException as http_error:
			print(http_error)
			await ctx.send("Something went wrong. The lyrics are most likely too long.")

	@commands.command(aliases=['qlyrics', 'ql'])
	async def quicklyrics(self, ctx, *, arg):
		await ctx.send("Searching...")
		data = _lyrics.get_lyrics(arg, get_full_info=False)
		if not data or data is None:
			await ctx.send("Trouble getting info.")
		(lyrics, title, artist) = data
		pfp_url = ctx.author.avatar_url

		embed = discord.Embed(title=title, description=artist, colour=discord.Colour.from_hsv(random(), 1, 1))
		for verse in lyrics:
			embed.add_field(name=self.ZERO_WIDTH_SPACE, value=verse, inline=False)
		embed.set_thumbnail(url=pfp_url)
		try:
			await ctx.send(embed=embed)
		except discord.errors.HTTPException as http_error:
			print(http_error)
			await ctx.send("Something went wrong. The lyrics are most likely too long.")

	@commands.command(aliases=['giphy'])
	async def gif(self, ctx, *, arg):
		data = gif.search_gifs(arg)
		if not data or data is None:
			await ctx.send("Trouble getting gifs.")
		(gif_url, title) = data
		pfp_url = ctx.author.avatar_url

		embed = discord.Embed(title=title, colour=discord.Colour.from_hsv(random(), 1, 1))
		embed.set_image(url=gif_url)
		embed.set_thumbnail(url=pfp_url)
		await ctx.send(embed=embed)
	
	"""
	@commands.command(aliases=['rtweet', 'rt'])
	async def randomtweet(self, ctx):
		data = tweets.get_recent_tweet()
		print(data)
		if not data or data is None:
			await ctx.send("Trouble getting tweets.")

		data = data['data']
		user_id = data['id']
		url = f"https://twitter.com/twitter/status/{user_id}"
		await ctx.send(url)
	"""

def setup(bot):
	bot.add_cog(Text(bot))