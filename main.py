from fastapi import FastAPI
import helper
from Model import Item
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()


@app.get("/")
async def root():
    myDb, myCursor = openDatabaseConnection()
    status = helper.isStatusOK(myCursor)
    closeConn(myDb)
    return {"HasInternet": status}


@app.post("/")
async def create_user(item: Item):
    myDb, myCursor = openDatabaseConnection()
    helper.updateData(myCursor, item.randomId)
    myDb.commit()
    closeConn(myDb)
    return item


def openDatabaseConnection():
    myDb = psycopg2.connect(
        "host=ec2-44-196-250-191.compute-1.amazonaws.com user=pwhrwzbpsucdgt "
        "password=0630fecbf0e7373fe314f3ab92751d811d23b4c507219e53c654fac03c265502 dbname=d34jeb751p3qko"
    )
    myCursor = myDb.cursor(cursor_factory=RealDictCursor)

    return myDb, myCursor


def closeConn(myDb):
    myDb.close()
