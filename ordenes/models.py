from django.db import models
from .managers import TecnicoManager

# Create your models here.
# Modelo abstracto
class BasePersona(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    class Meta:
        abstract = True  # No crea tabla, solo estructura

# Herencia multi-tabla: sí crea tabla
class Cliente(BasePersona):
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return f"Cliente: {self.nombre}"

# Herencia multi-tabla con Manager personalizado

class Tecnico(BasePersona):
    especialidad = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)

    objects = TecnicoManager()  # activamos el manager personalizado

    def __str__(self):
        return f"Técnico: {self.nombre}"
