from typing import Optional
from fastapi import FastAPI, Body, Path, Query, HTTPException
from pydantic import BaseModel, Field
from starlette import status

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


@app.get("/books", status_code=status.HTTP_200_OK)
async def books():
    return BOOKS


@app.get("/book/{book_id}", status_code=status.HTTP_200_OK)
async def book(book_id: int = Path(gt=0)):
    for x in BOOKS:
        if x.id == book_id:
            return x
    raise HTTPException(status_code=400, detail='Libro no encontrado')


@app.get("/books_by_rating", status_code=status.HTTP_200_OK)
async def books_by_rating(rating: int = Query(gt=0, lt=6)):
    books_filtered = []
    for x in BOOKS:
        if x.rating == rating:
            books_filtered.append(x)
    return books_filtered

@app.get("/books_by_year", status_code=status.HTTP_200_OK)
async def books_by_year(year: int = Query(gt=1999, lt=2023)):
    books_filtered = []
    for x in BOOKS:
        if x.published_date == year:
            books_filtered.append(x)
    return books_filtered


@app.post("/book/create", status_code=status.HTTP_201_CREATED)
async def create_book(book_request=Body()):
    BOOKS.append(book_request)
    {'message': 'Libro agregado correctamente'}


@app.put("/book/update/", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(update_book: BookRequest):
    book_change = False
    for x in range(len(BOOKS)):
        if BOOKS[x].id == update_book.id:
            BOOKS[x] = update_book
            book_change = True
            break
    if book_change:
        raise HTTPException(status_code=204, detail='Libro actualizado correctamente')
    else:
        raise HTTPException(status_code=404, detail='Libro no encontrado')


@app.delete("/book/delete/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    book_change = False
    for x in range(len(BOOKS)):
        if BOOKS[x].id == book_id:
            BOOKS.pop(x)
            book_change = True
            break
    if book_change:
        raise HTTPException(status_code=204, detail='Libro eliminado correctamente')
    else:
        raise HTTPException(status_code=404, detail='Libro no encontrado')


@app.post("/book/create_pydantic")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.dict())
    BOOKS.append(find_book_id(new_book))


def find_book_id(book: Book):
    # A una lista se le indica -1 es por que se refiere al último
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book
