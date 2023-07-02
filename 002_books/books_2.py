from typing import Optional
from fastapi import FastAPI, Body, Path
from pydantic import BaseModel, Field


app = FastAPI()


class Book:
    id = int
    title = str
    author = str
    description = str
    rating = int
    published_date = int

    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date


class BookRequest(BaseModel):
    id: Optional[int] = Field(title="Este parametro no es requerido")
    title: str = Field(min_length=3)
    author: str = Field(min_length=10)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)
    published_date: int = Field(gt=1999, lt=2023)

    class Config:
        schema_extra = {
            'example': {
                'title': 'The new morning dev',
                'autor': 'ponsianodeloor',
                'description': 'Una descripcion del libro',
                'rating': 5,
                'published_date': 2020
            }
        }

BOOKS = [
    Book(id=1, title="Computer Science Pro", author="ponsianodeloor", description="A Very important Book", rating=5, published_date=2021),
    Book(2, 'Postgres with Python', 'ponsianodeloor', 'A Database book', 5, 2022),
    Book(3, 'Master in Endpoints', 'ponsianodeloor', 'A Endpoint book', 4, 2022),
    Book(4, 'HP1', 'Author one', 'Book description', 3, 2021),
    Book(5, 'HP2', 'Author two', 'Book description', 3, 2023),
    Book(6, 'HP3', 'Author three', 'Book description', 5, 2024),
]


@app.get("/books")
async def books():
    return BOOKS


@app.get("/book/{book_id}")
async def book(book_id: int = Path(gt=0)):
    for x in BOOKS:
        if x.id == book_id:
            return x


@app.get("/books_by_rating")
async def books_by_rating(rating: int):
    books_filtered = []
    for x in BOOKS:
        if x.rating == rating:
            books_filtered.append(x)
    return books_filtered

@app.get("/books_by_year")
async def books_by_year(year: int):
    books_filtered = []
    for x in BOOKS:
        if x.published_date == year:
            books_filtered.append(x)
    return books_filtered


@app.post("/book/create")
async def create_book(book_request=Body()):
    BOOKS.append(book_request)
    {'message': 'Libro agregado correctamente'}


@app.put("/book/update/")
async def update_book(update_book: BookRequest):
    for x in range(len(BOOKS)):
        if BOOKS[x].id == update_book.id:
            BOOKS[x] = update_book
            return {'message': 'libro actualizado correctamente'}


@app.delete("/book/delete/{book_id}")
async def delete_book(book_id: int = Path(gt=0)):
    for x in range(len(BOOKS)):
        if BOOKS[x].id == book_id:
            BOOKS.pop(x)
            return {'message': 'libro eliminado correctamente'}


@app.post("/book/create_pydantic")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.dict())
    BOOKS.append(find_book_id(new_book))


def find_book_id(book: Book):
    # A una lista se le indica -1 es por que se refiere al último
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book
