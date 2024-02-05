# https://en.wikipedia.org/wiki/Programmer

import requests
from bs4 import BeautifulSoup


def get_page(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    print(soup.find("a"))


get_page(input("Enter the url: "))
