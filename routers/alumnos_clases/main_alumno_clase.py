from fastapi import APIRouter
from typing import List
from schema.alumnos_clases_schema import *
from model.alumnos_clases import AlumnosClases

from db_connection import DataBaseConnection

conn = DataBaseConnection()

# Instancia de Alumnos()
alumnos_clases_instance = AlumnosClases()

#objeto tipo APIRouter
routeralumnos_clases = APIRouter(prefix="/alumnos_clases")


#-----------------------------------------------------------------
# routes
#-----------------------------------------------------------------

# Lee todos los resgistros de la tabla Alumnos_clases
@routeralumnos_clases.get("/read")
async def root_alumnos():
    """
    Endpoint Read. Lee todos los resgistros de la tabla Alumnos_clases
    :return
    """
    items = []
    for data in alumnos_clases_instance.read_all_alumnos_clases():
        dictionary = {}
        dictionary["alumno_id"] = data[0]
        dictionary["clase_id"] = data[1]
        items.append(dictionary)
    return items

@routeralumnos_clases.post("/insert")
def insert(alumno_data: AlumnosClasesSchema):
    """
    Endpoint Create. Crea un registro en la tabla Alumnos_clases
    :param alumno_data: AlumnosClasesSchema
    :return:
    """
    data = alumno_data.dict()
    alumnos_clases_instance.insert_alumno_clase(data)
    return {"message": f"Registro añadido exitosamente"}


@routeralumnos_clases.delete("/delete/{alumno_id}/{clase_id}")
def delete(alumno_id: int, clase_id: int):
    """
    Endpoint Delete. Borra el registro específico de la tabla Alumnos_clases
    :param alumno_id:
    :param clase_id:
    :return:
    """
    alumnos_clases_instance.delete(alumno_id, clase_id)
    return {"message": f"Registro con alumno_id  borrado exitosamente"}

