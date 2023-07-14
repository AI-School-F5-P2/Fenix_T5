from fastapi import  FastAPI
from model.user_connection import UserConnection

# instanciamos la clase
app  = FastAPI()
conn = UserConnection()

#creamos un decorador que se ejecute mediante el método get desde la ruta base de la app
@app.get("/")
def root():
    conn
    return "Hi, I am FastAPI"
