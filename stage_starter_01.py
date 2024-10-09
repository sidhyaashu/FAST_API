from fastapi import FastAPI,status
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Post(BaseModel): #Schema creation
    title:str
    content:str
    published:bool = True #default setting
    rating: Optional[int] = None

my_data = [{"title":"books 1", "content":"Hey this book is so good","id":1},{"title":"books 2", "content":"Hey this book is so good","id":2},{"title":"books 3", "content":"Hey this book is so good","id":3}]

# Request to GET methode http://127.0.0.1:8000
@app.get("/")
async def root():
    return {"message":"Hi my name is sidhya"}


# http://127.0.0.1:8000/post
@app.get("/post")
async def grt_data():
    return {"data":my_data}

# http://127.0.0.1:8000/post
# @app.post("/post")
# async def create_post(payload:dict=Body(...)):
#     print(payload)
#     return {"new_post":f"title: {payload["title"]} & content: {payload["content"]}"}

# http://127.0.0.1:8000/post
@app.post("/post",status_code=status.HTTP_201_CREATED)
async def create_post(new_post: Post):
    post_dict = new_post.model_dump()  # Correct usage, dump the instance
    post_dict["id"] = randrange(0, 100000)  # Add random ID
    my_data.append(post_dict)
    return {"data": post_dict}



