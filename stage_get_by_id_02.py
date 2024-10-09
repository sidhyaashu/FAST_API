from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Post(BaseModel):  # Schema creation
    title: str
    content: str
    published: bool = True  # default setting
    rating: Optional[int] = None

my_data = [
    {"title": "books 1", "content": "Hey this book is so good", "id": 1},
    {"title": "books 2", "content": "Hey this book is so good", "id": 2},
    {"title": "books 3", "content": "Hey this book is so good", "id": 3}
]


def find_post_by_id(id):
    for p in my_data:
        if p["id"] == id:
            return p
        

# Request to GET method http://127.0.0.1:8000
@app.get("/")
async def root():
    return {"message": "Hi my name is Sidhya"}


# GET all posts http://127.0.0.1:8000/post
@app.get("/post")
async def get_data():
    return {"data": my_data}


# POST a new post http://127.0.0.1:8000/post
@app.post("/post")
async def create_post(new_post: Post):
    post_dict = new_post.model_dump()  # Correct usage, dump the instance
    post_dict["id"] = randrange(0, 100000)  # Add random ID
    my_data.append(post_dict)
    return {"data": post_dict}

# http://127.0.0.1:8000/post/latest
@app.get("/post/latest")
async def get_latest():
    x = my_data[len(my_data)-1]
    return {"data":x}

#Get single posts http://127.0.0.1:8000/post/1
@app.get("/post/{id}")
async def get_post(id:int):
    x = find_post_by_id(id)
    return {"data":x}