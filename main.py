from fastapi import FastAPI
from starlette.responses import RedirectResponse
#from typing import List

from db_connection import DataBaseConnection
# from schema.clases_schema import *
# from schema.alumnos_schema import *
# from schema.alumnos_clases_schema import *
# from schema.profesores_schema import *
# from schema.profesores_clases_schema import *
# from schema.pagos_schema import *

# from model.clases import Clases
# from model.alumnos import Alumnos
# from model.alumnos_clases import AlumnosClases
# from model.profesores import Profesores
# from model.profesores_clases import ProfesoresClases
# from model.pagos import Pagos

#objetos de apirouter a incluir
from routers.clases import main_clase as mainclase
from routers.alumnos import main_alumno as main_alumnno
from routers.alumnos_clases import main_alumno_clase as main_alumno_clase
from routers.profesores import main_profesor as main_profesor
from routers.profesores_clases import main_profesor_clase as main_profesores_clase
from routers.pagos import main_pago as main_pago

# Se crea objeto FastAPI
app = FastAPI(title="FastApi Danza Fénix",
              description="Simple rest-full api with postreSQL",
              version="1.0")

# Se incluyen los objetos de APIROUTER
app.include_router(mainclase.routerclase)
app.include_router(main_alumnno.routeralumno)
app.include_router(main_alumno_clase.routeralumnos_clases)
app.include_router(main_profesor.routerprofesores)
app.include_router(main_profesores_clase.routerprofesores_clases)
app.include_router(main_pago.routerpagos)


#route index para redireccionar a la documentacion
@app.get("/")
async def main():
    return RedirectResponse(url="/docs/")

# conn = DataBaseConnection()
#
# # Creación de instancias
# clases_instance = Clases()
# alumnos_instance = Alumnos()
# alumnos_clases_instance = AlumnosClases()
# profesores_instance = Profesores()
# profesores_clases_instance = ProfesoresClases()
# pagos_instance = Pagos()






# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)