import requests

from bs4 import BeautifulSoup

word = input()

url = input()

r = requests.get(url)

if r.status_code:
    soup = BeautifulSoup(r.content, 'html.parser')
    paragraphs = soup.find_all('p')
    for p in paragraphs:
        #check = p.text.lstrip().partition(' ')[0]
        sentences = p.text.split(". ")
        for sentence in sentences:
            if word in sentence:
                print(p.text)
                break
