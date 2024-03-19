from django.db import models
from datetime import datetime
from Usuarios.models import Cliente
from django.utils.text import slugify


class Proveedor(models.Model):
    ESTADO_CHOICES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
        ('Bloqueado', 'Bloqueado'),
        # Puedes agregar más opciones aquí según tus necesidades
    ]

    nombre_proveedor = models.CharField(max_length=60, verbose_name='Nombre del proveedor')
    TelefonoProveedor = models.BigIntegerField(verbose_name='Teléfono del proveedor')
    CorreoElectronicoP = models.CharField(max_length=40, verbose_name='Correo electrónico')
    DiereccionP = models.CharField(max_length=40, verbose_name='Dirección')
    estado_proveedor = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='Activo',  # Puedes establecer un valor predeterminado aquí
        verbose_name='Estado del proveedor'
    )

    def __str__(self):
        return self.nombre_proveedor

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        db_table = 'proveedor'
        ordering = ['nombre_proveedor']

class TipoProducto(models.Model):
    nombre_Producto = models.CharField(max_length=20, verbose_name='Nombre del producto')

    def __str__(self):
        return self.nombre_Producto

    class Meta:
        verbose_name = 'Tipo de Producto'
        verbose_name_plural = 'Tipos de Productos'
        db_table = 'tipo_producto'
        ordering = ['nombre_Producto']

class Marca(models.Model):
    nombre_marca = models.CharField(max_length=20, verbose_name='Nombre de Marca')

    def __str__(self):
        return self.nombre_marca

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        db_table = 'marca'
        ordering = ['nombre_marca']
    

class Producto(models.Model):
    ESTADO_CHOICES = (
        ('Agotado', 'Agotado'),
        ('Disponible', 'Disponible'),
    )

    nombre_producto = models.CharField(max_length=60, verbose_name='Nombre del producto')
    Descripcion_Producto = models.CharField(max_length=60, verbose_name='Descripción del producto')
    PrecioProducto = models.BigIntegerField(verbose_name='Precio del producto')
    Estado_Producto = models.TextField(max_length=20, choices=ESTADO_CHOICES, verbose_name='Estado del producto')
    tipo_producto = models.ForeignKey(TipoProducto, on_delete=models.CASCADE, verbose_name='Tipo de producto')
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, verbose_name='Marca del producto')
    image= models.ImageField(upload_to='productos/', verbose_name='Imagen del producto',default='productos/default.jpg')
    slug = models.SlugField(null=False, blank=False, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre_producto)
        super(Producto, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre_producto

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'producto'
        ordering = ['nombre_producto']

class Inventario(models.Model):
    Cantidad_productos = models.IntegerField(verbose_name='Cantidad de productos')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name='Producto')
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, verbose_name='Proveedor del inventario')
    def __str__(self):
        return f'Inventario {self.id}'

    class Meta:
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventarios'
        db_table = 'inventario'
        ordering = ['id']

class Venta(models.Model):
    Fecha_venta = models.DateTimeField(verbose_name='Fecha de venta')
    total_venta = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Total de venta')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name='Cliente de la venta')
    def __str__(self):
        return f'Venta {self.id}'

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        db_table = 'venta'
        ordering = ['id']

class DetalleVenta(models.Model):
    PrecioVenta = models.BigIntegerField(verbose_name='Precio de venta')
    Cantidad = models.IntegerField(verbose_name='Cantidad')
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, verbose_name='Venta')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name='Producto')

    def __str__(self):
        return f'DetalleVenta {self.id}'

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalles de Venta'
        db_table = 'detalle_venta'
        ordering = ['id']
