import datetime
from pydantic import BaseModel
from typing import Optional

class PagosSchema(BaseModel):
    alumno_id: int
    clase_id: int
    fecha_pago: datetime.date



