from utils import students_list
from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()

@app.get('/students', tags=["Получение списка всех студентов"], summary="Получение всех студентов")
def get_students():
    return students_list


@app.get('/students/{stud_id}', tags=["Получение студента по id"], summary="Получение студента по id")
def get_student(stud_id: int):
    for student in students_list:
        if student["student_id"] == stud_id:
            return student
    raise HTTPException(status_code=404, detail=f"Студент с id={stud_id} не найден")
    



if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)