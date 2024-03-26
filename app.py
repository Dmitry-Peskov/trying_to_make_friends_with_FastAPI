from fastapi import FastAPI
import uvicorn
from api_v1 import api_v1_router


app = FastAPI()
app.include_router(api_v1_router)


@app.get("/")
def index():
    return {"status": 200, "message": "Welcome!"}


if __name__ == "__main__":
    uvicorn.run("app:app", reload=True)
