from django.db import models
from django.db.models import Q

class TriviasQueryset(models.QuerySet):
    def por_concepto(self, concepto):
        if not concepto:
            return self.all()

        return self.filter(
            Q(nombre__icontains=concepto) |
            Q(descripcion__icontains=concepto)
        )

    def por_id(self, id_trivia):
        return self.filter(id=id_trivia)

