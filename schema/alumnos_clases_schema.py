from pydantic import BaseModel
from typing import Optional

class AlumnosClasesSchema(BaseModel):
    alumno_id: int
    clase_id: int

