from fastapi import FastAPI

app = FastAPI()

app.title = "Mi primera aplicacion con FastAPI"
app.version = "0.0.1"

@app.get("/", tags=["Home"])
def home():
    return {"Hola Mundo" : "desde FastAPI por neftali"}

