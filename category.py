import time
import csv

import requests
from bs4 import BeautifulSoup

from book import get_book


CSV_HEADERS = ['product_page_url', 'universal_product_code', 'title', 'price_including_tax',
    'price_excluding_tax', 'number_available', 'product_description', 'category',
    'review_rating', 'image_url']


def get_books_from_category(url, category):
    response, pages = requests.get(url), []

    if response.ok:
        filename = 'books_' + category + '.csv'

        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file) # Création d'un object ou l'on peut écrire/convertir des données en csv.
            writer.writerow(CSV_HEADERS) # On ajoute les en-têtes en première ligne du fichier csv.

            #Récupère le bloc HTML de la page web.
            soup = BeautifulSoup(response.text, 'html.parser')
            number_of_pages = soup.find('li', {'class': 'current'})

            # Cette condition permet d'ajouter les urls des différentes pages si elles existent, sinon
            # on ajoute simplement l'url de base.
            if number_of_pages:
                number_of_pages = int(number_of_pages.text.split()[-1]) 
                for page in range(number_of_pages):
                    pages.append('/'.join(url.split('/')[:-1]) + '/page-{}.html'.format(page+1))
            else:
                pages.append(url)

                    
            # On navigue à travers toutes les urls disponibles dans la liste 'pages'.
            for page in pages:
                response = requests.get(page)

                if response.ok:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    books = soup.findAll('li', {'class': 'col-xs-6 col-sm-4 col-md-3 col-lg-3'})

                    # on récupère le lien de chaque livre et leurs informations souhaitées.
                    for book in books:
                        link = 'http://books.toscrape.com/catalogue' +  book.find('a')['href'][8:]
                        data = get_book(link)
                                    
                        # Utilise la solution d'encodage et décodage pour afficher correctement £ et autres
                        # caractères dans le fichier CSV (seul solution trouvé).
                        writer.writerow([d.encode('raw_unicode_escape').decode('utf-8') for d in data])
    else:
        print('Error loading page.')
    print('\n', flush=True)


# Tester le script sans l'importer
if __name__ == '__main__':
    get_books_from_category('http://books.toscrape.com/catalogue/category/books/fantasy_19/index.html')

