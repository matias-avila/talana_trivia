from django.db import models
from django.db.models.deletion import PROTECT, CASCADE
from Apps.Base.BaseModel import ModeloBase
from Apps.TriviaPregunta.Querysets.TriviaPreguntaQueryset import TriviaPreguntaQueryset
from Apps.Trivias.Models.TriviasModel import Trivias
from Apps.Preguntas.Models.PreguntasModel import Preguntas

class TriviaPregunta(ModeloBase):
    #region Atributos
    id = models.AutoField(primary_key= True)
    id_trivia = models.ForeignKey(Trivias, on_delete=CASCADE, related_name='TriviaPregunta_Trivias')
    id_pregunta = models.ForeignKey(Preguntas, on_delete=CASCADE, related_name='TriviaPregunta_Preguntas')

    objects = TriviaPreguntaQueryset.as_manager()
    #endregion

    #region Meta
    class Meta:
        db_table = 'TriviaPregunta'
        managed = False
        unique_together = ('id_trivia', 'id_pregunta')
    #endregion