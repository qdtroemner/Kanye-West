from deps import kanye_secrets as secrets
import lyricsgenius

genius = lyricsgenius.Genius(secrets.GENIUS)

def get_lyrics(title, artist="", get_full_info=True):
	if not title:
		return False
	
	try:	
		song = genius.search_song(title=title, artist=artist, get_full_info=get_full_info)
	except Exception as error:
		print(error)
		return

	lyrics = song.lyrics
	title = song.title
	artist = song.artist
	album_cover = song.song_art_image_url
	genius_url = song.url

	lyrics = lyrics.split("\n\n")
	if get_full_info:	
		return {"lyrics": lyrics, "title": title, "artist": artist, "genius_url": genius_url, "album_cover": album_cover}
	else:
		return {"lyrics": lyrics, "title": title, "artist": artist}