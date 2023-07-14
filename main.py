from fastapi import FastAPI
from db_connection import DataBaseConnection
from schema.clases_schema import *
from schema.alumnos_schema import *
from model.clases import Clases
from model.alumnos import Alumnos

app = FastAPI()
conn = DataBaseConnection()
clases_instance = Clases()
alumnos_instance = Alumnos()

@app.get("/")
async def root():
    """
    Endpoint Read. Lee todos los resgistros de la tabla Clases
    :return
    """
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
    """
    Endpoint Create. Crea un registro en la tabla Clases
    :param clase_data:condauvicorn
    :return:
    """
    data = clase_data.dict()
    data.pop("clase_id")
    clases_instance.insert(data)
    return {"message": f"Registro añadido exitosamente"}

@app.delete("/delete/{clase_id}")
def delete(clase_id: int):
    """
    Endpoint Delete. Borra el registro específico de la tabla Clase
    :param clase_id:
    :return:
    """
    clases_instance.delete(clase_id)
    return {"message": f"Registro con clase_id {clase_id} borrado exitosamente"}

@app.put("/update/{clase_id}")
def update(clase_id: int, updated_data: UpdateClasesSchema):
    """
    Endpoint Update. Actualiza un registro específico de la tabla Clase
    :param clase_id:
    :param updated_data:
    :return:
    """
    clases_instance.update(clase_id, updated_data)
    return {"message": f"Registro con clase_id {clase_id} modificado exitosamente"}


# Endpoints para tabla alumnos

@app.get("/alumnos/")
async def root_alumnos():
    """
    Endpoint Read. Lee todos los resgistros de la tabla Alumnos
    :return
    """
    items = []
    for data in alumnos_instance.read_all_alumnos():
        dictionary = {}
        dictionary["alumno_id"] = data[0]
        dictionary["nombre_alumno"] = data[1]
        dictionary["apellido_alumno"] = data[2]
        dictionary["edad_alumno"] = data[3]
        dictionary["telefono_alumno"] = data[4]
        dictionary["email_alumno"] = data[5]
        items.append(dictionary)
    return items

@app.post("/alumnos/insert")
def insert_alumnos(alumno_data: AlumnosSchema):
    """
    Endpoint Create. Crea un registro en la tabla Alumnos
    :param clase_data:AlumnosSchema
    :return:
    """
    data = alumno_data.dict()
    data.pop("alumno_id")
    alumnos_instance.insert_alumno(data)
    return {"message": f"Registro añadido exitosamente"}

@app.delete("/alumnos/delete/{alumno_id}")
def delete(alumno_id: int):
    """
    Endpoint Delete. Borra el registro específico de la tabla Alumnos
    :param clase_id:
    :return:
    """
    alumnos_instance.delete(alumno_id)
    return {"message": f"Registro con alumno_id {alumno_id} borrado exitosamente"}