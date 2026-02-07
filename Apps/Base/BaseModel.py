from django.db import models

# Create your models here.
class ModeloBase(models.Model):
    #region Atributos
    activo = models.BooleanField(null=True)
    id_usuario_creacion = models.IntegerField(null=True)
    fecha_creacion = models.DateTimeField(auto_now=False, auto_now_add=False)
    id_usuario_ult_modificacion = models.IntegerField()
    fecha_ult_modificacion = models.DateTimeField(auto_now= False, auto_now_add= False)
    id_usuario_anulacion = models.IntegerField()
    decha_anulacion = models.DateTimeField(auto_now=False, auto_now_add= False)
    #endregion

    #region Meta
    class Meta:
        abstract = True
    #endregion