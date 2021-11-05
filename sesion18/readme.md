Instalar Dependencias

    pip install -r requirements.txt

Crear Proyecto

    django-admin startproject catalog
    python manage.py startapp core

Crear Modelo de Datos en `models.py`

Realizar migraciones de Base Datos

    python manage.py makemigrations
    python manage.py migrate