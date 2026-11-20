from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "welcome to FastAPI"}

books = [
    {
        "id": 1,
        "title": "Think Python",
        "author": "Allen B. Downey",
        "publisher": "O'Reilly Media",
        "published_date": "2021-01-01",
        "page_count": 1234,
        "language": "English",
    },
    {
        "id": 2,
        "title": "Django By Example",
        "author": "Antonio Mele",
        "publisher": "Packt Publishing Ltd",
        "published_date": "2022-01-19",
        "page_count": 1023,
        "language": "English",
    },
    {
        "id": 3,
        "title": "The web socket handbook",
        "author": "AlexDiaconu",
        "publisher": "Xinyu Wang",
        "published_date": "2021-01-01",
        "page_count": 3677,
        "language": "English"
    },
    {
        "id": 4,
        "title": "Head first Javascript",
        "author": "Hellen Smith",
        "publisher": "Oreilly Media",
        "published_date": "2021-01-01",
        "page_count": 540,
        "language": "English",
    },
    {
        "id": 5,
        "title": "Algorithms and Data Structures in Python",
        "author": "Kent Lee",
        "publisher": "Springer Inc",
        "published_date": "2021-01-01",
        "page_count": 9282,
        "language": "English"
    },
    {
        "id": 6,
        "title": "Head First HTML5 Programming",
        "author": "Eric T Freeman",
        "publisher": "Oreilly Media",
        "published_date": "2011-21-01",
        "page_count": 3006,
        "language": "English"
    },
]

# BaseModel turns Book class into a strict runtime data validator
class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str

# make all fields optional so the client only has to send what they want to change
class Book_Update_Model(BaseModel):
    title: str | None = None
    author: str | None = None
    publisher: str | None = None
    page_count: int | None = None
    language: str | None = None

# get all books
@app.get("/books", response_model=List[Book])
async def get_all_books():
    return books

# create a book
@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data: Book):
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book

# get one book
@app.get("/books/{book_id}", response_model=Book)
async def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with ID {book_id} not found")


# partial update with patch
@app.patch("/books/{book_id}", response_model=Book)
async def update_book(book_id: int, book_update_data: Book_Update_Model):
    for book in books:
        if book["id"] == book_id:
            # extract only the fields the client actually sent in the JSON body
            update_dict = book_update_data.model_dump(exclude_unset=True)

            # merge those updated key value pairs directly into the existing book dictionary
            book.update(update_dict)
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


# delete book
@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return None

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with ID {book_id} not found")
