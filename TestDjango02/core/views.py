from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm 
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from .carro import Carro
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.generic import ListView, CreateView
from django.db.models import Q
from .forms import ProductoForm
from .forms import PedidoForm
from .forms import PromocionesForm
from .forms import CategoriaForm



#detalle


# Create your views here.
def home(request):
    busqueda = request.POST.get("buscador")
    product_list = Productos.objects.order_by('nombre')
    page = request.GET.get('page', 1)

    if busqueda:
        product_list = Productos.objects.filter(
            Q(nombre__icontains = busqueda) |
            Q(descripcion__icontains = busqueda)
        ).distinct()
    
    try:
        paginator = Paginator(product_list, 12)
        product_list = paginator.page(page)
    except:
        raise Http404

    data = {'entity': product_list,
            'paginator': paginator
    }
    return render(request, 'core/home.html', data)

def registro(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="login")
    return render(request, 'core/registro.html', {'form':form})


#crearProducto

def detalleProducto(request, id):
    product = get_object_or_404(Productos, id=id)
    
    data = {
        'producto': product,
        
    }
    return render(request, 'core/producto/detalle.html', data)

@login_required(login_url='/login')
def addProducto(request):
    data = {
        'form' : ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Registro agregado correctamente")
            return redirect(to="/listarproductos")
        else:
            data["form"] = formulario   
    return render(request, 'CORE/producto/agregar.html', data)



@login_required(login_url='/login')
def listarProductos(request):
    busqueda = request.POST.get("buscador")
    lista_productos = Productos.objects.order_by('nombre')
    page = request.GET.get('page', 1)
    if busqueda:
        lista_productos = Productos.objects.filter(
            Q(nombre__icontains = busqueda) |
            Q(descripcion__icontains = busqueda)
        ).distinct()

    try:
        paginator = Paginator(lista_productos, 6)
        lista_productos = paginator.page(page)
    except:
        raise Http404

    data = {'entity': lista_productos,
            'title': 'LISTADO DE PRODUCTOS',
            'paginator': paginator
            }
    return render(request, 'core/producto/listar.html', data)


@login_required(login_url='/login')
def editarProducto(request, id):
    producto = get_object_or_404(Productos, id=id)
    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Registro modificado correctamente")
            return redirect(to="/listarproductos")
        data["form"] = formulario
    return render(request, 'core/producto/modificar.html', data)


@login_required(login_url='/login')
def deleteProducto(request, id):
    producto = get_object_or_404(Productos, id=id)
    producto.delete()
    messages.success(request, "Registro eliminado correctamente")
    return redirect(to="/listarproductos")


#pedidoListar
@login_required(login_url='/login')
def listarPedido(request):
    busqueda = request.POST.get("buscador")
    lista_productos = Pedidos.objects.order_by('nombrep')
    page = request.GET.get('page', 1)
    if busqueda:
        lista_productos = Pedidos.objects.filter(
            Q(nombrep__icontains = busqueda) |
            Q(descripcionp__icontains = busqueda)
        ).distinct()

    try:
        paginator = Paginator(lista_productos, 6)
        lista_productos = paginator.page(page)
    except:
        raise Http404

    data = {'entity': lista_productos,
            'title': 'LISTADO DE PEDIDOS',
            'paginator': paginator
            }
    return render(request, 'core/seguimiento/listar.html', data)

#pedidoagregar
@login_required(login_url='/login')
def addPedido(request):
    data = {
        'form' : PedidoForm()
    }

    if request.method == 'POST':
        formulario = PedidoForm(data=request.POST, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Registro agregado correctamente")
            return redirect(to="/listarpedidos")
        else:
            data["form"] = formulario   
    return render(request, 'CORE/seguimiento/agregar.html', data)

#pedidoEditar
@login_required(login_url='/login')
def editarPedido(request, id):
    producto = get_object_or_404(Pedidos, id=id)
    data = {
        'form': PedidoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = PedidoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Registro modificado correctamente")
            return redirect(to="/listarpedidos")
        data["form"] = formulario
    return render(request, 'core/producto/modificar.html', data)

#pedidoBorrar
@login_required(login_url='/login')
def deletePedido(request, id):
    producto = get_object_or_404(Pedidos, id=id)
    producto.delete()
    messages.success(request, "Registro eliminado correctamente")
    return redirect(to="/listarpedidos")

def crearPromociones(request):
    datos = {"form":PromocionesForm()}
    if request.method == "POST":
        form = PromocionesForm(request.POST)
        if form.is_valid:
            form.save()
            datos["mensaje"] = "Promoción agregado!."
    return render(request, 'core/crearPromociones.html', datos)

def modificarPromociones(request, id):
    promociones = Promociones.objects.get(idPromociones=id)
    datos = {'form': PromocionesForm(instance=promociones)}
    if request.method == "POST":
        form = PromocionesForm(request.POST, instance=promociones)
        if form.is_valid:
            form.save()
            datos["mensaje"] = "Producto Modificado"
            datos["form"] = form
    return render(request, 'core/modificarPromociones.html', datos)

def eliminarPromociones(request, id):
    promociones = Promociones.objects.get(idPromociones=id)
    promociones.delete()
    return redirect(to = "crudPromociones")



def crudProducto(request):
    productos= Productos.objects.all()
    return render(request, 'core/crudProducto.html', {'contexto':productos})

def crudPromociones(request):
    promociones= Promociones.objects.all()
    return render(request, 'core/crudPromociones.html', {'contexto':promociones})  



def seguimiento(request):
    busqueda = request.POST.get("buscador")
    product_list = Pedidos.objects.order_by('nombrep')
    page = request.GET.get('page', 1)

    if busqueda:
        product_list = Pedidos.objects.filter(
            Q(nombre__icontains = busqueda) |
            Q(descripcion__icontains = busqueda)
        ).distinct()
    
    try:
        paginator = Paginator(product_list, 12)
        product_list = paginator.page(page)
    except:
        raise Http404

    data = {'entity': product_list,
            'paginator': paginator
    }
    return render(request, 'core/seguimiento.html', data)

def problemasPedido(request):
    return render(request, 'core/problemasPedido.html')  

def nosotros(request):
    return render(request, 'core/nosotros.html')

def terminosycondiciones(request):
    return render(request, 'core/terminosycondiciones.html')
    


def productos(request):
    busqueda = request.POST.get("buscador")
    product_list = Productos.objects.order_by('nombre')
    page = request.GET.get('page', 1)

    if busqueda:
        product_list = Productos.objects.filter(
            Q(nombre__icontains = busqueda) |
            Q(descripcion__icontains = busqueda)
        ).distinct()
    
    try:
        paginator = Paginator(product_list, 12)
        product_list = paginator.page(page)
    except:
        raise Http404

    data = {'entity': product_list,
            'paginator': paginator
    }
    return render(request, 'core/productos.html', data)
 
# Listar productos por categoria



#categoria


def vercompras(request):
    return render(request, 'core/vercompras.html')

def ventaSus(request):
    return render(request, 'core/ventaSus.html')

def suscripciones(request):
    return render(request, 'core/suscripciones.html')

def venta(request):
    return render(request, 'core/venta.html')

#accionesCarro
def viewcart(request):
    return render(request, 'core/carrito/cart.html', {'carro': request.session['carro']})

def agregar_producto(request, producto_id):
    carro=Carro(request)
    producto=Productos.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect(to="/viewcart")

def eliminar_producto(request, producto_id):
    carro=Carro(request)
    producto=Productos.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect(to="/viewcart")


def restar_producto(request, producto_id):
    carro = Carro(request)
    producto = Productos.objects.get(id=producto_id)
    carro.restar(producto=producto)
    return redirect(to="/viewcart")

def cleancart(request):
    carro=Carro(request)
    carro.limpiar_carro()
    return redirect(to="/viewcart")


def procesar_compra(request):
    messages.success(request, 'Gracias por su Compra!!')
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect('/')

@login_required(login_url='/login')
def listCategorias(request):
    lista_categorias = Categorias.objects.all().order_by('nombre')
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(lista_categorias, 6)
        lista_categorias = paginator.page(page)
    except:
        raise Http404

    data = {'entity': lista_categorias,
            'title': 'LISTADO DE CATEGORIAS',
            'paginator': paginator
            }

    return render(request,'core/categorias.html', data)


@login_required(login_url='/login')
def addCategoria(request):
    data = {
        'form': CategoriaForm()
    }
    if request.method == 'POST':
        formulario = CategoriaForm(data=request.POST)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Registro agregado correctamente")
            return redirect(to="/categorias")
        else:
            data["form"] = formulario
    return render(request, 'core/categoria/agregar.html', data)


@login_required(login_url='/login')
def modificarCategoria(request, id):
    categoria = get_object_or_404(Categorias, id=id)

    data = {
        'form': CategoriaForm(instance=categoria)
    }
    if request.method == 'POST':
        formulario = CategoriaForm(data=request.POST, instance=categoria)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Registro modificado correctamente")
            return redirect(to="/categorias")
        else:
            data["form"] = formulario

    return render(request, 'core/categoria/modificar.html', data)


@login_required(login_url='/login')
def deleteCategoria(request, id):
    categoria = get_object_or_404(Categorias, id=id)
    categoria.delete()
    messages.success(request, "Registro eliminado correctamente")
    return redirect(to="/categorias")

#promociones


