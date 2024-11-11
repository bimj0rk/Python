import requests
from bs4 import BeautifulSoup

def student_function():
    url = "https://quotes.toscrape.com/"
    dict = {}
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return scrape_page(soup, dict)

def scrape_page(soup, dict):
    quotes = soup.find_all(class_ = 'quote')
    for quote in quotes:
        quote_text = quote.find(class_ = 'text').string
        author = quote.find(class_ = 'author').text
        dict[author] = quote_text
    return dict