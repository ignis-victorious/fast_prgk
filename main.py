#  ___________________
#  Import LIBRARIES
from fastapi import FastAPI

#  Import FILES
from models.models import Item
#  ___________________

app: FastAPI = FastAPI()


@app.get(path="/")
def read_root() -> dict[str, str]:
    return {"Hello": "World"}


#  POST
@app.post(path="/items/")
def create_item(item: Item) -> dict[str, str | Item]:
    return {"message": "item created", "item": item}


# def main():
#     print("Hello from fast-prgk!")


# if __name__ == "__main__":
#     main()

#  ___________________
#  Import LIBRARIES
#  Import FILES
#  ___________________
