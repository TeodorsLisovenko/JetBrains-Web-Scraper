import requests

from bs4 import BeautifulSoup

act = int(input())

url = input()

r = requests.get(url)

if r.status_code:
    soup = BeautifulSoup(r.content, 'html.parser')
    hyperlinks = soup.find_all('a')
    counter = 1
    for link in hyperlinks:
        if link.get('href') and counter == act:
            print(link.get('href'))
        counter += 1
