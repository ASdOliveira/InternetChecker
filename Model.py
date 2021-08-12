from pydantic import BaseModel


class Item(BaseModel):
    randomId: str
