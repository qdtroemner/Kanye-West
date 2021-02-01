import requests
from io import BytesIO

def generate_person():
	url = "https://thispersondoesnotexist.com/image"
	headers = {

	}
	req = requests.get(url, headers=headers)
	image_data = BytesIO(req.content)
	return image_data