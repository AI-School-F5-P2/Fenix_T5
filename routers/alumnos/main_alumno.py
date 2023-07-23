from fastapi import APIRouter
from typing import List
from schema.alumnos_schema import *
from model.alumnos import Alumnos

from db_connection import DataBaseConnection

conn = DataBaseConnection()

# Instancia de Alumnos()
alumnos_instance = Alumnos()

#objeto tipo APIRouter
routeralumno = APIRouter(prefix="/alumnos")


#-----------------------------------------------------------------
# routes
#-----------------------------------------------------------------

# Lee todos los registros de la tabla Alumnos
@routeralumno.get("/read")
async def root_alumnos():
    """
    Endpoint Read. Lee todos los registros de la tabla Alumnos
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
        dictionary["familiar"] = data[6]
        items.append(dictionary)
    return items

# Crea|Inserta un registro en la tabla Alumnos
@routeralumno.post("/insert")
def insert_alumnos(alumno_data: AlumnosSchema):
    """
    Endpoint Create. Crea un registro en la tabla Alumnos
    :param clase_data:AlumnosSchema
    :return:
    """
    data = alumno_data.dict()
    alumnos_instance.insert_alumno(data)
    return {"message": f"Registro añadido exitosamente"}


# Borra un registro específico de la tabla Alumnos
@routeralumno.delete("/delete/{alumno_id}")
def delete(alumno_id: int):
    """
    Endpoint Delete. Borra un registro específico de la tabla Alumnos
    :param alumno_id:
    :return:
    """
    alumnos_instance.delete(alumno_id)
    return {"message": f"Registro con alumno_id {alumno_id} borrado exitosamente"}


# Actualiza un registro específico de la tabla Alumnos
@routeralumno.put("/update/{alumno_id}")
def update(alumno_id: int, updated_data: AlumnosSchema):
    """
    Endpoint Update. Actualiza un registro específico de la tabla Alumnos
    :param alumno_id:
    :param updated_data:
    :return:
    """
    alumnos_instance.update(alumno_id, updated_data)
    return {"message": f"Registro con alumno_id {alumno_id} modificado exitosamente"}

