from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional


app = FastAPI()

class Post(BaseModel): #Schema creation
    title:str
    content:str
    published:bool = True #default setting
    rating: Optional[int] = None






# Request to GET methode
@app.get("/")
async def root():
    return {"message":"Hi my name is sidhya"}



# @app.post("/post")
# async def create_post(payload:dict=Body(...)):
#     print(payload)
#     return {"new_post":f"title: {payload["title"]} & content: {payload["content"]}"}


@app.post("/post")
async def create_post(new_post:Post):
    print(new_post)
    print(new_post.model_dump()) 
    return {"data":f"title: {new_post.title} & content: {new_post.content}"}