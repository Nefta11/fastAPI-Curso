from fastapi import FastAPI

app = FastAPI()     # Instancia de la clase FastAPI

app.title = "Mi primera aplicacion con FastAPI" # Titulo de la API
app.version = "0.0.1" # Version de la API

@app.get("/", tags=["Home"])  # Decorador para definir la ruta de la API
def home():    # Funcion que se ejecutara al ingresar a la ruta
    return {"Hola Mundo" : "desde FastAPI por neftali"} # Respuesta de la API

