import os       # Pour manipuler les dossiers et les fichiers
import json     # Pour lire les fichiers   json
import pandas as pd     # Pour créer et manipuler les tableaux de données

#=======PARAMÈTRE===========
DOSSIER_JSON = "output"     # Dossier contenant les fichiers  .json

#=========LISTE POUR STOCKER TOUS LES PRODUITS==========
tous_les_produits = []

#=======PARCOURIR TOUS LES FICHIERS DU DOSSIER===========
for nom_fichier in sorted(os.listdir(DOSSIER_JSON)):     # Trie les fichiers par ordre alphabétique
    if nom_fichier.endswith(".json"):       # On ne garde que les fichiers  .json
        chemin_complet = os.path.join(DOSSIER_JSON, nom_fichier)    # Chemin complet vers le fichier
        with open(chemin_complet, "r", encoding="utf-8") as f:
            produits = json.load(f)     # Charge le contenu JSON (liste de produits)
            tous_les_produits.extend(produits)  # Ajouter tous les produits à la liste globale

#==========CONVERTIR EN TABLEAU AVEC PANDAS==========
df = pd.DataFrame(tous_les_produits)    # Créer un tableau (DataFrame) à partir de la liste

#=========AFFICHER QUELQUES INFOS========
print("✅ Colonnes disponibles :", df.columns.tolist())     # Afficher les noms de colonnes
print("\n📊 Aperçu des 5 premiers produits :")
print(df.head())

df.to_csv("Produits_complets.csv", index=False, encoding="utf-8-sig")