from django.urls import path
from .views import (
    products_list,
    product_details,
)

urlpatterns = [
    path('', products_list, name="ProductsList"),
    path('Details/<int:pk>/', product_details, name="ProductDetails"),
]
