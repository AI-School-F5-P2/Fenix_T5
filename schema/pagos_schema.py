import datetime

from pydantic import BaseModel
from typing import Optional

class PagosSchema(BaseModel):
    importe_pagado: float
    alumno_id: int
    clase_id: int
    fecha_pago: datetime.date

