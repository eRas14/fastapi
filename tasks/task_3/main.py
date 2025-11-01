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
from data import items_for_sale
from pydantic import BaseModel, Field

app = FastAPI()

data = {

    "name": "1234567890123245",
    "description": "LED лампа с регулируемой яркостью",
    "price": 0,
    "tax": 5

}

class ItemsSchema(BaseModel):
    name: str = Field(max_length=15)
    description: str | None = Field(None, max_length=100)
    price: float = Field(ge=0)
    tax: float | None = Field(10.5)

items = []

@app.get("/items", tags=["Задача 3.1"], summary="Получение данных")
def get_items():
    return items


@app.post("/items", tags=["Задача 3"], summary="Создание Pydanic модели")
def post_items(item: ItemsSchema):
    items.append(item)
    return {"success": True, "message": "Данные добавлены", "Итоговая стоимость": f"{item.tax + item.price} рублей"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)