<!-- Fenix -->
<div align="justify">

<!-- Profile -->
<p align="left"><strong><samp>「</samp></strong></p>
  <p align="center">
    <samp>
      <b>
        Welcome,
      <br>
        We present our project
      </b>🚀
      <br>
      <a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&width=435&lines=Fenix+starting+project..." alt="Typing SVG" /></a>
      <br>
    </samp>

<p align="right"><strong><samp>」</samp></strong></p>

<p align="center">
  <img src="https://github.com/AI-School-F5-P2/Fenix_T5/assets/131301013/a9709c2c-f254-4b5f-9b75-1e38be8e34f6" alt="Fenix" width="200" />
</p>
<br>

</div>

<body>
<samp>
  <h1>🔥 Fenix Team 5</h1>
  <p>Este proyecto tiene como objetivo proporcionar una solución digital y escalable a la gestión de alumnos y cuentas de la escuela de baile "Danza Fénix". La escuela ha experimentado un éxito inesperado, lo que ha llevado a un aumento en la cantidad de alumnos y clases ofrecidas. Sin embargo, la gestión actual se realiza en papel y bolígrafo, lo que resulta en un trabajo arduo, propenso a errores y difícil de mantener.

Para abordar este problema, nuestro equipo de desarrollo ha sido contratado por Mar, la dueña de la escuela, para implementar una base de datos de tipo SQL y una API tipo REST. Esta solución permitirá almacenar de manera eficiente y segura la información de los alumnos, las clases y los profesores, lo que simplificará la gestión de datos y facilitará el proceso de inscripción, modificación de clases, seguimiento de pagos y otras operaciones relacionadas con la escuela.</p>
</samp>

  <h2>💻 Tecnologías Utilizadas</h2>
<!-- Títulos con enlaces -->
<p align="center">
  <a href="https://www.postgresql.org/">PostgreSQL</a> |
  <a href="https://www.pgadmin.org/">PgAdmin</a> |
  <a href="https://fastapi.tiangolo.com/">FastAPI</a> |
  <a href="https://www.uvicorn.org/">Uvicorn</a>
</p>

  <h2>🖇️ Estructura de la Base de Datos</h2>

  Se ha diseñado una base de datos con cinco tablas dentro del esquema público:

    "Alumnos": Almacena los datos de los alumnos, incluyendo su identificación (alumno_id), nombre (nombre_alumno), apellidos (apellidos_alumno), teléfono (telefono_alumno) y correo electrónico (email_alumno).
    
    "Alumnos_clases": Establece la relación entre alumnos y las clases a las que están inscritos. Contiene el identificador del alumno (alumno_id) y el identificador de la clase (clase_id).

    "Clases": Guarda la información de las clases ofrecidas en la escuela, incluyendo su identificación (clase_id), nombre (nombre_clase), nivel (nivel_clase) y precio (precio_clase).

    "Profesores_clases": Define la relación entre los profesores y las clases que imparten. Contiene el identificador del profesor (profesor_id) y el identificador de la clase (clase_id).

    "Profesores": Almacena los datos de los profesores que trabajan en la escuela, incluyendo su identificación (profesor_id) y nombre (nombre_profesor).

    "Pagos": Proporciona los pagos realizados con identificiación (pagos_id) por los alumnos (alumno_id) en cada clase (clase_id) y el importe que han pagado (importe_pagado)

  <h2>🛠️ Funcionalidades de la API</h2>

  La API REST que desarrollaremos permitirá realizar las siguientes operaciones:

    Gestión de Alumnos:
        Obtener la lista de todos los alumnos registrados.
        Agregar un nuevo alumno a la base de datos.
        Modificar los datos de un alumno existente.
        Eliminar un alumno de la base de datos.

    Gestión de Clases:
        Obtener la lista de todas las clases disponibles.
        Agregar una nueva clase a la base de datos.
        Modificar los detalles de una clase existente.
        Eliminar una clase de la base de datos.

    Gestión de Profesores:
        Obtener la lista de todos los profesores de la escuela.
        Agregar un nuevo profesor a la base de datos.
        Modificar los datos de un profesor existente.
        Eliminar un profesor de la base de datos.

    Inscripción y Asignación:
        Inscribir un alumno a una clase específica.
        Asignar un profesor a una clase determinada.

  <h2>🔧 Instalación</h2>
  <p>Para utilizar este proyecto, sigue los siguientes pasos:</p>
  <ol>
    <li>Si dispones de GIT clona este repositorio en tu máquina local.</li>
    <code>git clone https://github.com/AI-School-F5-P2/Fenix_T5.git</code> <code>cd Nombre_tu_proyecto</code><br>
    <li>(opcional pero recomendado) Crea un entorno virtual e actívalo.</li>
    <code>python -m venv venv</code><br>
    En Windows: <code>venv\Scripts\activate</code><br>
    En macOS/Linux: <code>source venv/bin/activate</code>
    <li>Instala las dependencias desde el archivo <code>requirements.txt</code>.</li>
    <code>pip install -r requirements.txt</code><br>
  </ol>

  <h2>📋 Configuración de la Base de Datos</h2>
  <p>Asegúrate de tener PostgreSQL instalado en tu máquina.</p>
  <p>Abre pgAdmin y crea una nueva base de datos para tu proyecto.</p>
  <p>Ejecuta los scripts SQL proporcionados para crear las tablas y relaciones necesarias.</p>

  <h2>⚙️ Ejecutar el Servidor</h2>
  <ol>
    <li>Para iniciar el servidor FastAPI, ejecuta el siguiente comando:</li>
    <code>uvicorn app.main:app --reload</code>
    <li>Abre tu navegador y visita <code>http://localhost:8000/docs</code> para ver la interfaz de tu proyecto.</li>
  </ol>

<br>
<details>
<summary><samp><b>More Info</b></samp></summary>

<h2></h2><br>

  <h2>💡 Contribuciones</h2>
  <p>Las contribuciones son bienvenidas. Si encuentras algún error o tienes mejoras, por favor, abre un issue o envía un pull request.</p>
  <p>Los actuales contribuidores de este proyecto son:</p>

<!-- Lista de contribuidores con iconos y enlaces -->
- [<img src="https://github.com/sgomezp.png" width="50" alt="Sandra Gomez"> Sandra Gómez](https://github.com/sgomezp)
- [<img src="https://github.com/Victoria-moraleda.png" width="50" alt="Victoria Moraleda"> Victoria Moraleda](https://github.com/Victoria-moraleda)
- [<img src="https://github.com/GabrielArjona.png" width="50" alt="Gabriel Arjona"> Gabriel Arjona](https://github.com/GabrielArjona)
- [<img src="https://github.com/migue29.png" width="50" alt="Miguel Mendoza"> Miguel Mendoza](https://github.com/migue29)
- [<img src="https://github.com/BlanckSpeed.png" width="50" alt="Rodrigo Lendinez"> Rodrigo Lendinez](https://github.com/BlanckSpeed)

  
  <h2>📄 Licencia</h2>
  <p>Este proyecto está bajo la Licencia MIT - consulta el archivo <code>LICENSE</code> para más detalles.</p>
  <a href="#license"><img src="https://img.shields.io/github/license/sourcerer-io/hall-of-fame.svg?colorB=ff0000"></a>
</body>
