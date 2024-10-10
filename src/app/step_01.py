from fastapi import FastAPI , Response ,status ,HTTPException
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
        
def find_index(id):
    for i,p in enumerate(my_data):
        if p["id"] == id:
            return i


# Request to GET method http://127.0.0.1:8000
@app.get("/")
async def root():
    return {"message": "Hi my name is Sidhya"}


# GET all posts http://127.0.0.1:8000/post
@app.get("/post")
async def get_data():
    return {"data": my_data}


# POST a new post http://127.0.0.1:8000/post
@app.post("/post",status_code=status.HTTP_201_CREATED)
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
# @app.get("/post/{id}")
# async def get_post(id:int,response:Response):
#     x = find_post_by_id(id)
#     if not x:
#         # response.status_code = 404
#         response.status_code = status.HTTP_404_NOT_FOUND
#         return {"message":f"Post id {id} was not found"}

#     return {"data":x}

#Alternate
@app.get("/post/{id}")
async def get_post(id:int):
    x = find_post_by_id(id)
    if not x:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post {id} not found")
    return {"data":x}


#delete post
@app.delete("/post/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id:int):
    post = find_post_by_id(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post {id} not found")
    else:
        index = find_index(id)
        my_data.pop(index)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    

#Update 
@app.put("/post/{id}",status_code=status.HTTP_202_ACCEPTED)
async def update_post(id:int,post:Post):
    x = find_index(id)
    if not x:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post {id} not found")
    else:
        post_dict = post.model_dump()
        post_dict["id"] = id
        my_data[x] = post_dict
        return {"data":my_data[x]}