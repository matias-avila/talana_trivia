from django.db import models

class TriviaPreguntaQueryset(models.QuerySet):
    def por_id_trivia(self, id_trivia):
        return self.filter(id_trivia=id_trivia).values_list("id_pregunta", flat=True)
