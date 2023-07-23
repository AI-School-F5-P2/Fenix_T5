from fastapi import APIRouter
from typing import List
from schema.clases_schema import *
from model.clases import Clases

from db_connection import DataBaseConnection

conn = DataBaseConnection()

# Instancia de Clases()
clases_instance = Clases()

#objeto tipo APIRouter
routerclase = APIRouter(prefix="/clases")



#-----------------------------------------------------------------
# routes
#-----------------------------------------------------------------

# Lee todos los registros de la tabla Clases
@routerclase.get("/read")
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
        dictionary["pack"] = data[4]
        items.append(dictionary)
    return items


# Crea|Inserta una clase en la tabla Clases
@routerclase.post("/insert")
def insert(clase_data: ClasesSchema):
    """
    Endpoint Create. Crea un registro en la tabla Clases
    :param clase_data:ClasesSchema
    :return:
    """
    data = clase_data.dict()
    clases_instance.insert(data)
    return {"message": f"Registro añadido exitosamente"}


@routerclase.delete("/delete/{clase_id}")
def delete(clase_id: int):
    """
    Endpoint Delete. Borra el registro específico de la tabla Clase
    :param clase_id:
    :return:
    """
    clases_instance.delete(clase_id)
    return {"message": f"Registro con clase_id {clase_id} borrado exitosamente"}


@routerclase.put("/update/{clase_id}")
def update(clase_id: int, updated_data: ClasesSchema):
    """
    Endpoint Update. Actualiza un registro específico de la tabla Clase
    :param clase_id:
    :param updated_data:
    :return:
    """
    clases_instance.update(clase_id, updated_data)
    return {"message": f"Registro con clase_id {clase_id} modificado exitosamente"}
