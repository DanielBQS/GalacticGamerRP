from import_export import resources 
from PQRS.models import PQRS,PQRSRespuesta
from core.models import Producto,Venta,TipoProducto,Marca,DetalleVenta
from Usuarios.models import Cliente
class PQRSResource(resources.ModelResource):
    class Meta:
        model = PQRS
        

class PQRSRespuestaResource(resources.ModelResource):
    class Meta:
        model = PQRSRespuesta

class ProductoResource(resources.ModelResource):
    class Meta:
        model = Producto

class VentaResource(resources.ModelResource):
    class Meta:
        model = Venta

class TipoProductoResource(resources.ModelResource):
    class Meta:
        model = TipoProducto

class MarcaResource(resources.ModelResource):
    class Meta:
        model = Marca

class DetalleVentaResource(resources.ModelResource):
    class Meta:
        model = DetalleVenta

class ClienteResource(resources.ModelResource):
    class Meta:
        model = Cliente