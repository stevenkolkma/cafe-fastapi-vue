from pydantic import BaseModel

class DrinkBase(BaseModel):
    name:str
    price:int
    description:str

class DrinkCreate(DrinkBase):
    pass

class Drink(DrinkBase):
    cafe_id: int

    class Config:
        orm_mode = True

class CafeBase(BaseModel):
    name: str
    address: str

class CafeCreate(CafeBase):
    pass

class Cafe(CafeBase):
    # cafes: list[Drink] = []

    class Config:
        orm_mode = True
