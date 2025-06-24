#  ___________________
#  Import LIBRARIES
from fastapi import FastAPI

#  Import FILES
from models.models import Item, ItemResponse
#  ___________________

app: FastAPI = FastAPI()


@app.get(path="/")
def read_root() -> dict[str, str]:
    return {"Hello": "World"}


#  POST - works with: {"name": "erre","price": 100,"is_offer": false,"password": "Don't show this"} or {"name": "elle", "price": 1000, "is_offer": true,"password": "Show this"}
@app.post(path="/items/", response_model=ItemResponse)
def create_item(item: Item) -> Item:
    return item


# Aslo this works
# @app.post(path="/items/", response_model=ItemResponse)
# def create_item(item: Item) -> ItemResponse:
#     return ItemResponse(**item.model_dump())


# def main():
#     print("Hello from fast-prgk!")


# if __name__ == "__main__":
#     main()

#  ___________________
#  Import LIBRARIES
#  Import FILES
#  ___________________
