<!-- Fenix -->
<div align="justify">

<!-- Profile -->
<p align="left"><strong><samp>「</samp></strong></p>
  <p align="center">
    <samp>
      <b>
        Hello There,
      <br>
        We present our first project
      </b>
      <br>
      <a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&width=435&lines=Fenix+starting+project..." alt="Typing SVG" /></a>
      <br>
      <b>
        ~ Fenix ~
      </b>
    </samp>
  </p>
<p align="right"><strong><samp>」</samp></strong></p>

<br>

</div>
<head>
  <title>Fenix_T5</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
      max-width: 800px;
      margin: 0 auto;
      padding: 20px;
    }
    h1 {
      text-align: center;
    }
    ul {
      list-style-type: disc;
      padding-left: 20px;
    }
    code {
      background-color: #f0f0f0;
      padding: 2px;
    }
  </style>
</head>
<body>
  <h1>Fenix Team 5</h1>

  <p>Este proyecto tiene como objetivo proporcionar una solución digital y escalable a la gestión de alumnos y cuentas de la escuela de baile "Danza Fénix". La escuela ha experimentado un éxito inesperado, lo que ha llevado a un aumento en la cantidad de alumnos y clases ofrecidas. Sin embargo, la gestión actual se realiza en papel y bolígrafo, lo que resulta en un trabajo arduo, propenso a errores y difícil de mantener.

Para abordar este problema, nuestro equipo de desarrollo ha sido contratado por Mar, la dueña de la escuela, para implementar una base de datos de tipo SQL y una API tipo REST. Esta solución permitirá almacenar de manera eficiente y segura la información de los alumnos, las clases y los profesores, lo que simplificará la gestión de datos y facilitará el proceso de inscripción, modificación de clases, seguimiento de pagos y otras operaciones relacionadas con la escuela.</p>

  <h2>Tecnologías Utilizadas</h2>
  <ul>
    <li>PostgreSQL</li>
    <li>pgAdmin</li>
    <li>FastAPI</li>
    <li>Uvicorn</li>
  </ul>

  Estructura de la Base de Datos

Se ha diseñado una base de datos con cinco tablas dentro del esquema público:

    Tabla "Alumnos": Almacena los datos de los alumnos, incluyendo su identificación (alumno_id), nombre (nombre_alumno), apellidos (apellidos_alumno), teléfono (telefono_alumno) y correo electrónico (email_alumno).

    Tabla "Alumnos_clases": Establece la relación entre alumnos y las clases a las que están inscritos. Contiene el identificador del alumno (alumno_id) y el identificador de la clase (clase_id).

    Tabla "Clases": Guarda la información de las clases ofrecidas en la escuela, incluyendo su identificación (clase_id), nombre (nombre_clase), nivel (nivel_clase) y precio (precio_clase).

    Tabla "Profesores_clases": Define la relación entre los profesores y las clases que imparten. Contiene el identificador del profesor (profesor_id) y el identificador de la clase (clase_id).

    Tabla "Profesores": Almacena los datos de los profesores que trabajan en la escuela, incluyendo su identificación (profesor_id) y nombre (nombre_profesor).

Funcionalidades de la API

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

  <h2>Instalación</h2>
  <p>Para utilizar este proyecto, sigue los siguientes pasos:</p>
  <ol>
    <li>Clona este repositorio en tu máquina local.</li>
    <code>git clone https://github.com/tu_usuario/tu_proyecto.git</code>
    <code>cd tu_proyecto</code>
    <li>Crea un entorno virtual (opcional pero recomendado) e actívalo.</li>
    <code>python -m venv venv</code>
    <code># En Windows:</code>
    <code>venv\Scripts\activate</code>
    <code># En macOS/Linux:</code>
    <code>source venv/bin/activate</code>
    <li>Instala las dependencias desde el archivo <code>requirements.txt</code>.</li>
    <code>pip install -r requirements.txt</code>
  </ol>

  <h2>Configuración de la Base de Datos</h2>
  <p>Asegúrate de tener PostgreSQL instalado en tu máquina.</p>
  <p>Abre pgAdmin y crea una nueva base de datos para tu proyecto.</p>
  <p>Ejecuta los scripts SQL proporcionados para crear las tablas y relaciones necesarias.</p>

  <h2>Ejecutar el Servidor</h2>
  <ol>
    <li>Para iniciar el servidor FastAPI, ejecuta el siguiente comando:</li>
    <code>uvicorn app.main:app --reload</code>
    <li>Abre tu navegador y visita <code>http://localhost:8000</code> para ver la interfaz de tu proyecto.</li>
  </ol>

  <h2>Contribuciones</h2>
  <p>Las contribuciones son bienvenidas. Si encuentras algún error o tienes mejoras, por favor, abre un issue o envía un pull request.</p>

  <h2>Licencia</h2>
  <p>Este proyecto está bajo la Licencia MIT - consulta el archivo <code>LICENSE</code> para más detalles.</p>
</body>
