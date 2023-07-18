from pydantic import BaseModel
from typing import Optional

class AlumnosSchema(BaseModel):
    nombre_alumno: str
    apellidos_alumno: str
    edad_alumno: int
    telefono_alumno: str
    email_alumno: str
    clase_id: int


class AlumnosUpdateSchema(BaseModel):
    nombre_alumno: str
    apellidos_alumno: str
    edad_alumno: int
    telefono_alumno: str
    email_alumno: str

