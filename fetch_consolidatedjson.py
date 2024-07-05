import os
import json
import xml.etree.ElementTree as ET

def generate_consolidated_json(root_folder):
    books = []
    for folder_name in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder_name)
        if os.path.isdir(folder_path):
            meta_file = os.path.join(folder_path, f"{folder_name}_meta.xml")
            pdf_url = os.path.join(folder_path, f"{folder_name}.pdf")
            thumbnail_url = os.path.join(folder_path, "__ia_thumb.jpg")
            if os.path.exists(meta_file):
                tree = ET.parse(meta_file)
                root = tree.getroot()
                title = root.find('title').text if root.find('title') is not None else "N/A"
                creators = [creator.text for creator in root.findall('creator')] if root.findall('creator') else []
                year = root.find('year').text if root.find('year') is not None else "N/A"
                language = root.find('language').text if root.find('language') is not None else "N/A"
                subject = root.find('subject').text if root.find('subject') is not None else "N/A"
                publisher = root.find('publisher').text if root.find('publisher') is not None else "N/A"

                books.append({
                    "identifier": folder_name,
                    "title": title,
                    "creators": creators,
                    "year": year,
                    "language": language,
                    "subject": subject,
                    "publisher": publisher,
                    "pdf_url": pdf_url,
                    "thumbnail_url": thumbnail_url
                })

    with open("consolidated_books.json", "w", encoding='utf-8') as f:
        json.dump(books, f, ensure_ascii=False, indent=4)

# Specify the root folder containing all the book folders
root_folder = "books"
generate_consolidated_json(root_folder)
