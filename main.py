from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

class ResponseDTO(BaseModel):
    code: int
    message:str
    data: object
    
    
class Cat(BaseModel):
    name : str
    id : int =0

app = FastAPI()


@app.get("/first/{id}")
async def root(id : int):
    return {"message":"hello" , "id" : id}

@app.get("/second")
async def second(skip:int =0,limit:int=10):
    return {"skip":skip,"limit":limit}


@app.post("/cat")
async def cat(cat: Cat):
    return cat


@app.get("/error")
async def error():
    dto=ResponseDTO(
        code=1,
        message="aa",
        data=None
    )
    return JSONResponse(status_code=404, content=jsonable_encoder(dto))

@app.get("/error1")
async def error1():
    return HTTPException(status_code=404, detail={"Message":"Item not found1"})
