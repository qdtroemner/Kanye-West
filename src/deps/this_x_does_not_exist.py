import requests
from io import BytesIO

def generate_person():
	url = "https://thispersondoesnotexist.com/image"
	req = requests.get(url)
	image_data = BytesIO(req.content)
	return image_data

def generate_rental():
	url = "https://thisrentaldoesnotexist.com/img-new/hero.jpg"
	req = requests.get(url)
	image_data = BytesIO(req.content)
	return image_data

def generate_cat():
	url = "https://thiscatdoesnotexist.com/"
	req = requests.get(url)
	image_data = BytesIO(req.content)
	return image_data

def generate_art():
	url = "https://thisartworkdoesnotexist.com/"
	req = requests.get(url)
	image_data = BytesIO(req.content)
	return image_data