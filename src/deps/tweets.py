import requests
from deps import kanye_secrets as secrets

def get_recent_tweet():
	url = "https://api.twitter.com/2/tweets/sample/stream"
	headers = {
		"Authorization": "Bearer " + secrets.TWITTER_TOKEN
	}
	print(url, headers)
	req = requests.get(url, headers=headers)
	print(req, req.json())
	if req.status_code == 200:
		return req.json()
	else:
		return False