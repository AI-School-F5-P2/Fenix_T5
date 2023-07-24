from fastapi import APIRouter
from typing import List
from schema.profesores_schema import *
from model.profesores import Profesores

from db_connection import DataBaseConnection

conn = DataBaseConnection()

# Instancia de Profesores()
profesores_instance = Profesores()

#objeto tipo APIRouter
routerprofesores = APIRouter(prefix="/profesores")


#-----------------------------------------------------------------
# routes
#-----------------------------------------------------------------

# Lee todos los resgistros de la tabla Profesores
@routerprofesores.get("/read")
async def root_profesores():
    """
    Endpoint Read. Lee todos los resgistros de la tabla Profesores
    :return
    """
    items = []
    for data in profesores_instance.read_all_profesores():
        dictionary = {}
        dictionary["profesor_id"] = data[0]
        dictionary["nombre_profesor"] = data[1]
        items.append(dictionary)
    return items


# Crea|Inserta un registro en la tabla Profesores
@routerprofesores.post("/insert")
def insert(profesor_data: ProfesoresSchema):
    """
    Endpoint Create. Crea un registro en la tabla Profesores
    :param profesor_data:ProfesoresSchema
    :return:
    """
    data = profesor_data.dict()
    profesores_instance.insert_profesor(data)
    return {"message": f"Registro añadido exitosamente"}


# Borra un registro específico de la tabla Profesores
@routerprofesores.delete("/delete/{profesor_id}")
def delete(profesor_id: int):
    """
    Endpoint Delete. Borra un registro específico de la tabla Profesores
    :param profesor_id:
    :return:
    """
    profesores_instance.delete(profesor_id)
    return {"message": f"Registro con profesor_id {profesor_id} borrado exitosamente"}


# Actualiza un registro específico de la tabla Profesores
@routerprofesores.put("/update/{profesor_id}")
def update(profesor_id: int, updated_data: ProfesoresSchema):
    """
    Endpoint Update. Actualiza un registro específico de la tabla Profesores
    :param profesor_id: int
    :param updated_data: ProfesoresSchema
    :return:
    """
    profesores_instance.update(profesor_id, updated_data)
    return {"message": f"Registro con profesor_id {profesor_id} modificado exitosamente"}


