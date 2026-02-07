from django.db import models
from django.db.models.deletion import PROTECT, CASCADE
from Apps.Base.BaseModel import ModeloBase
from Apps.UsuarioTrivia.Querysets.UsuarioTriviaQueryset import UsuarioTriviaQueryset
from Apps.Usuario.Models.UsuarioModel import Usuario
from Apps.Trivias.Models.TriviasModel import Trivias

class UsuarioTrivia(ModeloBase):
    #region Atributos
    id = models.AutoField(primary_key= True)
    id_usuario = models.ForeignKey(Usuario, on_delete=CASCADE, related_name='UsuarioTrivia_Usuario')
    id_trivia = models.ForeignKey(Trivias, on_delete=CASCADE, related_name='UsuarioTrivia_Trivias')
    puntaje = models.IntegerField(default=0)
    finalizada = models.BooleanField(default=False)
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_fin = models.DateTimeField(null=True, blank=True)

    objects = UsuarioTriviaQueryset.as_manager()
    #endregion

    #region Meta
    class Meta:
        db_table = 'UsuarioTrivia'
        managed = False
    #endregion