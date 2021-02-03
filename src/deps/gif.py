import requests
from deps import kanye_secrets as secrets
from random import randint

def search_gifs(query=None):
	if query is None:
		return None
	
	url = "https://api.giphy.com/v1/gifs/search"
	params = {
		"api_key": secrets.GIPHY,
		"q": query,
		"limit": 1, # 1 for now
		"offset": randint(0, 100),
		"lang": "en"
	}
	req = requests.get(url, params=params)
	
	if req.status_code == 200:
		json = req.json()
		data = json["data"][0]
		gif_url = data["images"]["original"]["url"]
		title = data["title"]

		return gif_url, title