import requests
from bs4 import BeautifulSoup
from task2_0 import scrape_book

def student_function():
    url = "https://books.toscrape.com/"
    dict = {}
    soup = # TODO Get the page's soup!
    index = # TODO: Set the index!
    # TODO: Use scrape_book to get the information needed to fill the dictionary and return it!
    scrape_page(url, soup, dict, index)
    return dict

def scrape_page(url, soup, dict, index):
    # TODO: Scrape the page!