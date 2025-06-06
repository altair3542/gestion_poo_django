# 🧩 Sistema de Gestión de Órdenes de Servicio

Este es un proyecto Django avanzado orientado a objetos, diseñado para gestionar órdenes de trabajo, técnicos, reportes y más. Está configurado con múltiples entornos y múltiples bases de datos.

---

## ⚙️ Requisitos

- Python 3.10+
- PostgreSQL (si vas a usar la BD de reportes)
- Git
- PowerShell o terminal con permisos

---

## 🚀 Instalación paso a paso

### 1. Clona el proyecto

git clone https://github.com/tu_usuario/sistema-ordenes.git
cd sistema-ordenes

o usa la opcion de descargar el zip del proyecto.

## 2. Crea y activa el entorno virtual

python -m venv venv
venv\Scripts\activate

En caso de tener algun error con la instalacion del entorno virtual (politica de ejecución)

ejecuta esto en una ventana de PowerShell como administrador:

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

Recuerden responder con la letra  O

Cierra y abre de nuevo PowerShell. Intenta:

venv\Scripts\activate

en la carpeta donde descargaste el proyecto.

## 3 Instala las dependencias:

pip install -r requirements.txt


## 4. Configura las bases de datos
Por defecto usa:
SQLite para la base principal.

PostgreSQL para la base de reportes. 

Edita config/settings/dev.py con tus credenciales si usas PostgreSQL:

https://www.postgresql.org/download/

## 5 Realiza las migraciones

python manage.py makemigrations

python manage.py migrate


## 6. Ejecuta el servidor de desarrollo

python manage.py runserver

Abre el navegador en: http://127.0.0.1:8000/

## 🧠 Notas adicionales
Usa python manage.py createsuperuser para crear un usuario admin.

Este proyecto incluye múltiples bases de datos, routers personalizados y separación de configuración por entorno.


## 📁 Estructura del proyecto

config/

├── settings/

│   ├── base.py

│   ├── dev.py

│   └── prod.py

├── db_routers.py

├── urls.py

├── wsgi.py

...

apps/

├── ordenes/

├── reportes/

└── productos/



