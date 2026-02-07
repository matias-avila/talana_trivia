from django.db import models
from django.db.models.deletion import PROTECT
from Apps.Base.BaseModel import ModeloBase
from Apps.Preguntas.Querysets.PreguntasQueryset import PreguntasQueryset
from Apps.Base.Parametros import DIFICULTAD_CHOICES
from django.utils import timezone

class Preguntas(ModeloBase):
    #region Atributos
    id = models.AutoField(primary_key= True)
    texto = models.TextField()
    dificultad = models.IntegerField(choices=DIFICULTAD_CHOICES)
    opciones = models.JSONField()
    opcion_correcta = models.IntegerField()

    objects = PreguntasQueryset.as_manager()
    #endregion

    #region Meta
    class Meta:
        db_table = 'Preguntas'
        managed = False
    #endregion

    def create(self, id_usuario, data):
        registro = {}
        registro['texto'] = data.get('texto')
        registro['dificultad'] = data.get('dificultad')
        registro['opciones'] = data.get('opciones')
        registro['opcion_correcta'] = data.get('opcion_correcta')
        registro['activo'] = True
        registro['id_usuario_creacion'] = id_usuario
        registro['fecha_creacion'] = timezone.now()

        return Preguntas.objects.create(**registro)