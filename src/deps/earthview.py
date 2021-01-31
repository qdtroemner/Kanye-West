import requests
from bs4 import BeautifulSoup

def get_random_earthview():
	url = "https://earthview.withgoogle.com"

	html = requests.get(url).text
	soup = BeautifulSoup(html, "html.parser")
	url_suffix = soup.findAll("a", {"class": "button intro__explore"})[0]["href"]

	return url + url_suffix