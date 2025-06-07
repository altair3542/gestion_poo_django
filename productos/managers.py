from django.db import models

class ProductoElectronicoManager(models.Manager):
    def baratos(self):
        return self.get_queryset().filter(precio__lt=500)

    def con_garantia(self):
        return self.get_queryset().filter(garantia_meses__gte=12)
