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
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
            }}
            .header {{
                display: flex;
                align-items: center;
                justify-content: space-between;
                background-color: #f8f8f8;
                padding: 20px;
                border-bottom: 1px solid #ddd;
                text-align: left;
            }}
            .header img {{
                max-height: 100px;
                margin-right: 20px;
            }}
            .header-content {{
                flex-grow: 1;
            }}
            .header-content p {{
                margin: 0;
                font-size: 16px;
                line-height: 1.5;
            }}
            .container {{
                display: grid;
                grid-template-columns: 20% 80%;
                grid-template-rows: 100px;
                gap: 20px;
                padding: 20px;
            }}
            .filters {{
                grid-column: 1 / 2;
                grid-row: 1;
                background-color: #f0f0f0;
                padding: 10px;
                border-radius: 5px;
                margin-bottom: 20px;
                margin-top: 10px;
            }}
            .filters fieldset {{
                margin-bottom: 10px;
            }}

            .filters fieldset div {{
                display: inline-block;
                margin-right: 10px;
            }}


            .filters label {{
                display: block;
                margin-bottom: 5px;
                margin-top: 10px;
            }}
            .filters input, .filters select {{
                width: 10%;
                margin-bottom: 10px;
            }}
            .filter-section {{
                margin-bottom: 20px;
            }}

            .filter-section div {{
                display: flex;
                align-items: center;
                margin-bottom: 5px;
            }}

           

            .filter-section input[type="checkbox"] {{
                margin-right: 10px;
                width:15px;
            }}
           
            .search-bar {{
                grid-column: 2 / -1;
                grid-row: 1;
                background-color: #f0f0f0;
                padding: 10px;
                border-radius: 20px; /* Adjust border-radius for curved edges */
                text-align: center;
                margin-bottom: 20px;
            }}

            .search-bar input[type="text"] {{
                width: 50%;
                padding: 8px;
                font-size: 16px;
                border: 1px solid #ccc;
                border-radius: 20px; /* Match the parent's border-radius */
            }}

            .search-bar input[type="text"]:focus {{
                outline: none;
                border-color: #aaa;
            }}
            .books-container {{
                grid-column: 2 / -1;
                grid-row: 2;
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 20px;
            }}
            .book {{
                position: relative;
                overflow: visible;
                border: 1px solid #ddd;
                margin-bottom: 10px;
                padding: 0;
                cursor: pointer;
            }}
            .book:hover .details-tooltip {{
                display: flex;
            }}
            .thumbnail {{
                position: relative;
                overflow: hidden;
            }}
            .thumbnail img {{
                max-width: 100%;
                display: block;
                transition: transform 0.2s;
            }}
            .book-title {{
                text-align: center;
                padding: 10px;
                font-size: 16px;
                background-color: #f0f0f0;
            }}
            .details-tooltip {{
                position: absolute;
                top: -90px; 
                left: calc(-50% - 10px); 
                transform: translateX(0%);
                width: 300px; 
                background-color: rgba(255, 255, 255, 0.95);
                color: black;
                display: none;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                opacity: 1;
                padding: 20px;
                box-sizing: border-box;
                z-index: 10; 
                border: 1px solid #ddd;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            }}
            .details {{
                text-align: left;
            }}
            .details h3 {{
                margin: 0;
            }}
            .details p {{
                margin: 5px 0;
            }}
            .clear {{
                clear: both;
            }}
              #search-books{{
                margin-top: 20px;
            }}
            .footer {{
                
                grid-column: 1 / -1;
                background-color: #bfbdbddb;
                text-align: center;
                padding: 10px;
                border-radius: 5px;
                margin-top: 20px;
            }}
        </style>
    </head>
    <body>
     <div class="header">
            <img src="public/servantsofknowledge.png" alt="Servants of knowledge">
            <div class="header-content">
                <p><strong>Servants Of Knowledge</strong></p>
                <p>This library of books, audio, video, and other materials from and about India is curated and maintained by Public Resource. The purpose of this library is to assist the students and the lifelong learners of India in their pursuit of an education so that they may better their status and their opportunities and to secure for themselves and for others justice, social, economic and political.</p>
                <br>
                <p>This library has been posted for non-commercial purposes only and facilitates fair dealing usage of academic and research materials for private use including research, for criticism and review of the work or of other works and reproduction by teachers and students in the course of instruction. Many of the books and articles are either unavailable or inaccessible in libraries in India, especially in some of the poorer states and this collection seeks to fill a major gap that exists in access to knowledge.</p>
                <p>Jai Gyan!</p>
            </div>
        </div>
        <div class="container">
            <div class="filters">
    <h2>Filters</h2>

    <div class="filter-section" id="filter-section-year">
        <h3>Year</h3>
        
        <!-- Add more years as needed 
        <button onclick="showMoreYears()">More</button>-->
    </div>

    <div class="filter-section">
        <h3>Author</h3>
        <div>
            <input type="checkbox" id="filter-author-creators" name="filter-author" value="creators" onchange="filterBooks()">
            <label for="filter-author-creators">Creators</label>
        </div>
        <div>
            <input type="checkbox" id="filter-author-shri" name="filter-author" value="shri" onchange="filterBooks()">
            <label for="filter-author-shri">Shri</label>
        </div>
        <!-- Add more authors as needed 
        <button onclick="showMoreAuthors()">More</button>-->
    </div>

    <div class="filter-section">
        <h3>Language</h3>
        <div>
            <input type="checkbox" id="filter-language-kannada" name="filter-language" value="kannada" onchange="filterBooks()">
            <label for="filter-language-kannada">Kannada</label>
        </div>
        <div>
            <input type="checkbox" id="filter-language-tamil" name="filter-language" value="tamil" onchange="filterBooks()">
            <label for="filter-language-tamil">Tamil</label>
        </div>
        <!-- Add more languages as needed 
        <button onclick="showMoreLanguages()">More</button>-->
    </div>

    <div class="filter-section">
        <h3>Subject</h3>
        <div>
            <input type="checkbox" id="filter-subject-magazine" name="filter-subject" value="magazine" onchange="filterBooks()">
            <label for="filter-subject-magazine">Magazine</label>
        </div>
        <div>
            <input type="checkbox" id="filter-subject-subject2" name="filter-subject" value="subject2" onchange="filterBooks()">
            <label for="filter-subject-subject2">Subject2</label>
        </div>
        <!-- Add more subjects as needed 
        <button onclick="showMoreSubjects()">More</button>-->
    </div>

    <div class="filter-section">
        <h3>Publisher</h3>
        <div>
            <input type="checkbox" id="filter-publisher1" name="filter-publisher" value="publisher1" onchange="filterBooks()">
            <label for="filter-publisher1">Publisher1</label>
        </div>
        <div>
            <input type="checkbox" id="filter-publisher2" name="filter-publisher" value="publisher2" onchange="filterBooks()">
            <label for="filter-publisher2">Publisher2</label>
        </div>
        <!-- Add more publishers as needed 
        <button onclick="showMorePublishers()">More</button>-->
    </div>

    <button onclick="clearFilters()">Clear Filters</button>
