from django.urls import path
from rest_producto.views import lista_producto
from rest_producto.views import lista_categorias
from rest_producto.views import lista_promociones
from rest_producto.views import lista_pedidos

urlpatterns = [
    path('lista_producto', lista_producto, name="lista_producto"),
    path('lista_categorias', lista_categorias, name="lista_categorias"),
    path('lista_promociones', lista_promociones, name="lista_promociones"),
    path('lista_pedidos', lista_pedidos, name="lista_pedidos"),
    
]