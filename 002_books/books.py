from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title one', 'author': 'Author one', 'category': 'Compute'},
    {'title': 'Title two', 'author': 'Author two', 'category': 'Compute'},
    {'title': 'Title three', 'author': 'Author three', 'category': 'History'},
    {'title': 'Title four', 'author': 'Author four', 'category': 'History'},
    {'title': 'Title five', 'author': 'Author five', 'category': 'Math'},
    {'title': 'Title six', 'author': 'Author six', 'category': 'Math'},
]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get('/book/{book_title}')
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
        else:
            return {'book': 'El libro no se encuentra en la lista'}


@app.get('/books_by_category')
async def read_books_by_category(category: str):
    books_by_category = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_by_category.append(book)
    return books_by_category


@app.get('/books_by_author_and_category/{author}')
async def read_book_by_author_and_category(author: str, category: str):
    books_by_author_and_category = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold() and \
                book.get('category').casefold() == category.casefold():
            books_by_author_and_category.append(book)

    if len(books_by_author_and_category) > 0:
        return books_by_author_and_category
    else:
        return {'message': 'No existen libros'}
