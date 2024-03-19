from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from core.views import ProductListView
from. import views

urlpatterns = [
    path('',views.IndexInicio, name='Inicio'),
    path('Productos',ProductListView.as_view(), name='index'),
    path('admin/', admin.site.urls),
#login/register
    path('usuarios/login', views.login_view, name='login'),
    path('usuarios/logout', views.logout_view, name='logout'),
    path('usuarios/register', views.register_view, name='register'),
#PQRS
    path('PQRS', views.PQRSC_view, name='PQRScliente'),
    path('PQRS/PQRSConsulta', views.PQRSConsultar_view, name='PQRSConsulta'),
    path('PQRS/PQRSActualizar/<int:pk>/', views.PQRSActualizar_view, name='PQRSActualizar'),
    path('PQRS/PQRSEliminar/<int:pk>/', views.eliminar_pqrs, name='PQRSEliminar'),
    path('respuesta_pqrs/<int:respuesta_id>/', views.ver_respuesta, name='ver_respuesta'),
#Contacto y Acerca de
    path('Contactenos', views.Contacto_view, name='Contactenos'),
    path('Acerca', views.Acerca_view, name='AcercaDe'),

#Productview
    path ('productos/', include('core.urls')),
    
    path('carrito/', include('carts.urls')),
    path('orden/', include('orders.urls')),
    path('direcciones/', include('shipping_addresses.urls')),
    path('pagos/', include('billing_profiles.urls')),




]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    
    