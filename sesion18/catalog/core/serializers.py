from rest_framework import serializers
from core.models import Product

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
