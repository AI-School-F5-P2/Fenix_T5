from pydantic import BaseModel
from typing import Optional

class ProfesoresSchema(BaseModel):
    nombre_profesor: str


