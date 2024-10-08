from fastapi import FastAPI


app = FastAPI()

# Request to GET methode
@app.get("/")
async def root():
    return {"message":"Hi my name is sidhya"}

@app.get("/log")
async def root():
    return {"message":"This is log "}

@app.get("/post")
async def root():
    return {"data":"This is data "}