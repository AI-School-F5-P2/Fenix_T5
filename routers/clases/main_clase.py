from fastapi import APIRouter
from typing import List
from schema.clases_schema import *
from model.clases import Clases
from logger_api import setup_logger
import logging

# Configurar el logger
logger = setup_logger('fenix.log')

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
    logger.info(msg="Lee todos los registros de la tabla Clases")
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
    logger.info(msg="Endpoint insert. Crea un registro en la tabla Clases")
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
    logger.info(msg=f"Borra el registro {clase_id} en la tabla Clases")
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
    logger.info(msg=f"Actualiza el registro { clase_id} en la tabla Clases")
    clases_instance.update(clase_id, updated_data)
    return {"message": f"Registro con clase_id {clase_id} modificado exitosamente"}


# Busca y muestra todas las clases que tiene un profesor dado
@routerclase.get("/buscar_clases/{profesor_id}")
async def clases_profesores(profesor_id: int):
    """
    Endpoint. Busca y muestra todas las clases que tiene un profesor dado
    :return
    """
    logger.info(msg=f"Muestra todas las clases que tiene el profesor: {profesor_id} en la tabla Clases")
    items = []
    for data in clases_instance.clases_por_profesor(profesor_id= profesor_id):
        dictionary = {}
        dictionary["nombre_clase"] = data[0]
        dictionary["nivel_clase"] = data[1]
        dictionary["pack_clase"] = data[2]
        items.append(dictionary)
    return items

