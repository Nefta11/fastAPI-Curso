# Proyecto FastAPI

Este es un proyecto básico utilizando FastAPI.

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/Nefta11/fastAPI-Curso.git
    cd fastAPI-Curso
    ```

2. Crea un entorno virtual y actívalo:
    ```bash
    python -m venv env
    .\venv\Scripts\activate  # En Windows usa `env\Scripts\activate`
    ```

3. Instala las dependencias:
    ```bash
    pip install fastapi uvicorn
    ```

## Ejecución

Para ejecutar la aplicación, usa el siguiente comando:
```bash
uvicorn main:app --reload
```

La aplicación estará disponible en `http://127.0.0.1:8000`.

## Endpoints

### GET /

Retorna un mensaje de bienvenida.

- **URL**: `/`
- **Método**: `GET`
- **Respuesta exitosa**:
    - **Código**: 200
    - **Contenido**:
        ```json
        {
            "Hola Mundo": "desde FastAPI por neftali"
        }
        ```

## Recursos

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Uvicorn Documentation](https://www.uvicorn.org/)
