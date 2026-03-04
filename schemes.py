from pydantic import BaseModel

class ProductCreate(BaseModel):
    name:str
    description:str|None=None
    price:int

class ProductResponse(BaseModel):
    id :int

    class Config:
        from_attributes=True


