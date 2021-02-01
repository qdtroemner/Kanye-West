import requests
from io import BytesIO

def generate_from_url(url):
	req = requests.get(url)
	image_data = BytesIO(req.content)
	return image_data

def generate_person():
	return generate_from_url("https://thispersondoesnotexist.com/image")

def generate_rental():
	return generate_from_url("https://thisrentaldoesnotexist.com/img-new/hero.jpg")

def generate_cat():
	return generate_from_url("https://thiscatdoesnotexist.com/")

def generate_art():
	return generate_from_url("https://thisartworkdoesnotexist.com/")

def generate_horse():
	return generate_from_url("https://thishorsedoesnotexist.com/")