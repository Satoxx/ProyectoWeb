from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

#name es un identificador para toda la url, se usa con las plantillas

    path('', views.servicios, name='Servicios'),

]

