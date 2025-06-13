from django.db import models
from .managers import TecnicoManager
from django.contrib.auth.models import User

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

class OrdenServicio(models.Model):
    descripcion = models.TextField()
    tecnico_asignado = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ordenes_asignadas')
    estado = models.CharField(max_length=20, choices=[
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('finalizada', 'Finalizada')
    ])
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(f"Orden #{self.id} - {self.estado}")
