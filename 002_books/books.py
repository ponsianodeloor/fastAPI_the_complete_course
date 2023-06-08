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
