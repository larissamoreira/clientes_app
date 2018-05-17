from django.contrib import admin
from django.urls import path

from clientes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('listar_clientes', views.listar_clientes, name='listar_clientes'),
    path('novo_cliente', views.novo_cliente, name='novo_cliente'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login'),
    path('sair', views.sair, name='sair'),
    path('editar_cliente/<int:pk>', views.editar_cliente, name="editar_cliente"),
    path('deletar_cliente/<int:pk>', views.deletar_cliente, name="deletar_cliente")
]
