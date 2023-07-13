from pydantic import BaseModel
from typing import Optional

class ProfesoresClasesSchema(BaseModel):
    profesor_id: int
    clase_id: int


