import time
import csv

import requests
from bs4 import BeautifulSoup

from category import get_books_from_category

def get_urls_categories():
    response = requests.get('http://books.toscrape.com/')
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Récupère tous les éléments liens lié aux catégories.
        categories = soup.find('ul', {'class': 'nav nav-list'}).find('ul').findAll('a')

        # Retourne une liste de urls qui contient une url de base et
        # on ajoute celle associé à chaque catégories.
        return ['http://books.toscrape.com/' + category['href'] for category in categories]


def scan_all_categories():
    urls = get_urls_categories()

    for url in urls:
        category = url[51:].split('_')[0] # Récupère le nom de la catagor
        print('Scan the category {}:'.format(category), flush=True)
        get_books_from_category(url, category)
    print('Scan finish, All files are available.')


# Tester le script sans l'importer
if __name__ == '__main__':
    scan_all_categories()
