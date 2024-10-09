from fastapi import FastAPI , Response ,status ,HTTPException

app = FastAPI()


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


#Get single posts http://127.0.0.1:8000/post/1
@app.get("/post/{id}")
async def get_post(id:int,response:Response):
    x = find_post_by_id(id)
    if not x:
        # response.status_code = 404
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message":f"Post id {id} was not found"}
    return {"data":x}


#Alternate 
@app.get("/post/{id}")
async def get_post(id:int):
    x = find_post_by_id(id)
    if not x:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post {id} not found")
    return {"data":x}