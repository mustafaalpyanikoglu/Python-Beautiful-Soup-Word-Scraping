from cgi import test
from bs4 import BeautifulSoup
import requests
import csv

URL = "https://github.com/ooguz/turkce-kufur-karaliste/blob/master/karaliste.txt"
source = requests.get(URL).text
soup = BeautifulSoup(source, 'lxml')

csv_file = open('TurkishBlackList.csv', 'a', encoding="utf-16", newline="")
csv_writer = csv.writer(csv_file)

table = soup.find('table')
rows = table.findAll('tr')
x = 0

for tr in rows:
    cols = tr.findAll(
        'td', attrs={'class': 'blob-code blob-code-inner js-file-line'})
    if not cols:
        # Boş satırı geçer
        continue
    for td in cols:
        word = str(td.text)
        print(word.replace(',', ''))
        csv_writer.writerow([word.replace(',', '')])
    x = x + 1
csv_file.close()
