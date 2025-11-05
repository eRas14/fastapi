from fastapi import FastAPI
from data import students
import uvicorn

app = FastAPI()

@app.get("/api/v1/students", tags=["Student list"])
def get_students():
    return students 


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)