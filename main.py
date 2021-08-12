from fastapi import FastAPI
import helper
from Model import Item
import psycopg2
from psycopg2.extras import RealDictCursor

mydb = psycopg2.connect(
  "host=ec2-44-196-250-191.compute-1.amazonaws.com user=pwhrwzbpsucdgt "
  "password=0630fecbf0e7373fe314f3ab92751d811d23b4c507219e53c654fac03c265502 dbname=d34jeb751p3qko"
)

mycursor = mydb.cursor(cursor_factory=RealDictCursor)

app = FastAPI()


@app.get("/")
async def root():
    status = helper.isStatusOK(mycursor)
    closeConn()
    return {"HasInternet": status}


@app.post("/")
async def create_user(item: Item):
    helper.updateData(mycursor, item.randomId)
    mydb.commit()
    mydb.close()
    return item

def closeConn():
    mydb.close()