from typing import Optional
from fastapi import FastAPI, Body
from pydantic import BaseModel, Field


app = FastAPI()


class Book:
    id = int
    title = str
    author = str
    description = str
    rating = int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


class BookRequest(BaseModel):
    id: Optional[int]
    title: str = Field(min_length=3)
    author: str = Field(min_length=10)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)


BOOKS = [
    Book(id=1, title="Computer Science Pro", author="ponsianodeloor", description="A Very important Book", rating=5),
    Book(2, 'Postgres with Python', 'ponsianodeloor', 'A Database book', 5),
    Book(3, 'Master in Endpoints', 'ponsianodeloor', 'A Endpoint book', 5),
    Book(4, 'HP1', 'Author one', 'Book description', 5),
    Book(5, 'HP2', 'Author two', 'Book description', 5),
    Book(6, 'HP3', 'Author three', 'Book description', 5),
]


@app.get("/books")
async def books():
    return BOOKS


@app.post("/book/create")
async def create_book(book_request=Body()):
    BOOKS.append(book_request)
    {'message': 'Libro agregado correctamente'}


@app.post("/book/create_pydantic")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.dict())
    BOOKS.append(find_book_id(new_book))


def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book
