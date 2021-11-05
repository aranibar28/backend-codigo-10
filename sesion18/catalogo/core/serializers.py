from rest_framework import serializers
from core.models import Product
from core.models import Category

class ProductSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=100)
    price = serializers.FloatField()
    sku = serializers.CharField(max_length=11)
    exp_date = serializers.DateField()

    def create(self, validate_data):
        product = Product(**validate_data)
        product.save()
        return product

    def update(self, product, data):
        product = Product.objects.filter(pk=product.id)
        product.update(**data)
        return product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description']