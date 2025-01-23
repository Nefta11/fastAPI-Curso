from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()  # Instancia de la clase FastAPI

app.title = "Mi primera aplicacion con FastAPI"  # Titulo de la API
app.version = "0.0.1"  # Version de la API

movies = [
    {
        "id": 1,
        "title": "Spiderman",
        "overview": "Un adolescente que es mordido por una araña y adquiere poderes de araña",
        "year": 2002,
        "rating": 7.3,
        "category": "Terror",
    },
    {
        "id": 2,
        "title": "Spiderman 2",
        "overview": "Peter Parker lucha con su vida personal y su vida como Spiderman",
        "year": 2004,
        "rating": 7.3,
        "category": "Accion",
    },
]


@app.get("/", tags=["Home"])  # Decorador para definir la ruta de la API
def home():  # Funcion que se ejecutara al ingresar a la ruta
    return {"Hola Mundo": "desde FastAPI por neftali"}  # Respuesta de la API


@app.get("/movies", tags=["Home"])
def Getmovies():
    return movies


@app.get("/movies/{movie_id}", tags=["Home"])  # Parametro de la ruta: Son valores que se envian a traves de la URL y se definen entre llaves
def Getmovies(id: int):
    for movie in movies:
        if movie["id"] == id:
            return movie
    return {"message": "Pelicula no encontrada"}


# Parametros Query: Es una forma de enviar parametros a la API a traves de la URL
@app.get("/movies/", tags=["Home"])
def get_movie_by_category(category: str):
    for movie in movies:
        if movie["category"] == category:
            return movie
    return {"message": "Pelicula no encontrada"}
