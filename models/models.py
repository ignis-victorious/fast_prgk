#  ___________________
#  Import LIBRARIES
from pydantic import BaseModel
#  Import FILES
#  ___________________


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False
    password: str = "Don't show this"
