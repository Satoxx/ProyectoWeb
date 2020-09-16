#urls de la App

from django.urls import path
from ProyectoWebApp import views

urlpatterns = [

#name es un identificador para toda la url, se usa con las plantillas
    path('', views.home, name='Home'),
    path('servicios', views.servicios, name='Servicios'),
    path('tienda', views.tienda, name='Tienda'),
    path('blog', views.blog, name='Blog'),
    path('contacto', views.contacto, name='Contacto'),

]