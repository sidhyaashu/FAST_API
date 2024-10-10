from fastapi import FastAPI , Response ,status ,HTTPException
from pydantic import BaseModel
from typing import Optional
from random import randrange

import psycopg2
from psycopg2.extras import RealDictCursor
import time


app = FastAPI()

class Post(BaseModel):  # Schema creation
    title: str
    content: str
    published: bool = True  # default setting

while True:
    try:
        conn = psycopg2.connect(host="localhost",database="fastapi",user="postgres",password="9749571885",cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Connected to database")
        break
    except Exception as e:
        print("Database connection failed")
        print(e)
        time.sleep(5)


# Request to GET method http://127.0.0.1:8000
@app.get("/")
async def root():
    return {"message": "Hi my name is Sidhya"}


# GET all posts http://127.0.0.1:8000/posts
@app.get("/posts")
async def get_data():
    cursor.execute(""" SELECT * FROM posts """)
    posts = cursor.fetchall()
    return {"data": posts}


# POST a new post http://127.0.0.1:8000/post
@app.post("/post",status_code=status.HTTP_201_CREATED)
async def create_post(post: Post):
    cursor.execute(""" INSERT INTO posts (title,content,published) VALUES(%s, %s, %s) RETURNING * """,
                              (post.title,post.content,post.published))
    new_post = cursor.fetchone()
    conn.commit()
    return {"data": new_post}



#GET http://127.0.0.1:8000/post/4
@app.get("/post/{id}")
async def get_post(id:int):
    cursor.execute(""" SELECT * FROM posts WHERE id = %s """,(str(id),))
    get_post = cursor.fetchone()
    if not get_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post {id} not found")
    return {"data":get_post}


#DELETE http://127.0.0.1:8000/post/2
@app.delete("/post/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id:int):
    cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""",(str(id),))
    deleted_post = cursor.fetchone()
    print(delete_post)
    conn.commit()
    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post {id} not found")
    else:
        return {"deleted ":deleted_post}
    

#UPDATE http://127.0.0.1:8000/post/4
@app.put("/post/{id}",status_code=status.HTTP_202_ACCEPTED)
async def update_post(id:int,post:Post):
    cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING * """,
                   (post.title,post.content,post.published,str(id)))
    updated_post = cursor.fetchone()
    conn.commit()
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post {id} not found")
    else:
        return {"data":updated_post}