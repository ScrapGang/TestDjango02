from rest_framework import serializers
from core.models import Productos
from core.models import Categorias
from core.models import Promociones
from core.models import Pedidos

class ProductosSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Productos
        fields =  ["nombre", "descripcion", "precio", "stock", "imagen"]

class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = ["nombre"]

class PromocionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promociones
        fields = ['idPromociones','nombrePromociones','marcaPromociones','stockPromociones','precioPromociones','descuentoPromociones','fechainiPromociones','fechaterPromociones','preciofinPromociones']

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedidos
        fields = ["nombrep", "descripcionp", "preciop"]