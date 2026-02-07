from django.db import models

class RespuestasQueryset(models.QuerySet):
    def por_id_usuario_trivia(self, id_usuario_trivia):
        return self.filter(id_usuario_trivia=id_usuario_trivia)
