from pydantic import BaseModel
from typing import Optional

class PagosSchema(BaseModel):
    pago_id: Optional[int]
    importe_pagado: float
    alumno_id: int
    clase_id: int

