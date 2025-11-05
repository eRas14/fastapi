from fastapi import FastAPI, HTTPException
from data import students
import uvicorn

app = FastAPI()

@app.get("/")
def start_page():
    return {"status": "ok"}

@app.get("/api/v1/students", tags=["Student list"])
def get_students():
    return students 

@app.get("/api/v1/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["student_id"] == student_id:
            return student
    raise HTTPException(status_code=404, detail="Студент с таким id не найдет")
        


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)