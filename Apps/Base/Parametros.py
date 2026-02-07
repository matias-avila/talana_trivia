from django.db import models

class MensajesEnum(models.TextChoices):
    mensajeCampoRequerido = 'Este campo debe ser informado.'
    mensajeErrorValidacionDatos = 'Error en la validación de los datos.'
    mensajeOk = 'Ok.'
    mensajeSinPrivilegios = 'Sin privilegios.'
    mensajeErrorCreacion = 'Registro no creado.'
    mensajeBusquedaSinResultados = 'Búsqueda sin resultados.'
    mensajeTriviaFinalizada = 'La trivia ya fue respondida.'
    mensajePreguntaInvalida = 'Pregunta inválida para esta trivia.'
    mensajeNoRepetirPreguntas = 'No se pueden repetir preguntas.'
    mensajeOpcionNoValida = 'La opción seleccionada no es válida.'
    mensajeNoPermitePreguntasDuplicadas = "No se permiten preguntas duplicadas."
    mensajePreguntasNoExisten = "Una o más preguntas no existen."
    mensajeUsuarioDuplicados = "No se permiten usuarios duplicados."
    mensajeUsuarioNoExisten = "Uno o más usuarios no existen."


DIFICULTAD_CHOICES = (
        (1, 'Fácil'),
        (2, 'Media'),
        (3, 'Difícil'),
    )