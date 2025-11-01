"""
Задание 3: Создание и валидация данных с Pydantic
Цель: Познакомиться с Pydantic моделями для валидации и сериализации данных.

Задача:
1. Создайте Pydantic-модель Item со следующими полями: name (строка, обязательно), description (строка, необязательно), price (положительное число, обязательно), tax (необязательное число с плавающей точкой).
2. Создайте эндпоинт POST /items/, который принимает тело запроса в виде модели Item.
3. Эндпоинт должен возвращать полученные данные. Реализуйте логику: если tax не передан, установите его в 10.5. Затем верните item и рассчитанную итоговую цену price + tax.

"""

from fastapi import FastAPI
import uvicorn
from data import peoples
from pydantic import BaseModel

app = FastAPI()


class ItemsSchema(BaseModel):
    name: str
    description: str | None
    price: int
    tax: float | None

    

@app.get("/items", tags=["Задача 3.1"], summary="Создание Pydanic модели")
class ItemSchema()
def get_items(skip: int = 0, limit: int = 10):
    return peoples[skip:skip + limit]