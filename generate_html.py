import json

def generate_html_from_json(json_file, output_html):
    with open(json_file, 'r', encoding='utf-8') as f:
        books = json.load(f)

    books_json = json.dumps(books, ensure_ascii=False, indent=4)

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Book Display</title>
        <style>
            .filter-container {{
                float: left;
                width: 20%;
                padding: 10px;
            }}
            .books-container {{
                float: left;
                width: 75%;
                padding: 10px;
            }}
            .book {{
                border: 1px solid #ddd;
                margin-bottom: 10px;
                padding: 10px;
                display: flex;
            }}
            .thumbnail img {{
                max-width: 100px;
                margin-right: 10px;
            }}
            .details {{
                flex: 1;
            }}
            .clear {{
                clear: both;
            }}
        </style>
    </head>
    <body>
        <div class="filter-container">
            <h2>Filters</h2>
            <label for="filter-year">Year:</label>
            <input type="text" id="filter-year" oninput="filterBooks()"><br>
            <label for="filter-author">Author:</label>
            <input type="text" id="filter-author" oninput="filterBooks()"><br>
            <label for="filter-language">Language:</label>
            <input type="text" id="filter-language" oninput="filterBooks()"><br>
            <label for="filter-publisher">Publisher:</label>
            <input type="text" id="filter-publisher" oninput="filterBooks()"><br>
            <label for="filter-subject">Subject:</label>
            <input type="text" id="filter-subject" oninput="filterBooks()"><br>
        </div>
        <div class="books-container" id="books"></div>
        <div class="clear"></div>

        <script>
            document.addEventListener('DOMContentLoaded', function() {{
                const booksData = {books_json};

                function loadBooks() {{
                    const booksContainer = document.getElementById('books');
                    booksContainer.innerHTML = '';  // Clear any previous book data
                    booksData.forEach(book => {{
                        const bookDiv = document.createElement('div');
                        bookDiv.className = 'book';
                        bookDiv.dataset.year = book.year;
                        bookDiv.dataset.author = book.creators.join(', ');
                        bookDiv.dataset.language = book.language;
                        bookDiv.dataset.publisher = book.publisher;
                        bookDiv.dataset.subject = book.subject;

                        const thumbnail = document.createElement('div');
                        thumbnail.className = 'thumbnail';
                        const img = document.createElement('img');
                        img.src = book.thumbnail_url;
                        thumbnail.appendChild(img);

                        const details = document.createElement('div');
                        details.className = 'details';
                        details.innerHTML = `<h3>${{book.title}}</h3><p>Author: ${{book.creators.join(', ')}}</p><p>Publisher: ${{book.publisher}}</p><p>Year: ${{book.year}}</p><p>Language: ${{book.language}}</p><p>Subject: ${{book.subject}}</p>`;

                        const link = document.createElement('a');
                        link.href = book.pdf_url;
                        link.textContent = 'Download';
                        details.appendChild(link);

                        bookDiv.appendChild(thumbnail);
                        bookDiv.appendChild(details);

                        booksContainer.appendChild(bookDiv);
                    }});
                }}

                function filterBooks() {{
                    const year = document.getElementById('filter-year').value.toLowerCase();
                    const author = document.getElementById('filter-author').value.toLowerCase();
                    const language = document.getElementById('filter-language').value.toLowerCase();
                    const publisher = document.getElementById('filter-publisher').value.toLowerCase();
                    const subject = document.getElementById('filter-subject').value.toLowerCase();

                    const books = document.querySelectorAll('.book');
                    books.forEach(book => {{
                        const bookYear = book.dataset.year.toLowerCase();
                        const bookAuthor = book.dataset.author.toLowerCase();
                        const bookLanguage = book.dataset.language.toLowerCase();
                        const bookPublisher = book.dataset.publisher.toLowerCase();
                        const bookSubject = book.dataset.subject.toLowerCase();

                        if ((year === '' || bookYear.includes(year)) &&
                            (author === '' || bookAuthor.includes(author)) &&
                            (language === '' || bookLanguage.includes(language)) &&
                            (publisher === '' || bookPublisher.includes(publisher)) &&
                            (subject === '' || bookSubject.includes(subject))) {{
                            book.style.display = 'flex';
                        }} else {{
                            book.style.display = 'none';
                        }}
                    }});
                }}

                window.loadBooks = loadBooks;
                window.filterBooks = filterBooks;

                loadBooks();  // Load books on page load
            }});
        </script>
    </body>
    </html>
    """

    with open(output_html, "w", encoding='utf-8') as f:
        f.write(html_content)

# Specify the path to your JSON file and the desired output HTML file
json_file = "consolidated_books.json"
output_html = "index.html"
generate_html_from_json(json_file, output_html)
