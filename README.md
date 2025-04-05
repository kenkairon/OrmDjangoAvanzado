# M7-L3-ORMDefinicionModelo
Nuevo Proyecto Django: Sistema de Gyms

---
## Tabla de Contenidos
- [Tecnologías](#Tecnologías)
- [Configuración Inicial](#configuración-Inicial)
- [Creación del Modelo](#creación-del-modelo)

---
# Tecnologías
- Django: Framework web en Python.
--- 
# Configuración Inicial 
1. Entorno virtual 
    ```bash 
    python -m venv venv

2. Activar el entorno virtual
    ```bash 
    venv\Scripts\activate

3. Instalar Django
    ```bash 
    pip install django 

4. Actulizamos el pip 
    ```bash
    python.exe -m pip install --upgrade pip

5. Crear el proyecto de django
    ```bash 
    django-admin startproject gym 

6. Ingresamos al proyecto 
    ```bash 
    cd gym

7. Creamos la aplicacion llamada reservations
    ```bash     
    python manage.py startapp reservations

8. Configuración de mi_proyecto/settings.py 
    ```bash 
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'reservations',
    ]
# Creación del Modelo 

9. en reservations/models.py
    ```bash
    from django.db import models

    # Create your models here.
    class Client(models.Model):
        first_name = models.CharField(max_length=100)
        last_name = models.CharField(max_length=100)
        email = models.EmailField(unique=True)
        birth_date = models.DateField()
        
    class SportClass(models.Model):
        name = models.CharField(max_length=100)
        max_capacity = models.PositiveBigIntegerField(default=10)
        
    class BookingClass(models.Model):
        client = models.ForeignKey(Client, on_delete=models.CASCADE)
        sport_class = models.ForeignKey(SportClass, on_delete=models.CASCADE)
        booking_date = models.DateTimeField(auto_now_add=True)
        
        class Meta:
            unique_together = ('client', 'sport_class')

10. Ejecuta las migraciones para aplicar estos cambios a la base de datos:
    ```bash 
    python manage.py makemigrations
    python manage.py migrate

11. reservations/admin.py
    ```bash 
    from django.contrib import admin
    from .models import Client, SportClass, BookingClass
    # Register your models here.
    admin.site.register(Client)
    admin.site.register(SportClass)
    admin.site.register(BookingClass)

12. Ingresamos a las rutas http://127.0.0.1:8000/

    ```bash 
    python manage.py runserver

13. Ingresamos a las rutas http://127.0.0.1:8000/admin