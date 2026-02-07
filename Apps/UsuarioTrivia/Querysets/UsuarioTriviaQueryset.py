from django.db import models
from django.db.models import Count, F

class UsuarioTriviaQueryset(models.QuerySet):
    def por_usuario(self, id_usuario):
        return (
            self.filter(id_usuario=id_usuario)
            .select_related("id_trivia")
            .annotate(
                cantidad_preguntas=Count("id_trivia__TriviaPregunta_Trivias",distinct=True),
                nombre=F("id_trivia__nombre"),
                descripcion=F("id_trivia__descripcion"),
            )
            .values(
                "id_trivia",
                "nombre",
                "descripcion",
                "cantidad_preguntas"
            )
            .order_by("id_trivia__nombre")
        )

    def por_usuario_trivia(self, id_usuario, id_trivia):
        return self.filter(id_usuario=id_usuario, id_trivia=id_trivia)

    def ranking(self, id_trivia):
        return (
            self.filter(id_trivia=id_trivia, finalizada=True)
            .select_related("id_usuario")
            .annotate(
                nombre=F("id_usuario__nombre"),
                apellidos = F("id_usuario__apellidos")
            )
            .values(
                "id_usuario",
                "nombre",
                "apellidos",
                "puntaje"
            )
            .order_by("-puntaje", "id_usuario")
        )