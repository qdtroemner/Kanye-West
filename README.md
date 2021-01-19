# Welcome to the Kanye West source code!
> Current verision: v1.0

# Usage
In its current form, the Kanye can be run through `bot.py` in the `src` folder.
The only missing file is `kanye_secrets.py` which you should add to `src/deps/` and create a variable named `TOKEN` with your bot token. Other secrets for bot functionality can be found below. Kanye may break without them.

## kanye_secrets.py
These are the secrets that should be included in the `kanye_secrets.py` script, if you would like full functionality.
- TOKEN
	- The token of your Discord bot.
- SPOTIFYB64
	- A base-64 encoded [Spotify API](https://developer.spotify.com/dashboard/applications) bearer token.
- GENIUS
	- A [Genius lyrics API](https://genius.com/api-clients) key.
- GIPHY
	- A [Giphy API](https://developers.giphy.com/dashboard/) key.

The docs for [discord.py](https://github.com/Rapptz/discord.py) can be found [here](https://discordpy.readthedocs.io/en/latest/api.html).
Feel free to use or copy this code.