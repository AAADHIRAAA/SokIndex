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
         html, body {{
                height: 100%;
                margin: 0;
                padding: 0;
                display: flex;
                flex-direction: column;
            }}
            body {{
                font-family: Arial, sans-serif;
              
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
               flex: 1;
               
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
                left: calc(-20% - 10px); 
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
                z-index: 9999; 
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
                padding: 5px;
                border-radius: 5px;
                margin-top: 20px;
                position: fixed;
                bottom: 0;
                width: 100%;
            }}
             .show-more {{
            cursor: pointer;
            color: blue;
         
        }}
         #clear-filters-button {{
            margin-bottom: 50px; 
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
        
        <button class="show-more" onclick="toggleYearFilters()">Show More</button>
        
    </div>

    <div class="filter-section" id="filter-section-author">
        <h3>Author</h3>
       
     
        <button class="show-more" onclick="toggleAuthorFilters()">Show More</button>
    </div>

    <div class="filter-section" id="filter-section-lang">
        <h3>Language</h3>
       
        
        <button class="show-more" onclick="toggleLanguageFilters()">Show More</button>
    </div>

    <div class="filter-section" id="filter-section-sub">
        <h3>Subject</h3>
       
       
        <button class="show-more" onclick="toggleSubjectFilters()">Show More</button>
    </div>

    <div class="filter-section" id="filter-section-publisher">
        <h3>Publisher</h3>
       
      
        <button class="show-more" onclick="togglePublisherFilters()">Show More</button>
    </div>

    <button id="clear-filters-button" onclick="clearFilters()">Clear Filters</button>
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
              
                    const booksData = {books_json};

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
          
                  

                loadBooks();
            
               function clearFilters() {{
                document.getElementById('search-books').value = '';
                // Clear other filter inputs here
                 document.querySelectorAll('.filters input[type="checkbox"]').forEach(checkbox => {{
                    checkbox.checked = false;
                }});
                loadBooks(); // Reload books after clearing filters
            }}
                // Initialize filter checkboxes
                    function initializeFilters() {{
                    
                        const filterSectionYear = document.getElementById('filter-section-year');
                        const uniqueYears = [...new Set(booksData.map(book => book.year).filter(year => year !=="N/A" ))];
                        uniqueYears.sort((a,b) => b - a);
                        uniqueYears.slice(0, Math.min(5, uniqueYears.length)).forEach(year => {{
                            const div = document.createElement('div');
                            const input = document.createElement('input');
                            input.type = 'checkbox';
                            input.value = year;
                            input.className = 'filter-checkbox';
                            input.id = `filter-year-${{year}}`;
                            input.addEventListener('change', applyFilters);

                            const label = document.createElement('label');
                            label.htmlFor = `filter-year-${{year}}`;
                            label.textContent = year;

                            div.appendChild(input);
                            div.appendChild(label);
                            filterSectionYear.insertBefore(div, filterSectionYear.querySelector('.show-more'));

                            
                        }});

                         
                        const filterSectionAuthor = document.getElementById('filter-section-author');
                            const uniqueAuthors = [...new Set(booksData.flatMap(book => {{
                                if (Array.isArray(book.creators)) {{
                                    return book.creators.map(author => author.trim());
                                }} else {{
                                    return [];
                                }}
                            }}))];
                      
                       uniqueAuthors.slice(0, Math.min(5,uniqueAuthors.length)).forEach(author => {{
                        const div = document.createElement('div');
                        const input = document.createElement('input');
                        input.type = 'checkbox';
                        input.value = author;
                        input.className = 'filter-checkbox';
                        input.id = `filter-author-${{author}}`;
                        input.addEventListener('change', applyFilters);

                        const label = document.createElement('label');
                        label.htmlFor = `filter-author-${{author}}`;
                        label.textContent = author;

                        div.appendChild(input);
                        div.appendChild(label);
                            filterSectionAuthor.insertBefore(div, filterSectionAuthor.querySelector('.show-more'));
                            }});

                        const filterSectionLanguage = document.getElementById('filter-section-lang');
                        const uniqueLanguages = [...new Set(booksData.map(book => book.language).filter(language => language !=="N/A"))];
                       
                        uniqueLanguages.slice(0, Math.min(5,uniqueLanguages.length)).forEach(language => {{
                            const div = document.createElement('div');
                            const input = document.createElement('input');
                            input.type = 'checkbox';
                            input.value = language;
                            input.className = 'filter-checkbox';
                            input.id = `filter-language-${{language}}`;
                            input.addEventListener('change', applyFilters);

                            const label = document.createElement('label');
                            label.htmlFor = `filter-language-${{language}}`;
                            label.textContent = language;

                            div.appendChild(input);
                            div.appendChild(label);
                            filterSectionLanguage.insertBefore(div, filterSectionLanguage.querySelector('.show-more'));
                            }});

                         const filterSectionPublisher = document.getElementById('filter-section-publisher');
                        const uniquePublishers = [...new Set(booksData.map(book => book.publisher).filter(publisher => publisher !== "N/A"))];
                       
                        uniquePublishers.slice(0, Math.min(5, uniquePublishers.length)).forEach(publisher => {{
                            const div = document.createElement('div');
                            const input = document.createElement('input');
                            input.type = 'checkbox';
                            input.value = publisher;
                            input.className = 'filter-checkbox';
                            input.id = `filter-publisher-${{publisher}}`;
                            input.addEventListener('change', applyFilters);

                            const label = document.createElement('label');
                            label.htmlFor = `filter-publisher-${{publisher}}`;
                            label.textContent = publisher;

                            div.appendChild(input);
                            div.appendChild(label);
                            filterSectionPublisher.insertBefore(div, filterSectionPublisher.querySelector('.show-more'));
                            }});

                         const filterSectionSubject = document.getElementById('filter-section-sub');
                       const uniqueSubjects = [...new Set(booksData.flatMap(book => {{
                            return book.subject.split(';').map(subject => subject.trim()).filter(subject => subject !== "N/A");
                        }}))];

                        // Generate checkboxes for unique subjects, show all if less than 5
                        uniqueSubjects.slice(0, Math.min(5, uniqueSubjects.length)).forEach(subject => {{
                            const div = document.createElement('div');
                            const input = document.createElement('input');
                            input.type = 'checkbox';
                            input.value = subject;
                            input.className = 'filter-checkbox';
                            input.id = `filter-subject-${{subject}}`;
                            input.addEventListener('change', applyFilters);

                            const label = document.createElement('label');
                            label.htmlFor = `filter-subject-${{subject}}`;
                            label.textContent = subject;

                            div.appendChild(input);
                            div.appendChild(label);
                            filterSectionSubject.insertBefore(div, filterSectionSubject.querySelector('.show-more'));
                        }});
                    }}

                   

                     let showAllYears = false;

                    function toggleYearFilters() {{
                        const filterSectionYear = document.getElementById('filter-section-year');
                        filterSectionYear.innerHTML = '<h3>Year</h3>';
                        const uniqueYears = [...new Set(booksData.map(book => book.year).filter(year => year!=="N/A"))];
                        uniqueYears.sort((a,b) => b - a);
                        if (showAllYears) {{
                            uniqueYears.slice(0, Math.min(5,uniqueYears.length)).forEach(year => {{
                                const div = document.createElement('div');
                                const input = document.createElement('input');
                                input.type = 'checkbox';
                                input.value = year;
                                input.className = 'filter-checkbox';
                                input.id = `filter-year-${{year}}`;
                                input.addEventListener('change', applyFilters);

                                const label = document.createElement('label');
                                label.htmlFor = `filter-year-${{year}}`;
                                label.textContent = year;

                                div.appendChild(input);
                                div.appendChild(label);
                                filterSectionYear.insertBefore(div, filterSectionYear.querySelector('.show-more'));
                            }});
                            filterSectionYear.appendChild(createToggleButton('Show More', toggleYearFilters));
                        }} else {{
                            uniqueYears.forEach(year => {{
                                const div = document.createElement('div');
                                const input = document.createElement('input');
                                input.type = 'checkbox';
                                input.value = year;
                                input.className = 'filter-checkbox';
                                input.id = `filter-year-${{year}}`;
                                input.addEventListener('change', applyFilters);

                                const label = document.createElement('label');
                                label.htmlFor = `filter-year-${{year}}`;
                                label.textContent = year;

                                div.appendChild(input);
                                div.appendChild(label);
                                filterSectionYear.insertBefore(div, filterSectionYear.querySelector('.show-more'));
                            }});
                            filterSectionYear.appendChild(createToggleButton('Hide', toggleYearFilters));
                        }}
                        showAllYears = !showAllYears;
                    }}

                    let showAllAuthors = false;

                    function toggleAuthorFilters() {{
                        const filterSectionAuthor = document.getElementById('filter-section-author');
                        filterSectionAuthor.innerHTML = '<h3>Author</h3>';
                        const uniqueAuthors = [...new Set(booksData.flatMap(book => {{
                            if (Array.isArray(book.creators)) {{
                                return book.creators.map(author => author.trim());
                            }} else {{
                                return [];
                            }}
                        }}))];
                        
                        if (showAllAuthors) {{
                            uniqueAuthors.slice(0, Math.min(5,uniqueAuthors.length)).forEach(author => {{
                                const div = document.createElement('div');
                                const input = document.createElement('input');
                                input.type = 'checkbox';
                                input.value = author;
                                input.className = 'filter-checkbox';
                                input.id = `filter-author-${{author}}`;
                                input.addEventListener('change', applyFilters);

                                const label = document.createElement('label');
                                label.htmlFor = `filter-author-${{author}}`;
                                label.textContent = author;

                                div.appendChild(input);
                                div.appendChild(label);
                                filterSectionAuthor.insertBefore(div, filterSectionAuthor.querySelector('.show-more'));
                            }});
                            filterSectionAuthor.appendChild(createToggleButton('Show More', toggleAuthorFilters));
                        }}else {{
                            uniqueAuthors.forEach(author => {{
                                const div = document.createElement('div');
                                const input = document.createElement('input');
                                input.type = 'checkbox';
                                input.value = author;
                                input.className = 'filter-checkbox';
                                input.id = `filter-author-${{author}}`;
                                input.addEventListener('change', applyFilters);

                                const label = document.createElement('label');
                                label.htmlFor = `filter-author-${{author}}`;
                                label.textContent = author;

                                div.appendChild(input);
                                div.appendChild(label);
                                filterSectionAuthor.insertBefore(div, filterSectionAuthor.querySelector('.show-more'));
                            }});
                            filterSectionAuthor.appendChild(createToggleButton('Hide', toggleAuthorFilters));
                        }}
                        showAllAuthors = !showAllAuthors;
                    }}

                    let showAllPublishers = false;

                    function togglePublisherFilters() {{
                        const filterSectionPublisher = document.getElementById('filter-section-publisher');
                        filterSectionPublisher.innerHTML = '<h3>Publisher</h3>';
                        const uniquePublishers = [...new Set(booksData.map(book => book.publisher).filter(publisher => publisher !== "N/A"))];
                        
                        if (showAllPublishers) {{
                            uniquePublishers.slice(0, Math.min(5,uniquePublishers.length)).forEach(publisher => {{
                                const div = document.createElement('div');
                                const input = document.createElement('input');
                                input.type = 'checkbox';
                                input.value = publisher;
                                input.className = 'filter-checkbox';
                                input.id = `filter-publisher-${{publisher}}`;
                                input.addEventListener('change', applyFilters);

                                const label = document.createElement('label');
                                label.htmlFor = `filter-publisher-${{publisher}}`;
                                label.textContent = publisher;

                                div.appendChild(input);
                                div.appendChild(label);
                                filterSectionPublisher.appendChild(div);
                            }});
                            filterSectionPublisher.appendChild(createToggleButton('Show More', togglePublisherFilters));
                        }} else {{
                            uniquePublishers.forEach(publisher => {{
                                const div = document.createElement('div');
                                const input = document.createElement('input');
                                input.type = 'checkbox';
                                input.value = publisher;
                                input.className = 'filter-checkbox';
                                input.id = `filter-publisher-${{publisher}}`;
                                input.addEventListener('change', applyFilters);

                                const label = document.createElement('label');
                                label.htmlFor = `filter-publisher-${{publisher}}`;
                                label.textContent = publisher;

                                div.appendChild(input);
                                div.appendChild(label);
                                filterSectionPublisher.appendChild(div);
                            }});
                            filterSectionPublisher.appendChild(createToggleButton('Hide', togglePublisherFilters));
                        }}
                        showAllPublishers = !showAllPublishers;
                    }}

                    let showAllSubjects = false;

                    function toggleSubjectFilters() {{
                        const filterSectionSubject = document.getElementById('filter-section-sub');
                        filterSectionSubject.innerHTML = '<h3>Subject</h3>';
                        const uniqueSubjects = [...new Set(booksData.flatMap(book => book.subject.split(';').map(subject => subject.trim())).filter(subject => subject !== "N/A"))];
                        
                        if (showAllSubjects) {{
                            uniqueSubjects.slice(0, Math.min(5, uniqueSubjects.length)).forEach(subject => {{
                                const div = document.createElement('div');
                                const input = document.createElement('input');
                                input.type = 'checkbox';
                                input.value = subject;
                                input.className = 'filter-checkbox';
                                input.id = `filter-subject-${{subject}}`;
                                input.addEventListener('change', applyFilters);

                                const label = document.createElement('label');
                                label.htmlFor = `filter-subject-${{subject}}`;
                                label.textContent = subject;

                                div.appendChild(input);
                                div.appendChild(label);
                                filterSectionSubject.appendChild(div);
                            }});
                            filterSectionSubject.appendChild(createToggleButton('Show More', toggleSubjectFilters));
                        }} else {{
                            uniqueSubjects.forEach(subject => {{
                                const div = document.createElement('div');
                                const input = document.createElement('input');
                                input.type = 'checkbox';
                                input.value = subject;
                                input.className = 'filter-checkbox';
                                input.id = `filter-subject-${{subject}}`;
                                input.addEventListener('change', applyFilters);

                                const label = document.createElement('label');
                                label.htmlFor = `filter-subject-${{subject}}`;
                                label.textContent = subject;

                                div.appendChild(input);
                                div.appendChild(label);
                                filterSectionSubject.appendChild(div);
                            }});
                            filterSectionSubject.appendChild(createToggleButton('Hide', toggleSubjectFilters));
                        }}
                        showAllSubjects = !showAllSubjects;
                    }}

                        let showAllLanguages = false;

                        function toggleLanguageFilters() {{
                            const filterSectionLanguage = document.getElementById('filter-section-lang');
                            filterSectionLanguage.innerHTML = '<h3>Language</h3>';
                            const uniqueLanguages = [...new Set(booksData.map(book => book.language).filter(language => language !== "N/A"))];
                            
                            if (showAllLanguages) {{
                                uniqueLanguages.slice(0, Math.min(5, uniqueLanguages.length)).forEach(language => {{
                                    const div = document.createElement('div');
                                    const input = document.createElement('input');
                                    input.type = 'checkbox';
                                    input.value = language;
                                    input.className = 'filter-checkbox';
                                    input.id = `filter-language-${{language}}`;
                                    input.addEventListener('change', applyFilters);

                                    const label = document.createElement('label');
                                    label.htmlFor = `filter-language-${{language}}`;
                                    label.textContent = language;

                                    div.appendChild(input);
                                    div.appendChild(label);
                                    filterSectionLanguage.appendChild(div);
                                }});
                                filterSectionLanguage.appendChild(createToggleButton('Show More', toggleLanguageFilters));
                            }}else {{
                                uniqueLanguages.forEach(language => {{
                                    const div = document.createElement('div');
                                    const input = document.createElement('input');
                                    input.type = 'checkbox';
                                    input.value = language;
                                    input.className = 'filter-checkbox';
                                    input.id = `filter-language-${{language}}`;
                                    input.addEventListener('change', applyFilters);

                                    const label = document.createElement('label');
                                    label.htmlFor = `filter-language-${{language}}`;
                                    label.textContent = language;

                                    div.appendChild(input);
                                    div.appendChild(label);
                                    filterSectionLanguage.appendChild(div);
                                }});
                                filterSectionLanguage.appendChild(createToggleButton('Hide', toggleLanguageFilters));
                            }}
                            showAllLanguages = !showAllLanguages;
                        }}


                   function createToggleButton(text, toggleFunction) {{
                    const button = document.createElement('button');
                    button.className = 'show-more';
                    button.textContent = text;
                    button.onclick = toggleFunction;
                    return button;
                }}

                  
                   
                    function applyFilters() {{
                    const searchInput = document.getElementById('search-books').value.toLowerCase();

                    // Get all checked filters
                    const checkedFilters = Array.from(document.querySelectorAll('.filter-checkbox:checked'));
                    
                    // Extract checked values for each filter type
                    const checkedYears = Array.from(document.querySelectorAll('#filter-section-year .filter-checkbox:checked')).map(checkbox => checkbox.value);
                    const checkedAuthors = Array.from(document.querySelectorAll('#filter-section-author .filter-checkbox:checked')).map(checkbox => checkbox.value);
                    const checkedLanguages = Array.from(document.querySelectorAll('#filter-section-lang .filter-checkbox:checked')).map(checkbox => checkbox.value);
                    const checkedPublishers = Array.from(document.querySelectorAll('#filter-section-publisher .filter-checkbox:checked')).map(checkbox => checkbox.value);
                    const checkedSubjects = Array.from(document.querySelectorAll('#filter-section-sub .filter-checkbox:checked')).map(checkbox => checkbox.value);

                    // Filter books based on search input and checked filters
                    const filteredBooks = booksData.filter(book => {{
                        const matchesSearch = book.title.toLowerCase().includes(searchInput) ||
                            book.creators.some(creator => creator.toLowerCase().includes(searchInput)) ||
                            book.publisher.toLowerCase().includes(searchInput) ||
                            book.language.toLowerCase().includes(searchInput) ||
                            book.subject.toLowerCase().includes(searchInput);

                        const matchesYear = checkedYears.length === 0 || checkedYears.includes(book.year);
                        const matchesAuthor = checkedAuthors.length === 0 || book.creators.some(creator => checkedAuthors.includes(creator.trim()));
                        const matchesLanguage = checkedLanguages.length === 0 || checkedLanguages.includes(book.language);
                        const matchesPublisher = checkedPublishers.length === 0 || checkedPublishers.includes(book.publisher);
                        const matchesSubject = checkedSubjects.length === 0 || checkedSubjects.some(subject => book.subject.split(';').map(s => s.trim()).includes(subject));

                        return matchesSearch && matchesYear && matchesAuthor && matchesLanguage && matchesPublisher && matchesSubject;
                    }});

                    // Update the books display
                    const booksContainer = document.getElementById('books');
                    booksContainer.innerHTML = '';
                    filteredBooks.forEach(book => {{
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

                        const detailsTooltip = document.createElement('div');
                        detailsTooltip.className = 'details-tooltip';
                        const details = document.createElement('div');
                        details.className = 'details';
                        details.innerHTML = `
                            <h3>${{book.title}}</h3>
                            <p><strong>Author:</strong> ${{book.creators.join(', ')}}</p>
                            <p><strong>Publisher:</strong> ${{book.publisher}}</p>
                            <p><strong>Language:</strong> ${{book.language}}</p>
                            <p><strong>Year:</strong> ${{book.year}}</p>
                            <p><strong>Subject:</strong> ${{book.subject}}</p>
                            <a href="${{book.pdf_url}}" target="_blank">Read PDF</a>
                        `;
                        detailsTooltip.appendChild(details);

                        bookDiv.appendChild(thumbnail);
                        bookDiv.appendChild(title);
                        bookDiv.appendChild(detailsTooltip);

                        booksContainer.appendChild(bookDiv);
                    }});
                }}
                
                 document.addEventListener('DOMContentLoaded', () => {{
                    loadBooks();
                    initializeFilters();
                    document.getElementById('search-books').addEventListener('input', applyFilters);
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
