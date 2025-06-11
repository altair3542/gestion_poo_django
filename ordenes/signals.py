from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Cliente

@receiver(post_delete, sender=Cliente)
def cliente_eliminado(sender, instance, **kwargs):
    print(f"🗑 Cliente eliminado: {instance.nombre} ({instance.email})")
