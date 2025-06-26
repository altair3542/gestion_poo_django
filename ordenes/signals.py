from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Cliente, PerfilUsuario


@receiver(post_delete, sender=Cliente)
def cliente_eliminado(sender, instance, **kwargs):
    print(f"🗑 Cliente eliminado: {instance.nombre} ({instance.email})")

@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        PerfilUsuario.objects.create(usuario=instance)
