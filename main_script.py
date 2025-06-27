import aiohttp        # Pour effectuer des requêtes asynchrones
import aiofiles       # Pour écrire les fichiers asynchorones
import asyncio        # Pour gérer la boucle d'événements et les coroutines
import json           # Pour travailler avec des données JSON
from bs4 import BeautifulSoup     # Pour Nettoyer la description HTML
from tqdm import tqdm             # Pour afficher une barre de progression
import os             # Pour gérer les fichiers et des dossiers

#==========PARAMETRE============ 
API_URL = "https://api.tiki.vn/product-detail/api/v1/products/{}"
OUTPUT_DIR = "output"     # Dossier où les fichiers JSON seront sauvegardé
ERROR_LOG = "errors.log"  # Fichier de log pour les produits qui échouent
BATCH_SIZE = 1000         # Nombre de produits par fichier .json
CONCURRENT_REQUESTS = 50   # Limite de requêtes simultanées (évite de surcharger l'API)

# ====NORMALISATION DES DESCRIPTIONS====
def clean_description(desc):
    # Nettoie le champ description en supprimant les balises HTML et les superflus.
    if not desc:
        return ""
    
    soup = BeautifulSoup(desc, "html.parser")   # Supprime le HTML
    return " ".join(soup.get_text().split())    # Supprime les espaces multiples.
    
#=======ENREGISTRER UN BATCH=================
async def save_batch(batch_data, index):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    filename = os.path.join(OUTPUT_DIR, f"products_{index:04d}.json")
    async with aiofiles.open(filename, "w", encoding="utf-8") as f:
        await f.write(json.dumps(batch_data, ensure_ascii=False, indent=2))

#========ENREGISTRER UN ERREUR================
async def log_error(product_id, error_message):
    async with aiofiles.open(ERROR_LOG, "a", encoding="utf-8") as f:
        await f.write(f"{product_id}: {error_message}\n")
        
#=======TRAITER UN PRODUIT===========
async def fetch_product(session, product_id, semaphore):
    async with semaphore:
        try:
            async with session.get(API_URL.format(product_id), timeout=10) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return {
                        "id": data.get("id"),
                        "name": data.get("name"),
                        "url_key": data.get("url_key"),
                        "price": data.get("price"),
                        "description": clean_description(data.get("description")),
                        "image": data.get("image", [])
                    }
                else:
                    await log_error(product_id, f"HTTP{resp.status}")
        except Exception as e:
            await log_error(product_id, str(e))
    return None

#==========BOUCLE PRINCIPALE==============
async def main(product_ids):
    semaphore = asyncio.Semaphore(CONCURRENT_REQUESTS)
    connector = aiohttp.TCPConnector(limit=CONCURRENT_REQUESTS)
    timeout = aiohttp.ClientTimeout(total=20)
    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        tasks = []
        results = []
        file_index = 1

        for i, pid in enumerate(tqdm(product_ids, desc="Téléchargement")):
            tasks.append(fetch_product(session, pid, semaphore))
            if len(tasks) >= BATCH_SIZE:
                batch = await asyncio.gather(*tasks)
                cleaned_batch = [item for item in batch if item]
                await save_batch(cleaned_batch, file_index)
                file_index += 1
                tasks = []

        # Derniers éléments
        if tasks:
            batch = await asyncio.gather(*tasks)
            cleaned_batch = [item for item in batch if item]
            await save_batch(cleaned_batch, file_index)

#==========LECTURE DES IDS==========
def load_ids(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip().isdigit()]
    
#=======POINT D'ENTRÉE==========
if __name__ == "__main__":
    ids = load_ids("product_ids.txt")       # Tu dois avoir in fichier avec 1 ID par ligne
    asyncio.run(main(ids))






    
