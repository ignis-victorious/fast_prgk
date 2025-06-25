#  ___________________
#  Import LIBRARIES
from sqlmodel import SQLModel, Field
#  Import FILES
#  ___________________


class Item(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    price: float
    is_offer: bool = False


# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: bool = False
#     password: str = "Don't show this"


# class ItemResponse(BaseModel):
#     name: str
#     price: float
#     is_offer: bool = False
