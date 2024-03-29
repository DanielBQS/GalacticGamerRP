"""
Django settings for ProyectoGAE4Galactic1 project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from.import db as db
import os
from django.utils.translation import gettext_lazy as _
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!^rr*&eu%i4^-)%0ei(nspd$0-5es_q1gyxu5bt68c3-oa177@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'import_export',
    'core',
    'billing_profiles',
    'charges',
    'orders',
    'carts',
    'Usuarios',
    'shipping_addresses',
    'PQRS',
    'paypal.standard.ipn',
    'colorfield',
    'ecom',
    

]

#Configuracino de Jazzmin panel de administrador personalizado
JAZZMIN_SETTINGS = {
# Título de la ventana (Se establecerá en current_admin_site.site_title si está ausente o None)
"site_title": "Galactic Gamer Admin",

# Título en la pantalla de inicio de sesión (máximo 19 caracteres) (se establece en current_admin_site.site_header si está ausente o None)
"site_header": "Galactic Gamer Administracion",

# Título en la marca (máximo 19 caracteres) (se establece en current_admin_site.site_header si está ausente o None)
"site_brand": "Galactic Admin",

# Logo para usar en tu sitio, debe estar presente en archivos estáticos, usado para la marca en la parte superior izquierda
"site_logo": "../static/img/logo.png",

# Logo para usar en el formulario de inicio de sesión (se establece en site_logo si está ausente)
"login_logo": None,

# Logo para usar en el formulario de inicio de sesión en temas oscuros (se establece en login_logo por defecto)
"login_logo_dark": None,

# Clases de CSS que se aplican al logotipo arriba
"site_logo_classes": "img-circle",

# Texto de bienvenida en la pantalla de inicio de sesión
"welcome_sign": "Bienvenido a la Administracion de Galactic Gamer",

# Derechos de autor en el pie de página
"copyright": "Galactic Gamer",


# Nombre del campo en el modelo de usuario que contiene el avatar ImageField/URLField/Charfield o una función llamada que recibe al usuario
"user_avatar": None,

############
# Menú Superior #
############

# Enlaces para poner a lo largo del menú superior
"topmenu_links": [

    # Url que se invierte (los permisos se pueden agregar)
    {"name": "Inicio",  "url": "admin:index", "permissions": ["auth.view_user"]},

  
    # administrador de modelos al que enlazar (Permisos verificados contra el modelo)
    {"model": "auth.User"},

    # Aplicación con menú desplegable a todas sus páginas de modelos (Permisos verificados contra los modelos)
    {"app": "books"},
],

#############
# Menú de Usuario #
#############

# Enlaces adicionales para incluir en el menú de usuario en la parte superior derecha (el tipo de url "app" no está permitido)
"usermenu_links": [
    {"name": "Ver Sitio", "url": "#", "new_window": True},
    {"model": "auth.user"}
],

#############
# Menú Lateral #
#############

# Si mostrar el menú lateral
"show_sidebar": True,

# Si expandir automáticamente el menú
"navigation_expanded": True,

# Ocultar estas aplicaciones al generar el menú lateral, por ejemplo (auth)
"hide_apps": [],

# Ocultar estos modelos al generar el menú lateral (p. ej., auth.user)
"hide_models": [],

"hide_apps": ["billing_profiles", "charges"],

# Iconos personalizados para aplicaciones/modelos del menú lateral
"icons": {
    
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "carts.Cart": "fas fa-shopping-cart",  
        "core.Producto": "fas fa-box",    
        "core.Marca": "fas fa-tag",      
        "core.Tipo": "fas fa-tags",        
        "core.Venta": "fas fa-money-bill",  
        "Usuarios.user": "fas fa-user",
        "PQRS.PQRS": "fas fa-comments",  
        "PQRS.PQRSRespuesta": "fas fa-reply",
        "Usuarios.Cliente": "fas fa-users",  
        "core.DetalleVenta": "fas fa-list-alt",
        "core.TipoProducto": "fas fa-cubes", 
},
# Iconos que se utilizan cuando no se especifica manualmente uno
"default_icon_parents": "fas fa-chevron-circle-right",
"default_icon_children": "fas fa-circle",

# Rutas relativas a CSS/JS personalizados (deben estar presentes en archivos estáticos)
"custom_css": None,

# Si enlazar fuente desde fonts.googleapis.com (usa custom_css para proporcionar la fuente de lo contrario)
"use_google_fonts_cdn": True,
# Si mostrar el personalizador de interfaz de usuario en la barra lateral
"show_ui_builder": False,
 "theme": "dark", # Tema de color predefinido ('default', 'dark', 'flat', 'soft')

"theme_color": "warning",  # Color principal del tema ('primary', 'success', 'info', 'warning', 'danger')

# Personalización de los colores de los botones
"button_color": "#259FB8",

}


X_FRAME_OPTIONS = 'SAMEORIGIN'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ProyectoGAE4Galactic1.urls'
AUTH_USER_MODEL= 'Usuarios.User'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['Templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ProyectoGAE4Galactic1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = db.MYSQL


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'es'
LANGUAGES = [
    ('es', _('Spanish')),
    
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STRIPE_PUBLIC_KEY = 'pk_test_51OvmzqKyVYF4gNaGmVSZCQk40Uami0nheHS355BQAODG2O9akhIRMipxsp4k7gNnR9K8OIBT0Nxr9v1wth5yeX0U00Dqldge61'
STRIPE_PRIVATE_KEY = 'sk_test_51OvmzqKyVYF4gNaG2oYpY1Y1MJbkJ6yYqcdY5tRCcxalcseFELT9ez1KdxsfAhblqREWcHUPmiDyI0PiuJWUJJj800TE4jRphY'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
IMPORT_EXPORT_USE_TRANSACTIONS =True
STATIC_URL = 'static/'
STATICFILES_DIRS=(
    os.path.join(BASE_DIR, 'static'),
)

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



#PayPal Settings

PAYPAL_RECEIVER_EMAIL = 'galacticgamer.gg.sas@gmail.com'
PAYPAL_TEST = True


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
