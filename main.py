from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()


books = [
    {"id": 1, "name": "Как стать душой компании", "Author": "Василий Коклюшкин"},
    {"id": 2, "name": "Прометей", "Author": "Диана Власова"}
]


@app.get("/books", tags=["Книги"], summary="Книги в вродаже")
def all_books():
    return books

@app.get("/books/{book_id}", tags=["Книги"], summary="Книги в вродаже")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Книга не найдена")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)