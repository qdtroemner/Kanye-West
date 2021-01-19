import requests
from datetime import datetime
from deps import kanye_secrets as secrets

class Spotify:
	def __init__(self):
		self.access_token = None
		self.token_timestamp = None

	def request_auth(self):
		url = "https://accounts.spotify.com/api/token"
		headers = {
			"Authorization": "Basic " + secrets.SPOTIFYB64
		}
		params = {
			"grant_type": "client_credentials"
		}
		req = requests.post(url, data=params, headers=headers)
		if req.status_code == 200:
			self.access_token = req.json()['access_token']
			self.token_timestamp = datetime.now()

	def get(self, url, headers={}, params={}):
		if self.access_token and self.token_timestamp:
			time_since_token = datetime.now() - self.token_timestamp
			if time_since_token.total_seconds() < 3600.0:
				try:
					headers["Authorization"] = "Bearer " + self.access_token
					req = requests.get(url, headers=headers, params=params)
					data = req.json()
					if req.status_code == 200:
						return data
				except Exception as error:
					print(error)
			else:
				#print("Token expired")
				self.request_auth()
				return self.get(url=url, headers=headers, params=params)
		else:
			#print("No token or timestamp")
			self.request_auth()
			return self.get(url=url, headers=headers, params=params)