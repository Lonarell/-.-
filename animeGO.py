import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl

def collect_anime():
    data = []
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

        data.append(anime_all)  # Добавляем данные в список.

    return data

df = pd.DataFrame(collect_anime())  # Создаём DataFrame.
df.to_excel("anime.xlsx")  # Сохраняем DataFrame в Excel.
df.to_csv("anime.csv")  # Сохраняем DataFrame в CSV.

















