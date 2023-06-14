from fastapi import FastAPI

app = FastAPI()


class Book:
    id = int
    name = str
    author = str
    description = str
    rating = int

    def __init__(self, id, name, author, description, rating):
        self.id = id
        self.name = name
        self.author = author
        self.description = description
        self.rating = rating


BOOKS = [
    Book(id=1, name="Computer Science Pro", author="ponsianodeloor", description="A Very important Book", rating=5),
    Book(2, 'Postgres with Python', 'ponsianodeloor', 'A Database book', 5),
    Book(3, 'Master in Endpoints', 'ponsianodeloor', 'A Endpoint book', 5),
    Book(4, 'HP1', 'Author one', 'Book description', 5),
    Book(5, 'HP2', 'Author two', 'Book description', 5),
    Book(6, 'HP3', 'Author three', 'Book description', 5),
]


@app.get("/books")
async def books():
    return BOOKS
