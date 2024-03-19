from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import TipoProducto,Producto,Marca,Venta,DetalleVenta

@admin.register(Producto)
class ProductAdmin(ImportExportModelAdmin):
    fields =('nombre_producto','Descripcion_Producto','PrecioProducto','Estado_Producto','tipo_producto','marca','image')
    list_display =('__str__', 'slug',)
    list_filter = ('Estado_Producto','tipo_producto', 'marca',)


@admin.register(TipoProducto)
class TipoProductoAdmin (ImportExportModelAdmin):
   
    search_fields = ('nombre_Producto',)


@admin.register(Marca)
class MarcaAdmin (ImportExportModelAdmin):
    
    search_fields = ('nombre_marca',)

@admin.register(Venta)
class Admin (ImportExportModelAdmin):
    fields =('Fecha_venta','total_venta','cliente')
    list_filter =('Fecha_venta',)

@admin.register(DetalleVenta)
class Admin (ImportExportModelAdmin):
    fields =('PrecioVenta','Cantidad','venta','producto',)
    

