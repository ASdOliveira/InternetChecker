from fastapi import FastAPI
import helper
from Model import Item
app = FastAPI()
from pydantic import BaseModel


@app.get("/")
async def root():
    status = helper.isStatusOK()

    return {"HasInternet": status}


@app.post("/")
async def create_user(item: Item):
    #helper.updateData(item.randomId)
    return item