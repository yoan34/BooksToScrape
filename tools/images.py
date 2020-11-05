import requests
import os

def get_image(url, category, n):
    # Création du dossier images et sous-dossier de la catégorie
    # associé qui réception les images.
    if not os.path.exists('images'):
        os.mkdir('images')
    if not os.path.exists('images/' + category):
        os.mkdir('images/'+category)
    
    with open('images/' + category + '/book' + str(n+1)+'.jpg',  'wb') as file:
        file.write(requests.get(url).content)