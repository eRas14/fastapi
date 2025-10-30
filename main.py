from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()


books = [
    {"id": 1, "name": "Как стать душой компании", "Author": "Василий Коклюшкин"},
    {"id": 2, "name": "Прометей", "Author": "Диана Власова"}
]


@app.get("/books", tags=["Книги"], summary="Получить все книги")
def all_books():
    return books

@app.get("/books/{book_id}", tags=["Книги"], summary="Получить конкретную книгу")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Книга не найдена")

class newBook(BaseModel):
    name: str
    Author: str

@app.post("/books", tags=["Добавление книги"], summary="Добавление книги")
def create_book(new_book: newBook):
    books.append(
        {   "id": len(books) + 1, 
            "name": new_book.name,
            "Author": new_book.Author
            }
    )
    return {"success": True, "message": "Книга успешно добавлена" }




if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)