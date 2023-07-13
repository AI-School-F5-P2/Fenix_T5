from pydantic import BaseModel
from typing import Optional

class ProfesoresSchema(BaseModel):
    profesor_id: Optional[int]
    nombre_profesor: str


