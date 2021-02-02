import requests
from random import choice
from io import BytesIO

resolutions = ["640/480", "800/600", "960/720", "1024/768", "1280/960", "1400/1050", "1440/1080", "1600/1200", "1856/1392", "1920/1440", "2048/1536"]

def random_image():
	return f"https://picsum.photos/{choice(resolutions)}.jpg?random=1"
	# Is it better to download the image on the bot or simply send the URL?
