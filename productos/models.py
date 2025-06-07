from django.db import models
from .managers import ProductoElectronicoManager

# Create your models here.
class BaseProducto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        abstract = True

class ProductoElectronico(BaseProducto):
    garantia_meses = models.IntegerField()

    objects = ProductoElectronicoManager()


class ProductoBarato(ProductoElectronico):
    class Meta:
        proxy = True

    def es_muy_barato(self):
        return self.precio < 100
