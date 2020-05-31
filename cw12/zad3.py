from lxml import html
import requests

url = "https://boardgamegeek.com/"
data = requests.get(url)


page = html.fromstring(data.text)