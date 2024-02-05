import requests
from bs4 import BeautifulSoup
from urllib import *

visited_urls = set()


def spider_rules(url, keyword):
    try:
        response = requests.get(url)
    except:
        print(f"Request Failed {url}")
        return

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        a_tag = soup.find_all('a')
        urls = []
        for tag in a_tag:
            href = tag.get("href")
            print(href)
            if href is not None and href != "":
                urls.append(href)
        print(urls)
    else:
        print(f"Request Bad Status Code {response.status_code}")


url = input("Enter the url: ")
keyword = input("Enter the keyword to search in the url provided: ")
spider_rules(url, keyword)
