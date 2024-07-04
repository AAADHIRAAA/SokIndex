import os
import requests
import json

# Load book identifiers from JSON file
with open('book_identifiers.json', 'r') as json_file:
    book_identifiers = json.load(json_file)

# Base URL for fetching data from Internet Archive
base_url = "https://archive.org/download"

# Function to create directory if it doesn't exist
def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

# Function to download a file
def download_file(url, path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
    else:
        print(f"Failed to download {url}")

# Folder to store books
books_folder = "books"
create_directory(books_folder)

# List to store folder names
book_folders = []

# Loop through each book identifier and fetch the required files
for book_id in book_identifiers:
    folder_path = os.path.join(books_folder, book_id)
    create_directory(folder_path)

    # Fetch metadata XML
    meta_url = f"{base_url}/{book_id}/{book_id}_meta.xml"
    meta_path = os.path.join(folder_path, f"{book_id}_meta.xml")
    download_file(meta_url, meta_path)

    # Fetch thumbnail image
    thumb_url = f"{base_url}/{book_id}/__ia_thumb.jpg"
    thumb_path = os.path.join(folder_path, "__ia_thumb.jpg")
    download_file(thumb_url, thumb_path)

    # Fetch PDF file
    pdf_url = f"{base_url}/{book_id}/{book_id}.pdf"
    pdf_path = os.path.join(folder_path, f"{book_id}.pdf")
    download_file(pdf_url, pdf_path)

    # Add folder to list
    book_folders.append(book_id)

# Write the book folders to a JSON file
json_path = os.path.join(books_folder, "../book_folders.json")
with open(json_path, 'w') as json_file:
    json.dump(book_folders, json_file, indent=4)

print("All files downloaded successfully and book_folders.json created.")