</div>


            <div class="search-bar">
            <input type="text" id="search-books" placeholder="Search..." >
            </div>

            <div class="books-container" id="books"></div>
            <div class="footer">
                Servants Of Knowledge Collection
            </div>
        </div>

        <script>
            document.addEventListener('DOMContentLoaded', function() {{
                const booksData = {books_json};
        function addFilters() {{
          const filtersContainer = document.getElementById(
            "filter-section-year"
          );
          const years = booksData.map((data) => data.year);
          const uniqueYears = [...new Set(years)];

          uniqueYears.forEach((year) => {{
            const inputId = `filter-year-${{year}}`;
            const label = year;
            const div = document.createElement("div");
            const input = document.createElement("input");
            input.setAttribute("type", "checkbox");
            input.setAttribute("id", inputId);
            input.setAttribute("name", "filter-year");
            input.setAttribute("value", year);
            input.setAttribute("onchange", "filterBooks()");
            const labelElement = document.createElement("label");
            labelElement.setAttribute("for", inputId);
            labelElement.textContent = label;
            div.appendChild(input);
            div.appendChild(labelElement);
            filtersContainer.appendChild(div);
           
          }});
        }}
        addFilters();
                function loadBooks() {{
                    const booksContainer = document.getElementById('books');
                    booksContainer.innerHTML = '';  // Clear any previous book data
                    booksData.forEach(book => {{
                        const bookDiv = document.createElement('div');
                        bookDiv.className = 'book';

                        const thumbnail = document.createElement('div');
                        thumbnail.className = 'thumbnail';
                        const img = document.createElement('img');
                        img.src = book.thumbnail_url;
                        thumbnail.appendChild(img);

                        const title = document.createElement('div');
                        title.className = 'book-title';
                        title.textContent = book.title;
                        thumbnail.appendChild(title);

                        const detailsTooltip = document.createElement('div');
                        detailsTooltip.className = 'details-tooltip';
                        detailsTooltip.innerHTML = `
                            <div class="details">
                                <h3>${{book.title}}</h3>
                                <p><strong>Author:</strong> ${{book.creators.join(', ')}}</p>
                                <p><strong>Publisher:</strong> ${{book.publisher}}</p>
                                <p><strong>Year:</strong> ${{book.year}}</p>
                                <p><strong>Language:</strong> ${{book.language}}</p>
                                <p><strong>Subject:</strong> ${{book.subject}}</p>
                                <a href="${{book.pdf_url}}" target="_blank">Download</a>
                            </div>
                        `;

                        bookDiv.appendChild(detailsTooltip);
                        bookDiv.appendChild(thumbnail);

                        booksContainer.appendChild(bookDiv);
                     
                    }});
                }}
          
        function filterBooks() {{
                    const searchTerm = document.getElementById('search-books').value.toLowerCase();
                    const filters = {{
                        year: [],
                        author: [],
                        language: [],
                        subject: [],
                        publisher: []
                    }};

                    document.querySelectorAll('.filters input[type="checkbox"]').forEach(checkbox => {{
                        if (checkbox.checked) {{
                            const [filterType, filterValue] = checkbox.id.split('-').slice(1);
                            filters[filterType].push(filterValue);
                        }}
                    }});

                    const filteredBooks = booksData.filter(book => {{
                        const matchesSearchTerm = book.title.toLowerCase().includes(searchTerm) ||
                            book.creators.some(creator => creator.toLowerCase().includes(searchTerm)) ||
                            book.publisher.toLowerCase().includes(searchTerm) ||
                            book.year.toString().includes(searchTerm) ||
                            book.language.toLowerCase().includes(searchTerm) ||
                            book.subject.toLowerCase().includes(searchTerm);

                        const matchesFilters = (!filters.year.length || filters.year.includes(book.year.toString())) &&
                            (!filters.author.length || filters.author.some(author => book.creators.map(creator => creator.toLowerCase()).includes(author))) &&
                            (!filters.language.length || filters.language.includes(book.language.toLowerCase())) &&
                            (!filters.subject.length || filters.subject.includes(book.subject.toLowerCase())) &&
                            (!filters.publisher.length || filters.publisher.includes(book.publisher.toLowerCase()));

                        return matchesSearchTerm && matchesFilters;
                    }});

                    const booksContainer = document.getElementById('books');
                    booksContainer.innerHTML = '';
                    filteredBooks.forEach(book => {{
                        const bookDiv = document.createElement('div');
                        bookDiv.className = 'book';

                        const thumbnail = document.createElement('div');
                        thumbnail.className = 'thumbnail';
                        const img = document.createElement('img');
                        img.src = book.thumbnail;
                        img.alt = book.title;
                        thumbnail.appendChild(img);
                      
                        const title = document.createElement('div');
                        title.className = 'book-title';
                        title.textContent = book.title;
                        thumbnail.appendChild(title);
                        bookDiv.appendChild(thumbnail);
                        const detailsTooltip = document.createElement('div');
                        detailsTooltip.className = 'details-tooltip';
                        detailsTooltip.innerHTML = `
                            <div class="details">
                                <h3>${{book.title}}</h3>
                                <p><strong>Author:</strong> ${{book.creators.join(', ')}}</p>
                                <p><strong>Publisher:</strong> ${{book.publisher}}</p>
                                <p><strong>Year:</strong> ${{book.year}}</p>
                                <p><strong>Language:</strong> ${{book.language}}</p>
                                <p><strong>Subject:</strong> ${{book.subject}}</p>
                                <a href="${{book.pdf_url}}" target="_blank">Download</a>
                            </div>
                        `;
                        bookDiv.appendChild(detailsTooltip);

                        bookDiv.addEventListener('mouseover', () => {{
                            detailsTooltip.style.display = 'flex';
                        }});
                        bookDiv.addEventListener('mouseout', () => {{
                            detailsTooltip.style.display = 'none';
                        }});

                        booksContainer.appendChild(bookDiv);
                    }});
                }}

                    function searchBooks() {{
                        const searchQuery = document.getElementById('search-books').value.toLowerCase();
                        const books = document.querySelectorAll('.book');
                        books.forEach(book => {{
                            const bookTitle = book.querySelector('.details h3').textContent.toLowerCase();
                            if (bookTitle.includes(searchQuery)) {{
                                book.style.display = 'block';
                            }} else {{
                                book.style.display = 'none';
                            }}
                        }});
                    }}

                document.querySelectorAll('.filters input[type="checkbox"]').forEach(checkbox => {{
                    checkbox.addEventListener('change', filterBooks);
                }});

                loadBooks();
            }});

            function clearFilters() {{
                document.querySelectorAll('.filters input[type="checkbox"]').forEach(checkbox => {{
                    checkbox.checked = false;
                }});
                document.getElementById('search-books').value = '';
                loadBooks();
            }}
            document.getElementById('search-books').addEventListener('input',searchBooks);

            document.getElementById('search-books').addEventListener('keydown',function(event){{
                if(event.key === 'Enter'){{
                    searchBooks();
                }}
            }});

            document.getElementById('clear-filters').addEventListener('click',clearFilters);
            loadBooks();
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
