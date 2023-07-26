from fastapi import APIRouter
from typing import List
from schema.profesores_clases_schema import *
from model.profesores_clases import ProfesoresClases
from logger_api import setup_logger
from db_connection import DataBaseConnection

# Configurar el logger
logger = setup_logger('fenix.log')


conn = DataBaseConnection()

# Instancia de Profesores()
profesores_clases_instance = ProfesoresClases()

#objeto tipo APIRouter
routerprofesores_clases = APIRouter(prefix="/profesores_clases")


#-----------------------------------------------------------------
# routes
#-----------------------------------------------------------------

# Lee todos los resgistros de la tabla Profesores_clases
@routerprofesores_clases.get("/read")
async def root_profesores_clases():
    """
    Endpoint Read. Lee todos los resgistros de la tabla Profesores_clases
    :return
    """
    logger.info(msg="Lee todos los registros de la tabla Profesores_clases")
    items = []
    for data in profesores_clases_instance.read_all_profesores_clases():
        dictionary = {}
        dictionary["profesor_id"] = data[0]
        dictionary["clase_id"] = data[1]
        items.append(dictionary)
    return items


# Crea|Inserta un registro en la tabla Profesores_clases
@routerprofesores_clases.post("/insert")
def insert(profesor_data: ProfesoresClasesSchema):
    """
    Endpoint Create. Crea un registro en la tabla Profesores_clases
    :param clase_data:ProfesoresClasesSchema
    :return:
    """
    logger.info(msg="Crea un registro en la tabla Profesores_clases")
    data = profesor_data.dict()
    profesores_clases_instance.insert_profesor_clase(data)
    return {"message": f"Registro añadido exitosamente"}


# Borra un registro específico de la tabla Profesores_clases
@routerprofesores_clases.delete("/delete/{profesor_id}/{clase_id}")
def delete(profesor_id: int, clase_id: int):
    """
    Endpoint Delete. Borra un registro específico de la tabla Profesores_clases
    :param profesor_id:
    :param clase_id:
    :return:
    """
    logger.info(msg=f"Borra un registro en la tabla Profesores_clases")
    profesores_clases_instance.delete(profesor_id, clase_id)
    return {"message": f"Registro con profesor_id {profesor_id} y clase_id {clase_id} borrado exitosamente"}
