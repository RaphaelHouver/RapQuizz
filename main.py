import requests
from bs4 import BeautifulSoup as bs

print("---- Bienvenue dans le RapQuizz ----\n\n")

# Asking the name of the music (we also need the name of the artist for now)

artist = str(input("Veuillez nous donner l'artiste : "))
song = str(input("Veuillez nous donner le nom du son : "))


# Searching the song in RapGenius website

url = str("https://genius.com/search?q=" + song)

page = requests.get(url)
soup = bs(page.text , "html.parser")


# Looking for the Top Result link in the source code

data = []
link = soup.find('a', { 'class' : 'mini_card'})

print(soup)

