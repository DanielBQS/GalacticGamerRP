from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404
from .models import CartProducts
from .models import Cart
from core.models import Producto
from .utils import get_or_create_cart
from .models import CartProducts


def cart(request):
    cart = get_or_create_cart(request)
        
    
    return render(request, 'carts/cart.html', {
        'cart': cart
    })
    
def add(request):
    cart = get_or_create_cart(request)
    producto = Producto.objects.get(pk=request.POST.get('producto_id'))
    quantity = request.POST.get('quantity', 1)
    
    cart.Productos.add(producto, through_defaults={
      'quantity': quantity
    })
    
    #cart_product = CartProducts.objects.create(cart=cart, producto=producto, quantity=quantity)
    
    return render(request, 'carts/add.html', {
        'producto': producto
    })
    
def remove(request):
    if request.method == 'POST':
        cart_product_id = request.POST.get('cart_product_id')
        if cart_product_id:
            try:
                cart_product = get_object_or_404(CartProducts, id=cart_product_id)
                cart = cart_product.cart  # Obtenemos el carrito al que pertenece el producto
                
                # Eliminamos el producto del carrito
                cart_product.delete()
                
                # Actualizamos el subtotal y el total del carrito
                cart.update_totals()
                
            except CartProducts.DoesNotExist:
                # Manejar el caso en que el producto no existe
                pass
    return redirect('carts:cart')