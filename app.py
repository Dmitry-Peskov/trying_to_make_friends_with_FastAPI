from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/")
def index():
    return {"status": 200, "message": "Welcome!"}


if __name__ == "__main__":
    uvicorn.run("app:app", reload=True)
