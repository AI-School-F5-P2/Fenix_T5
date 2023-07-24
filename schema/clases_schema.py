from pydantic import BaseModel
from typing import Optional

# Representación de la Tabla Clases
class ClasesSchema(BaseModel):
    nombre_clase: str
    nivel_clase: str
    precio_clase: float
    pack: int

class ClasesPorProfesor(BaseModel):
    nombre_clase: str
    nivel_clase: str
    pack_clase: str