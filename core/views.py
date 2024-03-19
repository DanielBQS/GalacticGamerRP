from typing import Any
from django.shortcuts import render
from .models import Producto
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
@login_required
def index(request):
    products = Producto.objects.all()  # Obtiene todos los productos de la base de datos
    return render(request, 'index.html', {'products': products})

# Create your views here.
class ProductListView(ListView):
    template_name = 'index.html'
    queryset = Producto.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Listado de productos'

        print (context)

        return context

class ProductDetailView(DetailView):
    model = Producto
    template_name ='products/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        

        print(context)
        return context
    


class ProductSearchListView(ListView):
    template_name = 'products/search.html'

    def get_queryset(self):
        return Producto.objects.filter(nombre_producto__icontains=self.query())
    
    def query (self):
        return self.request.GET.get('q')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query()
        context['count'] = context['producto_list'].count()
        return context