"""
Quotes game: A game that generates random quotes by a random author and asks you to guess
the author.
"""
import csv
from time import sleep
import requests
from bs4 import BeautifulSoup


def quote_writer(quotes_array, writer):
    """Function to write quotes into csv file

    Parameters
    ----------
    quotes_array : list
        A list of quotes

    writer : object
        `csv.DictWriter` object
    """
    for quote in quotes_array:
        quote, author, bio_end = quote.findChild().get_text(), quote.findChild().findNextSibling(
        ).findChild().get_text(), quote.findChild().findNextSibling(
        ).findChild().findNextSibling()["href"]
        bio_url = f"http://quotes.toscrape.com/{bio_end}"
        sleep(1)
        bio_response = requests.get(bio_url)
        bio_soup = BeautifulSoup(bio_response.text, "html.parser")
        bio = bio_soup.select(
            ".author-description")[0].get_text()

        # finally we enter the results into our csv file!
        writer.writerow({
            "Author": author,
            "Quote": quote,
            "Bio": bio
        })
        print(author)


# First we scrape the quotes from this website using BS4 and store them in a csv file
URL = "http://quotes.toscrape.com"
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
next_button = soup.find("li", attrs="next")
quotes = soup.select(".quote")


# We create a csv file to store the data
with open("quote_db.csv", "w", encoding="utf-8") as file:
    headers = ["Author", "Quote", "Bio"]
    csv_writer = csv.DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    # Then we save the homepage data into csv
    quote_writer(quotes, csv_writer)
    # Then we access each quote to extract the quote author and bio to make the game.
    while next_button is not None:
        next_page = next_button.findChild()["href"]
        URL = f"http://quotes.toscrape.com{next_page}"
        sleep(1)
        response = requests.get(URL)
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.select(".quote")
        quote_writer(quotes, csv_writer)
        next_button = soup.find("li", attrs="next")
