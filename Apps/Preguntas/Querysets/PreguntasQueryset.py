from django.db import models
from django.db.models import Q

class PreguntasQueryset(models.QuerySet):
    def por_concepto(self, concepto):
        if not concepto:
            return self.all()

        return self.filter(
            Q(texto__icontains=concepto) |
            Q(opciones__icontains=concepto)
        )

    def por_id(self, id_pregunta):
        return self.filter(id=id_pregunta)
