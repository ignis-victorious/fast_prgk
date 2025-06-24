#  ___________________
#  Import LIBRARIES
from fastapi import FastAPI
#  Import FILES
#  ___________________

app: FastAPI = FastAPI()


@app.get(path="/")
def read_root():
    return {"Hello": "World"}


# def main():
#     print("Hello from fast-prgk!")


# if __name__ == "__main__":
#     main()

#  ___________________
#  Import LIBRARIES
#  Import FILES
#  ___________________
