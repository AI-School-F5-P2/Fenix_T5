from fastapi import FastAPI
from db_connection import DataBaseConnection
from schema.clases_schema import *
from model.clases import Clases

app = FastAPI()
conn = DataBaseConnection()
clases_instance = Clases()

@app.get("/")
async def root():
    items = []
    for data in clases_instance.read_all_clases():
        dictionary = {}
        dictionary["clase_id"] = data[0]
        dictionary["nombre_clase"] = data[1]
        dictionary["nivel_clase"] = data[2]
        dictionary["precio_clase"] = data[3]
        items.append(dictionary)
    return items


@app.post("/insert")
def insert(clase_data: ClasesSchema):
    data = clase_data.dict()
    data.pop("clase_id")
    clases_instance.insert(data)
    return {"message": f"Registro añadido exitosamente"}

@app.delete("/delete/{clase_id}")
def delete(clase_id: int):
    clases_instance.delete(clase_id)
    return {"message": f"Registro con clase_id {clase_id} borrado exitosamente"}

@app.put("/update/{clase_id}")
def update(clase_id: int, updated_data: UpdateClasesSchema):
    clases_instance.update(clase_id, updated_data)
    return {"message": f"Registro con clase_id {clase_id} modificado exitosamente"}



