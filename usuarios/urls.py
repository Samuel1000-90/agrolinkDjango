from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns =[
    path('registro/', views.mostrar_registro_usuarios, name='registrar'),
    path('registrar/', views.registrar_usuario, name='registrar_usuario'),
]