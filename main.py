from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()  # Instancia de la clase FastAPI

app.title = "Mi primera aplicacion con FastAPI"  # Titulo de la API
app.version = "0.0.1"  # Version de la API

movies = [
    {
        "id" : 1,
        "title" : "Spiderman",
        "overview" : "Un adolescente que es mordido por una araña y adquiere poderes de araña",
        "year" : 2002,
        "rating" : 7.3,
        "category" : "Accion"
    },
]

@app.get("/", tags=["Home"])  # Decorador para definir la ruta de la API
def home():  # Funcion que se ejecutara al ingresar a la ruta
    return {"Hola Mundo": "desde FastAPI por neftali"}  # Respuesta de la API


@app.get("/movies", tags=["Home"])
def Getmovies():
    return movies
