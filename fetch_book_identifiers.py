import requests
import json

# Define the collection identifier (replace with your actual collection ID)
collection_id = "ServantsOfKnowledge"

# Construct the search URL
search_url = f"https://archive.org/advancedsearch.php?q=collection:{collection_id}&fl[]=identifier&rows=10000&output=json"

# Fetch data from the Internet Archive
response = requests.get(search_url)
if response.status_code == 200:
    data = response.json()
    docs = data['response']['docs']
    book_identifiers = [doc['identifier'] for doc in docs]

    # Save the book identifiers to a JSON file
    with open('book_identifiers.json', 'w') as json_file:
        json.dump(book_identifiers, json_file, indent=4)

    print(f"Found {len(book_identifiers)} book identifiers and saved to book_identifiers.json.")
else:
    print("Failed to fetch data from Internet Archive.")
