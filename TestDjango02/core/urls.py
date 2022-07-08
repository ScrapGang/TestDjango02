from re import template
from xml.dom.minidom import Document
from django.urls import path
from .views import *
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', home, name="home"),
    path('login', LoginView.as_view(template_name="core/login.html"), name="login"),
    path('logout', LogoutView.as_view(template_name="core/logout.html"), name="logout"),
    path('productos', productos, name="productos"),
    path('vercompras', vercompras, name="vercompras"),
    path('suscripciones', suscripciones, name="suscripciones"),
    path('registro', registro, name="registro"),
    path('crudProducto', crudProducto, name="crudProducto"),
    path('venta', venta, name="venta"),
    path('crudPromociones', crudPromociones, name="crudPromociones"),
    path('problemasPedido', problemasPedido, name="problemasPedido"),
    path('nosotros', nosotros, name="nosotros"),
    path('terminosycondiciones', terminosycondiciones, name="terminosycondiciones"),
    path('crearPromociones', crearPromociones, name="crearPromociones"),
    path('modificarPromociones/<id>', modificarPromociones, name="modificarPromociones"),
    path('eliminarPromociones/<id>', eliminarPromociones, name="eliminarPromociones"),
    path('detalleproducto/<id>/', views.detalleProducto, name='detalleproducto'),
    path('seguimiento', seguimiento, name="seguimiento"),
    path('ventaSus', ventaSus, name="ventaSus"),

    #categorias
    path('categorias/', views.listCategorias, name='categorias'),
    path('addcategoria/', views.addCategoria, name='addcategoria'),
    path('editcategoria/<id>/', views.modificarCategoria, name='editcategoria'),
    path('deleteCategoria/<id>/', views.deleteCategoria, name='deleteCategoria'),

    #pedido
    path('listarpedidos/', views.listarPedido, name='listarpedidos'),
    path('addpedido/', views.addPedido, name='addpedido'),
    path('editpedido/<id>/', views.editarPedido, name='editpedido'),
    path('deletePedido/<id>/', views.deletePedido, name='deletePedido'),


    #producto
    path('producto/', views.detalleProducto, name='producto'),
    path('addproducto/', views.addProducto, name='addproducto'),
    path('detalleproducto/<id>/', views.detalleProducto, name='detalleproducto'),
    path('editproducto/<id>/', views.editarProducto, name='editproducto'),
    path('deleteProducto/<id>/', views.deleteProducto, name='deleteProducto'),
    path('listarproductos/', views.listarProductos, name='listarproductos'),
    
    #Paths del carrito
    path('viewcart/', views.viewcart, name="viewcart"),

    path('addcart/<producto_id>/', views.agregar_producto, name="addcart"),

    path('delcart/<producto_id>/', views.eliminar_producto, name="delcart"),

    path('restarcart/<producto_id>/', views.restar_producto, name="restarcart"),

    path('cleancart/', views.cleancart, name="cleancart"),

    path('procesar_compra/', views.procesar_compra, name="procesar_compra"),
    

    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
