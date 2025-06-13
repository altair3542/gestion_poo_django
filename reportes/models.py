from django.db import models

# Create your models here.
class LogReporte(models.Model):
    evento = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'reportes'

