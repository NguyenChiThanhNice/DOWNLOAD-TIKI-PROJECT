# 📦 Project 02 – Téléchargement de données produits via l'API de Tiki

Ce projet a pour but de télécharger les informations de 200 000 produits depuis l'API de Tiki, de les nettoyer et de les stocker dans des fichiers `.json` par lots (batchs) de 1 000 produits.

## ✅ Objectifs

- Utiliser `aiohttp` pour effectuer des requêtes asynchrones vers l'API Tiki
- Nettoyer les descriptions produits en supprimant les balises HTML
- Enregistrer les données dans des fichiers JSON structurés par lots
- Journaliser les erreurs dans un fichier `errors.log`
- Optimiser les performances grâce à l'asynchronisme et la limitation des requêtes simultanées

## 📄 Données extraites

Pour chaque produit, les champs suivants sont collectés :

- `id`
- `name`
- `url_key`
- `price`
- `description` (nettoyée)
- `image` (liste d'URL)

## 🛠️ Technologies utilisées

- `aiohttp` : pour les requêtes HTTP asynchrones
- `aiofiles` : pour écrire les fichiers sans bloquer l'exécution
- `asyncio` : pour gérer les tâches concurrentes
- `pandas` : pour lire, analyser ou transformer les fichiers JSON
- `BeautifulSoup` : pour nettoyer le HTML des descriptions
- `tqdm` : pour afficher une barre de progression

## 📁 Structure du projet

project02/
│
├── output/ ← Fichiers JSON exportés par batch
├── errors.log ← Liste des produits échoués avec message d'erreur
├── product_ids.txt ← Liste des IDs produits (un par ligne)
├── main_script.py ← Script principal de téléchargement
├── lire_json.py ← Script pour lire les fichiers JSON
├── nettoyer_data.py ← Script pour transformer un fichier CSV en product_ids.txt
└── README.md ← Ce fichier


## ▶️ Comment exécuter le projet

1. Installer les dépendances :

   ```bash
  	 pip install aiohttp aiofiles pandas beautifulsoup4 tqdm

2. Créer le fichier product_ids.txt contenant les IDs produits à extraire (un ID par ligne).

3. Exécuter le script principal :
	python main_script.py

4. Lire les données extraites avec :
	python lire_json.py
📝 Notes
    • Les fichiers sont enregistrés dans output/products_0001.json, products_0002.json, etc.
    • Les erreurs (produit non trouvé, timeout, etc.) sont enregistrées dans errors.log.
    • Le script est conçu pour être relancé sans perdre les données déjà collectées.
📬 Auteur
Xuong-Dao (Chi Thanh NGUYEN)

