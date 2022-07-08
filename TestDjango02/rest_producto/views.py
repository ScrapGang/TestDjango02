from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Productos
from core.models import Promociones
from core.models import Pedidos
from core.models import Categorias
from .serializers import ProductosSerializer
from .serializers import PromocionesSerializer
from .serializers import CategoriasSerializer
from .serializers import PedidoSerializer
@csrf_exempt
@api_view(['GET', 'POST'])

def lista_producto(request):
    if request.method == 'GET':
        prod = Productos.objects.all()
        serializer = ProductosSerializer(prod, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductosSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'POST'])

def lista_categorias(request):
    if request.method == 'GET':
        prod = Categorias.objects.all()
        serializer = CategoriasSerializer(prod, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CategoriasSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'POST'])

def lista_promociones(request):
    if request.method == 'GET':
        prod = Promociones.objects.all()
        serializer = PromocionesSerializer(prod, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PromocionesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'POST'])

def lista_pedidos(request):
    if request.method == 'GET':
        prod = Pedidos.objects.all()
        serializer = PedidoSerializer(prod, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PedidoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

