from pydantic import BaseModel, fields
from typing import Optional

class AlumnosSchema(BaseModel):
    nombre_alumno: str
    apellidos_alumno: str
    edad_alumno: int
    telefono_alumno: str
    email_alumno: str
    familiar: bool = fields.Field(default=False)
    #clase_id: int


class AlumnosUpdateSchema(BaseModel):
    nombre_alumno: str
    apellidos_alumno: str
    edad_alumno: int
    telefono_alumno: str
    email_alumno: str

