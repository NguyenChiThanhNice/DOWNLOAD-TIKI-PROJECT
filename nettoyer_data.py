import pandas as pd

#=====PARAMÈTRES=========
fichier_csv = "liste_ids.csv"
colonne_id = "id"
fichier_sortie = "product_ids.txt"

#======LECTURE ET NETTOYAGE=======
df = pd.read_csv(fichier_csv)

#==Garde uniquement les valeurs numériques valides (non vides, non NaN)
ids = df[colonne_id].dropna().astype(int).unique()

#=========ÉCRITURE DANS LE FICHIER TXT=================
with open(fichier_sortie, "w", encoding="utf-8") as f:
    for pid in ids:
        f.write(f"{pid}\n")

print(f"✅ {len(ids)} IDs enregistrés dans '{fichier_sortie}'")
