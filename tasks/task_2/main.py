"""
Задание 2: Работа с Query-параметрами
Цель: Научиться обрабатывать параметры, передаваемые в URL.

Задача:
1. Создайте эндпоинт GET /items/.
2. Реализуйте возможность принимать два необязательных query-параметра: skip (целое число, по умолчанию 0) и limit (целое число, по умолчанию 10).
3. Эндпоинт должен возвращать JSON вида {"skip": skip, "limit": limit}.
4. Проверьте его работу, обратившись по адресу /items/?skip=5&limit=20.

"""

from fastapi import FastAPI
import uvicorn
from data import peoples

app = FastAPI()

@app.get("/items", tags=["Задача 2.1"], summary="Реализуйте возможность принимать два необязательных query-параметра")
def get_items(skip: int = 0, limit: int = 10):
    return peoples[skip:skip + limit]

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)