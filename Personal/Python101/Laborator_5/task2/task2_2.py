import requests
import csv
from bs4 import BeautifulSoup
from task2_1 import scrape_page

def student_function():
    url = "https://books.toscrape.com/"
    # TODO: Use scrape_book to get the information needed to fill the dictionary and return it!
    return scrape_site(url)

def scrape_site(url):
    # TODO Scrape the site!
    dict = {}
    return dict