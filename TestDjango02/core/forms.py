from django.forms import ModelForm
from .models import *

class ProductoForm(ModelForm):
    class Meta:
        model = Productos
        fields = ["nombre", "descripcion", "precio", "stock", "categoria", "imagen"]

class CategoriaForm(ModelForm):

    class Meta:
        model = Categorias
        fields = ["nombre"]

class PromocionesForm(ModelForm):
    class Meta:
        model = Promociones
        fields = ['idPromociones','nombrePromociones','marcaPromociones','stockPromociones','precioPromociones','descuentoPromociones','fechainiPromociones','fechaterPromociones','preciofinPromociones']

class PedidoForm(ModelForm):
    class Meta:
        model = Pedidos
        fields = ["nombrep", "descripcionp", "preciop"]

