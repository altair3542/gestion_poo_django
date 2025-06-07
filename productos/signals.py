from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ProductoElectronico

@receiver(post_save, sender=ProductoElectronico)
def notificar_producto_guardado(sender, instance, created, **kwargs):
    if created:
        print(f"📦 Producto nuevo: {instance.nombre}")
    else:
        print(f"🛠️ Producto Actualizado: {instance.nombre}")
        
