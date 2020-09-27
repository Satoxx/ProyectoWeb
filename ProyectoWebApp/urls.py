#urls de la App

from django.urls import path
from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

#name es un identificador para toda la url, se usa con las plantillas
    path('', views.home, name='Home'),
    path('tienda', views.tienda, name='Tienda'),
    path('blog', views.blog, name='Blog'),
    path('contacto', views.contacto, name='Contacto'),

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)