from django.shortcuts import render

# For permission purpose
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from rest_framework import status
from rest_framework.response import Response
from .models import Product
from .serializers import ProductsListSerializer


@api_view(['GET'])
def products_list(request):
    products = Product.objects.all()
    serializer = ProductsListSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product_details(request, pk):
    try:
        product = Product.objects.get(id=pk)
        print(product)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ProductsListSerializer(product, many=False)
    return Response(serializer.data)

