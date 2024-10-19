import csv, requests
from bs4 import BeautifulSoup


with open('anime_list.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(('anime_name', 'anime_review'))

for i in range(1, 150):
    url = f'https://animego.org/anime?type=animes&page={i}'

    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')

    page = soup.find_all('div', class_='animes-list-item')

    if not page:
        break

    anime_all = [[
        name.find('div', class_='media-body').find('a').text,
        name.find('div', class_='p-rate-flag__text').text
        if name.find('div', class_='p-rate-flag__text') else '—'
    ] for name in page]

    for anime in anime_all:
        with open('anime_list.csv', 'a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(anime)



