import requests

from bs4 import BeautifulSoup

url = input()

r = requests.get(url)

if r.status_code:
    soup = BeautifulSoup(r.content, 'html.parser')
    header = soup.find('h1')
    print(header.text)
