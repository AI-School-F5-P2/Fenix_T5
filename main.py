from fastapi import FastAPI
#from model.user_connection import UserConnection
from db_connection import DataBaseConnection
from schema.clases_schema import ClasesSchema


app = FastAPI()
try:
    conn = DataBaseConnection()
    print("Se conectó la BD")
except:
    print("No Se conectó la BD")


@app.get("/")
async def root():
    items = []
    for data in conn.read_all_clases():
        dictionary = {}
        dictionary["clase_id"] = data[0]
        dictionary["nombre_clase"] = data[1]
        dictionary["nivel_clase"] = data[2]
        dictionary["precio_clase"] = data[3]
        items.append(dictionary)
    return items


@app.post("/api/insert")
def insert(clase_data:ClasesSchema):
    data = clase_data.dict()
    data.pop("clase_id")
    conn.write(data)