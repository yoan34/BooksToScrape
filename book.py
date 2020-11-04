import time
import csv

import requests
from bs4 import BeautifulSoup

NUMERATION_REVIEW_RATING = {'One': '1', 'Two': '2', 'Three': '3', 'Four': '4', 'Five': '5'}

def get_book(url):
    response = requests.get(url)

    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        informations = soup.findAll('td') # Récupère les données dans la section "Product Information"
        [informations.pop(index) for index in [1,3,4]] # Supprime des données inintéressantes

       # Extraction des informations demandées
        upc              = informations[0].text
        title            = soup.find('h1').text
        price_in_tax     = informations[1].text
        price_ex_tax     = informations[2].text
        number_available = informations[-1].text[10:].split()[0]
        description      = soup.findAll('p')[3].text
        category         = soup.find('ul', {'class': 'breadcrumb'}).findAll('li')[2].find('a').text
        review_rating    = NUMERATION_REVIEW_RATING[soup.find('p', {'class': 'star-rating'})['class'][1]]
        image_url        = 'http://books.toscrape.com/' + soup.find('img')['src'][6:]
        print('     book: {}'.format(title.encode('raw_unicode_escape').decode('utf-8')), flush=True)
        return [url, upc, title, price_in_tax, price_ex_tax, number_available, description,
            category, review_rating, image_url]


# Tester le script sans l'importer
if __name__ == '__main__':
    informations = get_book('http://books.toscrape.com/catalogue/the-power-of-now-a-guide-to-spiritual-enlightenment_855/index.html')
    for information in informations:
        print(information)

        
    