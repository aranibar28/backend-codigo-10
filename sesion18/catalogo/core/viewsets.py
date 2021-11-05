from rest_framework import viewsets
from rest_framework.response import Response
from core.models import Product, Category
from core.serializers import ProductSerializer, CategorySerializer
from django.shortcuts import get_object_or_404


class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
               'status': 'ok',
               'data': serializer.data
            })
        else:
            return Response({
                'error': serializer.errors
            })
    
    def update(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        data = request.data
        serializer = ProductSerializer(instance=product, data=data, partial=True)
        if serializer.is_valid():
            serializer.update(product, data)
            return Response({
               'status': 'ok',
               'data': serializer.data
            })
        else:
            return Response({
                'error': serializer.errors
            })

    def destroy(self, request, pk):
        product = get_object_or_404(Product, id=pk)

class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
