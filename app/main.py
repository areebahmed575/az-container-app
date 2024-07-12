from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/about")
def about():
    return {"Insitute": "Piaic"}


@app.get("/me")
def me():
    return {"name": "Areeb Ahmed"}
