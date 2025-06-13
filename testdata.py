# testdata.py

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')
django.setup()

from django.contrib.auth.models import User
from ordenes.models import OrdenServicio

# Eliminar datos previos
print("🧹 Eliminando datos anteriores...")
OrdenServicio.objects.all().delete()
User.objects.exclude(is_superuser=True).delete()

# Crear técnicos
print("👷‍♀️ Creando técnicos...")
try:
    laura = User.objects.create_user(username='laura', email='laura@correo.com', password='1234')
    pedro = User.objects.create_user(username='pedro', email='pedro@correo.com', password='1234')
except Exception as e:
    print(f"⚠️ Error creando usuarios: {e}")

# Crear órdenes
print("🛠️ Creando órdenes...")
try:
    OrdenServicio.objects.create(descripcion='Revisión de frenos', estado='pendiente', tecnico_asignado=laura)
    OrdenServicio.objects.create(descripcion='Cambio de aceite', estado='en_progreso', tecnico_asignado=laura)
    OrdenServicio.objects.create(descripcion='Alineación de ruedas', estado='finalizada', tecnico_asignado=pedro)
except Exception as e:
    print(f"⚠️ Error creando órdenes: {e}")

# Confirmar
print("✅ Carga de prueba completada con éxito.")
print("🔑 Inicia sesión con:")
print("• Usuario: laura / Contraseña: 1234")
print("• Usuario: pedro / Contraseña: 1234")
