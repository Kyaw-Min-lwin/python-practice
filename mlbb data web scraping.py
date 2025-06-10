import requests
from bs4 import BeautifulSoup
import csv


source = requests.get('https://www.expertwm.com/heroes/').content
soup = BeautifulSoup(source, 'lxml')

csv_file = open('mlbb_stats.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Hero name', 'winrate', 'pickrate', 'banrate'])

for hero in soup.find_all('tr'):
    try:
        hero_name = hero.find('td', class_='hero-name').text
        stats = hero.find_all('td', class_='hero-stats')
        winrate = stats[0].text
        pickrate = stats[1].text
        banrate = stats[2].text
        print(hero_name, winrate, pickrate, banrate)
        csv_writer.writerow([hero_name, winrate, pickrate, banrate])
    except:
        pass
    print()

csv_file.close()
