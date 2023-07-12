from pydantic import BaseModel
from typing import Optional

class AlumnosSchema(BaseModel):
    alumno_id: Optional[int]
    nombre_alumno: str
    apellidos_alumno: str
    edad_alumno: int
    telefono_alumno: str
    email_alumno: str
