from fastapi import FastAPI

app = FastAPI()


@app.get("/first")
async def root():
    return "hi "