from django.db import models

class TecnicoManager(models.Manager):
    def activos(self):
        return self.get_queryset().filter(activo=True)

    def inactivos(self):
        return self.get_queryset().filter(activo=False)
