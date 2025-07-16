from fastapi import FastAPI

api = FastAPI()

@api.get("/")
def hello():
    return {"name": "John Doe"}

@api.get("/score")
def testfn():
    return {"player": "Sam", "Score": 56}
