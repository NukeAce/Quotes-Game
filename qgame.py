"""
Quotes game: A game that generates random quotes by a random author and asks you to guess
the author.
"""
import csv

import requests
from bs4 import BeautifulSoup

# First we scrape the quotes from this website using BS4 and store them in a csv file
URL = "http://quotes.toscrape.com/"
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.select(".quote")

# Then we access each quote to extract the quote author and bio to make the game.
for quote in quotes:
    quote, author, bio = quote.findChild().get_text(
    ), quote.findChild().findNextSibling().findChild().get_text(), quote.findChild().findNextSibling().findChild().findNextSibling()["href"]

    print(quote, author, bio)
