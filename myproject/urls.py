from django.contrib import admin
from django.urls import path

from clientes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('novo_cliente', views.novo_cliente, name='novo_cliente'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login')
]
