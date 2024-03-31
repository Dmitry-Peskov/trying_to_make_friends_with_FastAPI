from fastapi import FastAPI
import uvicorn
from api_v1 import api_v1_router


app = FastAPI(
    title="Peskov-API",
    version="0.1.0",
    summary="Знакомлюсь с возможностями фреймворка FastAPI",
)
app.include_router(api_v1_router)


@app.get("/", summary="Стартовая страница", tags=["Главная"])
def index():
    return {"status": 200, "message": "Добро пожаловать в Peskov-API"}


if __name__ == "__main__":
    uvicorn.run("app:app", reload=True)
