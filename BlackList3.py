from bs4 import BeautifulSoup
import requests
import csv

URL = "https://en.wiktionary.org/wiki/Category:English_swear_words"
FIRSTWORD = "Appendix"

result = requests.get(URL)
soup = BeautifulSoup(result.text, "html.parser")

csv_file = open('EnglishBlackList.csv', 'w', encoding="utf-16", newline="")
csv_writer = csv.writer(csv_file)

for div in soup.findAll('div', {'class': 'mw-category-group'}):
    uls = div.findAll('ul')
    for ul in uls:
        for li in ul.findAll('li'):
            for a in li.find_all('a', href=True):
                if FIRSTWORD in a.text:
                    continue
                print(a.text)
                csv_writer.writerow([a.text.replace(',', '')])
csv_file.close()
