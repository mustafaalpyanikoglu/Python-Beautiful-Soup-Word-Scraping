from bs4 import BeautifulSoup
import requests
import csv
import codecs

URL = "https://www.turkedebiyati.org/argo-sozlugu/"
FIRSTWORD = "abondone"
BANNEDWORD = "argo"

source = requests.get(URL).text
soup = BeautifulSoup(source, 'lxml')
data = soup.find_all("p strong")

p_strong_elements = []
state = False

csv_file = open('TurkishBlackList.csv', 'w', encoding="utf-16", newline="")
csv_writer = csv.writer(csv_file)
csv_writer.writerow([''])


def checkWord(word):
    global state
    if FIRSTWORD in word:
        state = True
    if state is True and BANNEDWORD not in word.lower():
        p_strong_elements.append(word)


for word in soup.find_all("strong"):
    checkWord(str(word.text))

for element in p_strong_elements:
    for i in element:
        test_string = element.replace(i, '')
    csv_writer.writerow([test_string])
csv_file.close()
