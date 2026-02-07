from django.db import models
from django.db.models.deletion import PROTECT
from Apps.Base.BaseModel import ModeloBase
from Apps.Trivias.Querysets.TriviasQueryset import TriviasQueryset
from Apps.TriviaPregunta.Models.TriviaPreguntaModel import TriviaPregunta
from Apps.UsuarioTrivia.Models.UsuarioTriviaModel import UsuarioTrivia

class Trivias(ModeloBase):
    #region Atributos
    id = models.AutoField(primary_key= True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)

    objects = TriviasQueryset.as_manager()
    #endregion

    #region Meta
    class Meta:
        db_table = 'Trivias'
        managed = False
    #endregion

    def create(self, validated_data):
        preguntas = validated_data.pop("preguntas")
        usuarios = validated_data.pop("usuarios")

        trivia = Trivias.objects.create(**validated_data)

        for pregunta_id in preguntas:
            TriviaPregunta.objects.create(
                id_trivia=trivia,
                id_pregunta_id=pregunta_id
            )

        for usuario_id in usuarios:
            UsuarioTrivia.objects.create(
                id_trivia=trivia,
                id_usuario_id=usuario_id
            )
