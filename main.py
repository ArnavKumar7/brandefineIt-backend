from fastapi import FastAPI
import database
from pydantic import BaseModel
from typing import Dict, List, Any

app = FastAPI()

class Input(BaseModel):
    id: str
    step: int
    teamname: str
    m1name: str
    m1email: str
    m1phone: str
    m1college: str
    m1usn: str
    m1course: str
    m1sem: str
    m2name: str
    m2email: str
    m2phone: str
    m2college: str
    m2usn: str
    m2course: str
    m2sem: str
    m3name: str
    m3email: str
    m3phone: str
    m3college: str
    m3usn: str
    m3course: str
    m3sem: str
    m4name: str
    m4email: str
    m4phone: str
    m4college: str
    m4usn: str
    m4course: str
    m4sem: str
    transactionId: str

@app.get("/")
def hello_world():
    return {"message": "Hello World"}

@app.post("/create")
def add_user(input: Input):
    database.db.brandefineit.insert_one(input.dict())
    return {"message": "success"}

@app.get("/get")
def get_user():
    l=[]
    users = database.db.brandefineit.find()
    for i in users:
        i['_id']=str(i['_id'])
        l.append(i)
    return l

@app.put('/update')
def update_user(input: Input):
    database.db.brandefineit.update_one({"id":input.id},{"$set":input.dict()})
    return {"message": "success"}