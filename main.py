from fastapi import FastAPI
from starlette.responses import RedirectResponse


from db_connection import DataBaseConnection

#objetos de apirouter a incluir
from routers.clases import main_clase as mainclase
from routers.alumnos import main_alumno as main_alumnno
from routers.alumnos_clases import main_alumno_clase as main_alumno_clase
from routers.profesores import main_profesor as main_profesor
from routers.profesores_clases import main_profesor_clase as main_profesores_clase
from routers.pagos import main_pago as main_pago


# Se crea objeto FastAPI
app = FastAPI(title="FastApi Danza Fénix",
              description="Simple rest-full api with postgreSQL",
              version="1.0")

# Se incluyen los objetos de APIROUTER
app.include_router(mainclase.routerclase)
app.include_router(main_alumnno.routeralumno)
app.include_router(main_alumno_clase.routeralumnos_clases)
app.include_router(main_profesor.routerprofesores)
app.include_router(main_profesores_clase.routerprofesores_clases)
app.include_router(main_pago.routerpagos)


#route index para redireccionar a la documentacion
# @app.get("/")
# async def main():
#     return RedirectResponse(url="/docs/")


