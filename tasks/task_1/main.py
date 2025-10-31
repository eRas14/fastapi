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

from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/", tags=["Задача 1"], summary="Создайте корневой эндпоинт GET /, который возвращает ")
def get_message():
    return {"message": "Hellow World!"}





if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

