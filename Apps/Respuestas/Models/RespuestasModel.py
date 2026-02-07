from django.db import models
from django.db.models.deletion import PROTECT, CASCADE
from Apps.Base.BaseModel import ModeloBase
from Apps.Respuestas.Querysets.RespuestasQueryset import RespuestasQueryset
from Apps.UsuarioTrivia.Models.UsuarioTriviaModel import UsuarioTrivia
from Apps.Preguntas.Models.PreguntasModel import Preguntas
from django.utils import timezone

class Respuestas(ModeloBase):
    #region Atributos
    id = models.AutoField(primary_key= True)
    id_usuario_trivia = models.ForeignKey(UsuarioTrivia, on_delete=CASCADE, related_name='Respuestas_UsuarioTrivia')
    id_pregunta = models.ForeignKey(Preguntas, on_delete=CASCADE, related_name='Respuestas_Preguntas')
    opcion_seleccionada = models.IntegerField()
    es_correcta = models.BooleanField()
    puntaje = models.IntegerField()

    objects = RespuestasQueryset.as_manager()
    #endregion

    #region Meta
    class Meta:
        db_table = 'Respuestas'
        managed = False
        unique_together = ('id_usuario_trivia', 'id_pregunta')
    #endregion

    def create(self, id_usuario_trivia, id_pregunta, opcion_seleccionada, es_correcta, puntaje, id_usuario):
        registro = {}
        registro['id_usuario_trivia'] = id_usuario_trivia
        registro['id_pregunta'] = id_pregunta
        registro['opcion_seleccionada'] = opcion_seleccionada
        registro['es_correcta'] = es_correcta
        registro['puntaje'] = puntaje
        registro['activo'] = True
        registro['id_usuario_creacion'] = id_usuario
        registro['fecha_creacion'] = timezone.now()

        return Preguntas.objects.create(**registro)