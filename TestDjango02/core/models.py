from django.db import models


# Create your models here.
class Categorias(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = "categorias"
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']

# Create your models here.
class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="imagenesproducto", null=True)
    descripcion = models.CharField(max_length=500)
    precio = models.IntegerField()
    stock = models.IntegerField(null=True, default=0)
    categoria = models.ForeignKey(Categorias, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'productos'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']

class Promociones(models.Model):
    idPromociones = models.IntegerField(primary_key=True)
    nombrePromociones = models.CharField(max_length=50)
    marcaPromociones = models.CharField(max_length=20)
    stockPromociones = models.CharField(max_length=20)
    precioPromociones = models.CharField(max_length=20)
    descuentoPromociones = models.CharField(max_length=20)
    fechainiPromociones = models.CharField(max_length=10)
    fechaterPromociones = models.CharField(max_length=10)
    preciofinPromociones = models.CharField(max_length=20)
    

class Pedidos(models.Model):
    nombrep = models.CharField(max_length=100)
    descripcionp = models.CharField(max_length=500)
    preciop = models.IntegerField()


    def __str__(self):
        return self.nombrep

    class Meta:
        db_table = 'pedidos'
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['id']

   

   