from fastapi import FastAPI
from fastapi.params import Body
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

# POST a new post http://127.0.0.1:8000/post
@app.post("/post")
async def create_post(new_post: Post = Body(...)):  # Using Body for POST request
    post_dict = new_post.model_dump()  # Dump the instance
    post_dict["id"] = randrange(0, 100000)  # Add random ID
    my_data.append(post_dict)
    return {"data": post_dict}

# Run the app with: uvicorn filename:app --reload
