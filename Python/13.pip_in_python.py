from fastapi import FastAPI
from uvicorn import run as app_run

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    app_run(app, host="0.0.0.0", port=8080)