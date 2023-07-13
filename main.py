from fastapi import FastAPI
from db_connection import DataBaseConnection
from schema.clases_schema import ClasesSchema
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


@app.post("/api/insert")
def insert(clase_data: ClasesSchema):
    data = clase_data.dict()
    data.pop("clase_id")
    clases_instance.write(data)

