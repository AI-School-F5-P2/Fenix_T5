from fastapi import APIRouter
from typing import List
from schema.pagos_schema import *
from model.pagos import Pagos
from db_connection import DataBaseConnection

conn = DataBaseConnection()

# Instancia de Profesores()
pagos_instance = Pagos()

#objeto tipo APIRouter
routerpagos = APIRouter(prefix="/pagos")


#-----------------------------------------------------------------
# routes
#-----------------------------------------------------------------


# Lee todos los resgistros de la tabla Pagos
@routerpagos.get("/read")
async def root_pagos():
    """
    Endpoint Read. Lee todos los resgistros de la tabla Pagos
    :return
    """
    items = []
    for data in pagos_instance.read_all_pagos():
        dictionary = {}
        dictionary["pago_id"] = data[0]
        dictionary["importe_pagado"] = data[1]
        dictionary["alumno_id"] = data[2]
        dictionary["clase_id"] = data[3]
        dictionary["fecha_pago"] = data[4]
        items.append(dictionary)
    return items


# Crea|Inserta un registro en la tabla Pagos
@routerpagos.post("/pagos/insert")
def insert(pago_data: PagosSchema):
    """
    Endpoint Create. Crea un registro en la tabla Pagos
    :param profesor_data:PagosSchema
    :return:
    """
    data = pago_data.dict()
    pagos_instance.insert(data)
    return {"message": f"Registro añadido exitosamente"}

# Borra un registro específico de la tabla Pagos
@routerpagos.delete("/delete/{pago_id}")
def delete(pago_id: int):
    """
    Endpoint Delete. Borra un registro específico de la tabla Pagos
    :param pago_id:
    :return:
    """
    pagos_instance.delete(pago_id)
    return {"message": f"Registro con pago_id {pago_id} borrado exitosamente"}


# Actualiza un registro específico de la tabla Pagos
@routerpagos.put("/update/{pago_id}")
def update(pago_id: int, updated_data: PagosSchema):
    """
    Endpoint Update. Actualiza un registro específico de la tabla Pagos
    :param pago_id: int
    :param updated_data: PagosSchema
    :return:
    """
    pagos_instance.update(pago_id, updated_data)
    return {"message": f"Registro con pago_id {pago_id} modificado exitosamente"}


# Obtiene todos los registros de la tabla Pagos para un alumno_id dado.
@routerpagos.get("/alumno/{alumno_id}")
def get_pagos_by_alumno_id(alumno_id: int):
    """
        Obtiene todos los registros de la tabla Pagos para un alumno_id dado.
    """
    items = []
    for data in pagos_instance.pagos_by_alumnos(alumno_id):
        dictionary = {}
        dictionary["alumno_id_id"] = data[0]
        dictionary["clase_id"] = data[1]
        dictionary["importe_pagado"] = data[2]
        dictionary["fecha_pago"] = data[3]
        items.append(dictionary)
    return items


# Obtiene el total que ha pagado un alumno
@routerpagos.get("/alumno/importe_total/{alumno_id}")
def get_total_pagado_por_alumno(alumno_id: int):
    """
        Obtiene la suma total que ha pagado un alumno.
    """
    total_pagado = pagos_instance.total_pagado_alumno(alumno_id)
    return total_pagado

