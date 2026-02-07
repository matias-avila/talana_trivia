from django.db import models
from django.db.models import Q

class UsuarioQueryset(models.QuerySet):
    def por_concepto(self, concepto):
        if not concepto:
            return self.all()

        return self.filter(
            Q(nombre__icontains=concepto) |
            Q(apellidos__icontains=concepto) |
            Q(email__icontains=concepto)
        )
