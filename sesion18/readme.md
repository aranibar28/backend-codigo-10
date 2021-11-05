Instalar Dependencias

    pip install -r requirements.txt

Crear Proyecto

    django-admin startproject catalog
    python manage.py startapp core

Crear Modelo de Datos en `core/models.py`

    class Product(models.Model):
        colum1 = models.CharField(max_length=100)
        colum2 = models.CharField(max_length=100)
        colum3 = models.CharField(max_length=100)
        colum4 = models.CharField(max_length=100)

Realizar migraciones de Base Datos

    python manage.py makemigrations
    python manage.py migrate

------------------------------

Configurar Viewsets en `core/viewsets.py`

    class ProductViewSet(viewsets.ViewSet):
        def list()
        def create()


Configurar Serializers en `core/serializers.py`

    class ProductSerializer(serializers.Serializer):
        def create()
        
Configurar URLs en `catalog/urLs.py`

    path('catalog/', ProductViewSet.as_view())
    