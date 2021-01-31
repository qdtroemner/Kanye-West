import discord
from discord.ext import commands

from deps import kanye_secrets as secrets

INITIAL_EXTENTIONS = [
	'cogs.text',
	'cogs.fun'
]

class Client(commands.Bot):
	def __init__(self):
		super().__init__(
			command_prefix=("kanye ", "yeezus ", "ye ", "$"),
			case_insensitive=True,
			#intents=discord.Intents().all(),
			description="My greatest pain in life is that I will never be able to see myself perform live.",
			self_bot=False,
			owner_id=344429375489572865,
			activity=discord.Game(f"🏓 ping pong w/ CurtLiom")
		)

		for extension in INITIAL_EXTENTIONS:
			try:
				self.load_extension(extension) # Load the cog command groups
			except Exception as e:
				print(f'Failed to load extension {extension}. Because: {e}')

	async def on_ready(self):
		print(f"and I'm Kanye West!")
		# await self.change_presence(activity=discord.CustomActivity(name="I'm nice at ping pong", emoji=discord.PartialEmoji(name="U+1F3D3")))

client = Client()
client.run(secrets.TOKEN)