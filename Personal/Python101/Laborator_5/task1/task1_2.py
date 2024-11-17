import requests
from bs4 import BeautifulSoup
from task1_1 import scrape_page

def student_function():
    url = "https://quotes.toscrape.com/"
    dict = {}
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    return scrape_site(url, soup, dict)

def scrape_site(url, soup, dict):
    # TODO: Scrape the site!
    # HINT 1: See if the button for the next page exists, if not, then you have reached the last page
    # HINT 2: Use the scrape_page function from task1_1 !
    # HINT 3: Remember to modify the url so that you get the right page. use ref['href'] to get the value of the href field.

    return dict
