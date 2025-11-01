from fastapi import FastAPI, HTTPException
import uvicorn
from data import students
from typing import Literal
from pydantic import BaseModel, Field
app = FastAPI()

#Получение списка студентов
@app.get("/students", tags=["Получение списка студентов"],summary="Получение списка", description="Получение всего списка студентов методом GET")
def get_students():
    return students

#Получение студента по id
@app.get("/students/{student_id}", tags=["Получение студента по id"],summary="Получение списка по id", description="Получение студента по id ")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student
    raise HTTPException(status_code=404, detail="Студент с таким id не найден")

#Добавление студента
class StudentSchema(BaseModel):
    name: str = Field(max_length=20, description="Имя студента, максимум 20 символов")
    surname: str = Field(max_length=20,description="Фамилия студента, максимум 20 символов")
    age: int = Field(ge=18, le=85, description="Возраст студента, от 18 до 85 лет")
    country: str = Field(max_length=20, description="Страна студента")
    gender: Literal["м", "ж"]

@app.post("/students/", tags=["Добавление студента"],summary="Добавление студента", description="Добавление студента по полям")
def post_student(student: StudentSchema):
    students.append({
        "id": len(students) + 1,
        "name": student.name,
        "surname": student.surname,
        "age": student.age,
        "country": student.country,
        "gender": student.gender
    })
    return {"success": True, "message": "Студент добавлен"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

