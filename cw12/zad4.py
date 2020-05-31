from bs4 import BeautifulSoup
import urllib3


url = "https://www.metacritic.com/browse/games/genre/metascore/strategy/all?view=detailed"
http = urllib3.PoolManager()
page = http.request("GET", url)
# wyświetla każdy odczytany bajt
print(page.data)
soup = BeautifulSoup(page.data, 'lxml')

for tr in soup.find('table').find_all('tr'):
    for td in tr.find_all('td'):
        # jeżeli obiekt/-y nie zostaną odnalezione to zwracany jest obiekt None
        if td.find('a'):
            print(td.find('a').text.strip(), end=' ')
            # w strukturze tabeli rok wydania gry w oddzielnym elemencie <span>
            if td.find('span'):
                print(td.find('span').text.strip(), end=' ')
        else:
            print(td.text.strip(), end=' ')
    print()