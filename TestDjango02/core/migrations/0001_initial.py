# Generated by Django 3.2.8 on 2022-07-08 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'db_table': 'categorias',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrep', models.CharField(max_length=100)),
                ('descripcionp', models.CharField(max_length=500)),
                ('preciop', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
                'db_table': 'pedidos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Promociones',
            fields=[
                ('idPromociones', models.IntegerField(primary_key=True, serialize=False)),
                ('nombrePromociones', models.CharField(max_length=50)),
                ('marcaPromociones', models.CharField(max_length=20)),
                ('stockPromociones', models.CharField(max_length=20)),
                ('precioPromociones', models.CharField(max_length=20)),
                ('descuentoPromociones', models.CharField(max_length=20)),
                ('fechainiPromociones', models.CharField(max_length=10)),
                ('fechaterPromociones', models.CharField(max_length=10)),
                ('preciofinPromociones', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('imagen', models.ImageField(null=True, upload_to='imagenesproducto')),
                ('descripcion', models.CharField(max_length=500)),
                ('precio', models.IntegerField()),
                ('stock', models.IntegerField(default=0, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.categorias')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'db_table': 'productos',
                'ordering': ['id'],
            },
        ),
    ]
