from fastapi import FastAPI
from db_connection import DataBaseConnection
from schema.clases_schema import *
from schema.alumnos_schema import *
from schema.alumnos_clases_schema import *
from schema.profesores_schema import *
from model.clases import Clases
from model.alumnos import Alumnos
from model.alumnos_clases import AlumnosClases
from model.profesores import Profesores

app = FastAPI()
conn = DataBaseConnection()
clases_instance = Clases()
alumnos_instance = Alumnos()
alumnos_clases_instance = AlumnosClases()
profesores_instance = Profesores()


# Endpoints para tabla Clases
@app.get("/clases/read")
async def root():
    """
    Endpoint Read. Lee todos los resgistros de la tabla Clases
    :return
    """
    items = []
    for data in clases_instance.read_all_clases():
        dictionary = {}
        dictionary["clase_id"] = data[0]
        dictionary["nombre_clase"] = data[1]
        dictionary["nivel_clase"] = data[2]
        dictionary["precio_clase"] = data[3]
        items.append(dictionary)
    return items


@app.post("/clases/insert")
def insert(clase_data: ClasesSchema):
    """
    Endpoint Create. Crea un registro en la tabla Clases
    :param clase_data:condauvicorn
    :return:
    """
    data = clase_data.dict()
    clases_instance.insert(data)
    return {"message": f"Registro añadido exitosamente"}

@app.delete("/clases/delete/{clase_id}")
def delete(clase_id: int):
    """
    Endpoint Delete. Borra el registro específico de la tabla Clase
    :param clase_id:
    :return:
    """
    clases_instance.delete(clase_id)
    return {"message": f"Registro con clase_id {clase_id} borrado exitosamente"}

@app.put("/clases/update/{clase_id}")
def update(clase_id: int, updated_data: UpdateClasesSchema):
    """
    Endpoint Update. Actualiza un registro específico de la tabla Clase
    :param clase_id:
    :param updated_data:
    :return:
    """
    clases_instance.update(clase_id, updated_data)
    return {"message": f"Registro con clase_id {clase_id} modificado exitosamente"}


# Endpoints para tabla alumnos

@app.get("/alumnos/read")
async def root_alumnos():
    """
    Endpoint Read. Lee todos los resgistros de la tabla Alumnos
    :return
    """
    items = []
    for data in alumnos_instance.read_all_alumnos():
        dictionary = {}
        dictionary["alumno_id"] = data[0]
        dictionary["nombre_alumno"] = data[1]
        dictionary["apellido_alumno"] = data[2]
        dictionary["edad_alumno"] = data[3]
        dictionary["telefono_alumno"] = data[4]
        dictionary["email_alumno"] = data[5]
        items.append(dictionary)
    return items

@app.post("/alumnos/insert")
def insert_alumnos(alumno_data: AlumnosSchema):
    """
    Endpoint Create. Crea un registro en la tabla Alumnos
    :param clase_data:AlumnosSchema
    :return:
    """
    data = alumno_data.dict()
    data.pop("alumno_id")
    alumnos_instance.insert_alumno(data)
    return {"message": f"Registro añadido exitosamente"}

@app.delete("/alumnos/delete/{alumno_id}")
def delete(alumno_id: int):
    """
    Endpoint Delete. Borra el registro específico de la tabla Alumnos
    :param alumno_id:
    :return:
    """
    alumnos_instance.delete(alumno_id)
    return {"message": f"Registro con alumno_id {alumno_id} borrado exitosamente"}

@app.put("/alumnos/update/{alumno_id}")
def update(alumno_id: int, updated_data: AlumnosUpdateSchema):
    """
    Endpoint Update. Actualiza un registro específico de la tabla Alumnos
    :param alumno_id:
    :param updated_data:
    :return:
    """
    alumnos_instance.update(alumno_id, updated_data)
    return {"message": f"Registro con alumno_id {alumno_id} modificado exitosamente"}

# Endpoints para tabla Alumnos_clases *************************

@app.get("/alumnos_clases/read")
async def root_alumnos():
    """
    Endpoint Read. Lee todos los resgistros de la tabla Alumnos_clases
    :return
    """
    items = []
    for data in alumnos_clases_instance.read_all_alumnos_clases():
        dictionary = {}
        dictionary["alumno_id"] = data[0]
        dictionary["clase_id"] = data[1]
        items.append(dictionary)
    return items

@app.post("/alumnos_clases/insert")
def insert(alumno_data: AlumnosClasesSchema):
    """
    Endpoint Create. Crea un registro en la tabla Alumnos_clases
    :param clase_data:AlumnosClases
    :return:
    """
    data = alumno_data.dict()
    #data.pop("alumno_id")
    alumnos_clases_instance.insert_alumno_clase(data)
    return {"message": f"Registro añadido exitosamente"}


@app.delete("/alumnos_clases/delete/{alumno_id}/{clase_id}")
def delete(alumno_id: int, clase_id: int):
    """
    Endpoint Delete. Borra el registro específico de la tabla Alumnos_clases
    :param alumno_id:
    :param clase_id:
    :return:
    """
    alumnos_clases_instance.delete(alumno_id, clase_id)
    return {"message": f"Registro con alumno_id  borrado exitosamente"}



# Endpoints para tabla Profesores *************************

@app.get("/profesores/read")
async def root_profesores():
    """
    Endpoint Read. Lee todos los resgistros de la tabla Profesores
    :return
    """
    items = []
    for data in profesores_instance.read_all_profesores():
        dictionary = {}
        dictionary["profesor_id"] = data[0]
        dictionary["nombre_profesor"] = data[1]
        items.append(dictionary)
    return items

@app.post("/profesores/insert")
def insert(profesor_data: ProfesoresSchema):
    """
    Endpoint Create. Crea un registro en la tabla Profesores
    :param profesor_data:ProfesoresSchema
    :return:
    """
    data = profesor_data.dict()
    profesores_instance.insert_profesor(data)
    return {"message": f"Registro añadido exitosamente"}

@app.delete("/profesores/delete/{profesor_id}")
def delete(profesor_id: int):
    """
    Endpoint Delete. Borra el registro específico de la tabla Profesores
    :param profesor_id:
    :return:
    """
    profesores_instance.delete(profesor_id)
    return {"message": f"Registro con profesor_id {profesor_id} borrado exitosamente"}

@app.put("/profesores/update/{profesor_id}")
def update(profesor_id: int, updated_data: ProfesoresSchema):
    """
    Endpoint Update. Actualiza un registro específico de la tabla Profesores
    :param profesor_id:
    :param updated_data:
    :return:
    """
    profesores_instance.update(profesor_id, updated_data)
    return {"message": f"Registro con profesor_id {profesor_id} modificado exitosamente"}