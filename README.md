# BooksToScrape

Receptionner le projet dans un repertoire de votre choix.
	git clone https://github.com/yoan34/BooksToScrape.git

Aller dedans:
cd BooksToScrape/

Création d'un environnement virtuel:
	python -m venv env

Activation de l'environnement virtuel:
	console window: .\env\scripts\activate
	autre: source env/scripts/activate

Installation des dépendances du projet:
	pip install -r requirements.txt

Exécution du script qui va créer un dossier CSV avec les fichiers des différentes catégories et
un dossier images qui va télécharger les images de chaque livre.
	python scan_all_categories.py
