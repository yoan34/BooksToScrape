import time
import csv

import requests
from bs4 import BeautifulSoup

from book import get_book


CSV_HEADERS = ['product_page_url', 'universal_product_code', 'title', 'price_including_tax',
    'price_excluding_tax', 'number_available', 'product_description', 'category',
    'review_rating', 'image_url']

def get_books_from_category(url):
    response = requests.get(url)

    if response.ok:
        category = url[51:].split('_')[0]
        filename = 'books_' + category + '.csv'

        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file) # Création d'un object ou l'on peut écrire/convertir des données en csv.
            writer.writerow(CSV_HEADERS) # On ajoute les en-têtes en première ligne du fichier csv.

            soup = BeautifulSoup(response.text, 'html.parser')
            # récupère le bloc HTML de chaque livre
            books = soup.findAll('li', {'class': 'col-xs-6 col-sm-4 col-md-3 col-lg-3'})
                

            # Pour chaque livre, on isole son lien et on l'ajoute a une URL de base.
            for book in books:
                link = 'http://books.toscrape.com/catalogue' +  book.find('a')['href'][8:]
                data = get_book(link)
                    
                # Utilise la solution d'encodage et décodage pour afficher correctement £ et autres dans 
                # le fichier CSV (seul solution trouvé).
                writer.writerow([d.encode('raw_unicode_escape').decode('utf-8') for d in data])
    else:
        print('Error loading page.')


# Tester le script sans l'importer
if __name__ == '__main__':
    get_books_from_category('http://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html')

