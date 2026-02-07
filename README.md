# talana_trivia
Desafio Talana

Descripción
TalaTrivia es una API REST desarrollada en Django + Django REST Framework que permite:
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

Autenticación (Se utiliza JWT personalizado, el que se solicita en proyecto de autenticación aparte, para enfoque en trivia y apuntar a microservios)
El token incluye:
- id_usuario
- es_administrador

Instalación
git clone <repo>
cd TalaTrivia
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Endpoints principales
Crear usuario
POST /usuarios/crear_usuario
    Ejemplo payload
    {
        "nombre": "Matias",
        "apellidos": "Avila Bustamante",
        "email": "matias.avila.bustamante@gmail.com"
        "login": "mavila",
        "administrador": True
    }

Listar usuarios por concepto
GET /usuarios/listar_usuario/{concepto}

Crear trivia
POST /trivias/crear_trivias
    Ejemplo payload
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

Listar trivias por concepto
GET /trivias/listar_trivias/{concepto}

Listar trivias asociadas a un usuario
GET /trivias/listar_trivias_usuario

Listar ranking por trivia
GET /trivias/ranking_trivia/{id_trivia}

Responder Trivia
POST /respuestas/responder_trivia/{id_trivia}
    Ejemplo payload
    {
        "respuestas": [
            { "id_pregunta": 1, "opcion_seleccionada": 2 },
            { "id_pregunta": 2, "opcion_seleccionada": 3 },
            { "id_pregunta": 3, "opcion_seleccionada": 6 },
        ]
    }

Crear pregunta
POST /preguntas/crear_pregunta
    Ejemplo payload
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

Listar preguntas por concepto
GET /preguntas/listar_preguntas/{concepto}