"""

Задание 1: "Hello, World!" и основы маршрутизации
Цель: Создать базовое приложение FastAPI и понять, как работают эндпоинты.

Задача:
1. Создайте новый файл main.py.
2. Импортируйте FastAPI и создайте экземпляр приложения.
3. Создайте корневой эндпоинт GET /, который возвращает {"message": "Hello, World!"}.
4. Создайте еще один эндпоинт GET /users/{user_id}, который принимает путь user_id (целое число) и возвращает {"user_id": user_id}.
5. Запустите сервер с помощью uvicorn main:app --reload и проверьте оба эндпоинта в браузере.

"""

from fastapi import FastAPI, HTTPException
from data import peoples
import uvicorn

app = FastAPI()


@app.get("/peoples", tags=["Задача 1.1"], summary="Вовзращает список людей")
def get_peoples():
    return peoples

@app.get("/people{people_id}", tags=["Задача 1.2"], summary="Вовзращает человека по id")
def get_people(people_id: int):
    for people in peoples:
        if people["id"] == people_id:
            return people
    raise HTTPException(status_code=404, detail="Не найдет человек с таким id")



if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

