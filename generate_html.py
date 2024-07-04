import os
import json
from xml.etree import ElementTree as ET

# Load book identifiers from JSON file
with open('book_identifiers.json', 'r') as json_file:
    book_identifiers = json.load(json_file)

book_identifiers = book_identifiers[:25]
# Base directory for books
base_dir = "books"

# Function to generate HTML content for each book
def generate_book_html(folder):
    meta_file_path = os.path.join(base_dir, folder, f"{folder}_meta.xml")
    thumb_path = os.path.join(base_dir, folder, "__ia_thumb.jpg")
    pdf_path = os.path.join(base_dir, folder, f"{folder}.pdf")

    # Debugging print statements
    # print(f"Processing folder: {folder}")
    # print(f"Expected Meta file path: {meta_file_path}")
    # print(f"Expected Thumbnail path: {thumb_path}")
    # print(f"Expected PDF path: {pdf_path}")

    # Check if the directory exists
    dir_path = os.path.join(base_dir, folder)
    if not os.path.isdir(dir_path):
        print(f"Directory not found: {dir_path}")
        return ""

    # List all files in the directory for debugging
    # print(f"Files in directory {dir_path}:")
    # for file in os.listdir(dir_path):
    #     print(f"- {file}")

    # Check if meta file exists
    if not os.path.exists(meta_file_path):
        print(f"Meta file not found: {meta_file_path}")
        return ""

    try:
        # Load and parse XML metadata
        with open(meta_file_path, 'r', encoding='utf-8') as file:
            xml_content = file.read()

        # Parse the XML content
        xml_tree = ET.ElementTree(ET.fromstring(xml_content))
        title = xml_tree.findtext('title', 'N/A')
        creators = [creator.text for creator in xml_tree.findall('creator')]
        year = xml_tree.findtext('year', 'N/A')
        language = xml_tree.findtext('language', 'N/A')
        subject = xml_tree.findtext('subject', 'N/A')
        publisher = xml_tree.findtext('publisher', 'N/A')

        book_html = f'''
        <div class="book" data-year="{year}" data-author="{', '.join(creators)}" data-language="{language}" data-publisher="{publisher}" data-subject="{subject}">
            <div class="thumbnail">
                <img src="{thumb_path}" alt="{title}">
            </div>
            <div class="details">
                <h3>{title}</h3>
                <p>Author: {', '.join(creators)}</p>
                <p>Publisher: {publisher}</p>
                <p>Year: {year}</p>
                <p>Language: {language}</p>
                <p>Subject: {subject}</p>
              
            </div>
        </div>
        '''
        return book_html

    except Exception as e:
        print(f"Error processing {folder}: {e}")
        return ""

# Generate the complete HTML file
html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Book Collection</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="filters">
        <label for="filter-year">Year:</label>
        <input type="text" id="filter-year" onkeydown="handleFilterKeydown(event)">
        <label for="filter-author">Author:</label>
        <input type="text" id="filter-author" onkeydown="handleFilterKeydown(event)">
        <label for="filter-language">Language:</label>
        <input type="text" id="filter-language" onkeydown="handleFilterKeydown(event)">
        <label for="filter-publisher">Publisher:</label>
        <input type="text" id="filter-publisher" onkeydown="handleFilterKeydown(event)">
        <label for="filter-subject">Subject:</label>
        <input type="text" id="filter-subject" onkeydown="handleFilterKeydown(event)">
    </div>
    <div id="books">
'''

# Add book data to the HTML content
for folder in book_identifiers:
    html_content += generate_book_html(folder)

# Close the HTML content
html_content += '''
    </div>
    <script>
        function handleFilterKeydown(event) {
            if (event.key === "Enter") {
                filterBooks();
            }
        }

        function filterBooks() {
            const year = document.getElementById('filter-year').value.toLowerCase();
            const author = document.getElementById('filter-author').value.toLowerCase();
            const language = document.getElementById('filter-language').value.toLowerCase();
            const publisher = document.getElementById('filter-publisher').value.toLowerCase();
            const subject = document.getElementById('filter-subject').value.toLowerCase();

            const books = document.querySelectorAll('.book');
            books.forEach(book => {
                const bookYear = book.dataset.year.toLowerCase();
                const bookAuthor = book.dataset.author.toLowerCase();
                const bookLanguage = book.dataset.language.toLowerCase();
                const bookPublisher = book.dataset.publisher.toLowerCase();
                const bookSubject = book.dataset.subject.toLowerCase();

                if ((year === '' || bookYear.includes(year)) &&
                    (author === '' || bookAuthor.includes(author)) &&
                    (language === '' || bookLanguage.includes(language)) &&
                    (publisher === '' || bookPublisher.includes(publisher)) &&
                    (subject === '' || bookSubject.includes(subject))) {
                    book.style.display = 'flex';
                } else {
                    book.style.display = 'none';
                }
            });
        }
    </script>
    <footer class="footer">
        <p class="footer-text">&copy; 2013-2024 ಕನ್ನಡ ಸಂಚಯ | ಸಾಹಿತ್ಯ ಸಂಶೋಧನೆ ಹಾಗೂ ಅಧ್ಯಯನ ವೇದಿಕೆ</p>
    </footer>
</body>
</html>
'''

# Write the generated HTML content to a file
with open('index.html', 'w', encoding='utf-8') as file:
    file.write(html_content)

print("HTML file generated successfully.")
