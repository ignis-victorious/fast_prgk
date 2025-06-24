#  ___________________
#  Import LIBRARIES
from fastapi import FastAPI
#  Import FILES
#  ___________________

app: FastAPI = FastAPI()


@app.get(path="/")
def read_root() -> dict[str, str]:
    return {"Hello": "World"}


# PATH Parameters + QUERY parameters - Worls with http://127.0.0.1:8000/items/123?q=erre and http://127.0.0.1:8000/items/12345678
@app.get(path="/items/{item_id}")
def read_item(item_id: int, q: str | None = None) -> dict[str, int | str | None]:
    return {"item id": item_id, "query": q}


# # PATH Parameters ONLY - works with http://127.0.0.1:8000/items/12345678
# @app.get(path="/items/{item_id}")
# def read_item(item_id: int) -> dict[str, int]:
#     return {"item id": item_id}


#  OPTIONAL params - works with http://127.0.0.1:8000/products/, http://127.0.0.1:8000/products/?skip=11&limit=9
@app.get(path="/products/")
def list_products(skip: int = 0, limit: int = 10) -> dict[str, int]:
    return {"skip": skip, "limit": limit}


# def main():
#     print("Hello from fast-prgk!")


# if __name__ == "__main__":
#     main()

#  ___________________
#  Import LIBRARIES
#  Import FILES
#  ___________________

# /fix Expression of type "None" cannot be assigned to parameter of type "str"
#   "None" is not assignable to "str", Default value of type None is not assignable to annotated parameter type str

# You should annotate the parameter q as Optional[str] (or str | None in Python 3.10+) to allow None as a valid default value.
