# talana_trivia
Desafio Talana

Descripción
<br>TalaTrivia es una API REST desarrollada en Django + Django REST Framework que permite:
- Crear usuarios
- Crear preguntas
- Crear trivias
- Asignar preguntas y usuarios a trivias
- Responder trivias
- Generar ranking de usuarios por trivia

Tecnologías utilizadas
- Python 3.9.6
- Django
- Django REST Framework
- PostgreSQL / SQL Server
- JWT para autenticación
- ORM de Django

Arquitectura
- Usuario
- Preguntas
- Trivias
- UsuarioTrivia
- TriviaPregunta
- Respuestas

Autenticación
<br>(Se utiliza JWT personalizado, el que se solicita en proyecto de autenticación aparte, para enfoque en trivia y apuntar a microservios)
<br>El token incluye:
- id_usuario
- es_administrador

Instalación
1) git clone <repo>
2) cd TalaTrivia
3) python -m venv venv
4) source venv/bin/activate
5) pip install -r requirements.txt
6) python manage.py migrate
7) python manage.py runserver

Endpoints principales
- Crear usuario
<br>POST /usuarios/crear_usuario
    <br>Ejemplo payload
    ```json
    {
        "nombre": "Matias",
        "apellidos": "Avila Bustamante",
        "email": "matias.avila.bustamante@gmail.com"
        "login": "mavila",
        "administrador": True
    }
    ```

- Listar usuarios por concepto
<br>GET /usuarios/listar_usuario/{concepto}
<br>Permite buscar por nombre, apellido o correo electrónico.

- Crear trivia
<br>POST /trivias/crear_trivias
    <br>Ejemplo payload
    ```json
    {
        "nombre": "Trivia 1",
        "descripcion": "Primera trivia",
        "preguntas": [
            1,
            2,
            3
        ],
        "usuarios": [
            4,
            5
        ]
    }
    ```

- Listar trivias por concepto
<br>GET /trivias/listar_trivias/{concepto}

- Listar trivias asociadas a un usuario
<br>GET /trivias/listar_trivias_usuario

- Listar ranking por trivia
<br>GET /trivias/ranking_trivia/{id_trivia}

- Responder Trivia
<br>POST /respuestas/responder_trivia/{id_trivia}
    <br>Ejemplo payload
    ```json
    {
        "respuestas": [
            { "id_pregunta": 1, "opcion_seleccionada": 2 },
            { "id_pregunta": 2, "opcion_seleccionada": 3 },
            { "id_pregunta": 3, "opcion_seleccionada": 6 },
        ]
    }
    ```

- Crear pregunta
<br>POST /preguntas/crear_pregunta
    <br>Ejemplo payload
    ```json
    {
        "texto": "¿Quién pintó la Mona Lisa?",
        "dificultad": 2,
        "opciones": [
            "Pablo Picasso",
            "Leonardo da Vinci",
            "Vincent van Gogh",
            "Claude Monet"
        ],
        "opcion_correcta": 1
    }
   ```
<br>Nota:
<br>La opcion_correcta corresponde al índice dentro del arreglo opciones.

- Listar preguntas por concepto
<br>GET /preguntas/listar_preguntas/{concepto}
