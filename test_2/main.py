from utils import students_list
from fastapi import FastAPI, HTTPException
from typing import Optional
import uvicorn

app = FastAPI()

@app.get("/")
def home_page():
    return {"message": "Привет, Хабр!"}

@app.get('/api/v1/students', tags=["Получение списка всех студентов"])
def get_students():
    return students_list

# #Получение студента по Айди
# @app.get('/students/{stud_id}', tags=["Получение студента по id"], summary="Получение студента по id")
# def get_student(stud_id: int):
#     for student in students_list:
#         if student["student_id"] == stud_id:
#             return student
#     raise HTTPException(status_code=404, detail=f"Студент с id={stud_id} не найден")
    
# #Получение всех студентов с определенным курсом    
# @app.get('/students/', tags=["Получение всех студетов с определенным курсом"], summary="Получение всех студетов с определенным курсом")
# def get_student(course_id: int):
#     courses_list = []
#     for student in students_list:
#         if student["course"] == course_id:
#             courses_list.append(student)    
#     if not courses_list:
#         raise HTTPException(status_code=404, detail=f"Такого курса не существует")
#     return courses_list
    

@app.get('/students/', tags=["Получение всех студетов с определенным курсом или дефолт"], summary="Получение всех студетов с определенным курсом")
def get_student(course: Optional[int] = None):
    if course is None:
        return students_list
    else:
        courses_list = []
        for student in students_list:
            if student["course"] == course:
                courses_list.append(student)    
        if not courses_list:
            raise HTTPException(status_code=404, detail=f"Такого курса не существует")
        return courses_list
    


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)