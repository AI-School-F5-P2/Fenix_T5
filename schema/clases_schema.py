from pydantic import BaseModel
from typing import Optional

# Representación de la Tabla Clases
class ClasesSchema(BaseModel):
    clase_id: Optional[int]
    nombre_clase: str
    nivel_clase: str
    precio_clase: float

class UpdateClasesSchema(BaseModel):
    nombre_clase: str
    nivel_clase: str
    precio_clase: float