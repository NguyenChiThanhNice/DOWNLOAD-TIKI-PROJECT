📦 Project 02 – Product Data Downloader via Tiki API

This project aims to download information for 200,000 products from the Tiki API, clean the data, and store it into `.json` files in batches of 1,000 products each.

✅ Objectives

- Use `aiohttp` for asynchronous HTTP requests to the Tiki API
- Clean product descriptions by removing HTML tags
- Save structured product data into JSON files
- Log errors into a `errors.log` file
- Optimize performance via asynchronous processing and request throttling

📄 Data fields collected

For each product, the following fields are extracted:

- `id`
- `name`
- `url_key`
- `price`
- `description` (cleaned)
- `image` (list of image URLs)

🛠️ Technologies used

- `aiohttp`: for asynchronous HTTP requests
- `aiofiles`: to write files without blocking the event loop
- `asyncio`: to manage concurrent tasks
- `pandas`: to read and analyze JSON files
- `BeautifulSoup`: to clean HTML from descriptions
- `tqdm`: to display progress bars

📁 Project structure

project02/
│
├── output/ ← JSON batch files
├── errors.log ← Failed product logs with error messages
├── product_ids.txt ← Product IDs (one per line)
├── main_script.py ← Main async downloader script
├── lire_json.py ← Script to read and view JSON output
├── nettoyer_data.py ← Script to convert CSV into product_ids.txt
└── README.md ← This file


▶️ How to run the project

1. Install dependencies:
 
   	pip install aiohttp aiofiles pandas beautifulsoup4 tqdm
2. Prepare the product_ids.txt file with one product ID per line.

3. Run the main downloader script:

	python main_script.py

4. Read the downloaded data using:
	python lire_json.py
📝 Notes
    • Files are saved as output/products_0001.json, products_0002.json, etc.
    • Errors (missing product, timeout, etc.) are recorded in errors.log.
    • The script can be safely resumed — existing files won't be overwritten.
📬 Author
Xuong-Dao (Chi Thanh NGUYEN)

