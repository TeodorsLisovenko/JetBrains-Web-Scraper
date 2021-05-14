import requests

from bs4 import BeautifulSoup

link = input()
r = requests.get(link)
soup = BeautifulSoup(r.content, 'html.parser')

b = soup.find_all('a')
lst = []
for a in b:
    if a.text.find('S') == 0 and str(a).find('redirect') == -1 and str(a).find('data-sf-ec-immutable="" href="#S"') == -1 and len(a.text) > 1 and str(a).find('Subscribe to our newsletters') == -1:
        lst.append(a.text)

print(lst)
