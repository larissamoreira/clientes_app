from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cliente
from .forms import novo_cliente_form, cadastro_form, login_form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'listar_clientes.html', {'clientes':clientes})

def novo_cliente(request):
    if request.method == 'POST':
        form = novo_cliente_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = novo_cliente_form()
    return render(request, 'novo_cliente.html', {'form':form})

def editar_cliente(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    form = novo_cliente_form(request.POST or None, instance=cliente)

    if form.is_valid():
        form.save()
        return redirect('listar_clientes')
    
    return render(request, 'novo_cliente.html', {'form':form, 'cliente':cliente})

def deletar_cliente(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    cliente.delete()
    return redirect('listar_clientes')

def cadastro(request):
    if request.method == 'POST':
        form = cadastro_form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            usuario = authenticate(username=username, password=password)
            auth_login(request, usuario)
            return redirect('home')
        else:
            return HttpResponse('falhou')
    else:
        form = cadastro_form()
    return render(request, 'cadastro.html', {'form':form})


def login(request):
    if request.method == 'POST':
        form = login_form(request.POST)
        if form.is_valid():
            usuario_aux = User.objects.get(email=form.cleaned_data.get('email'))
            usuario = authenticate(username=usuario_aux.username, password=form.cleaned_data.get('password'))
            if usuario is not None:
                auth_login(request, usuario)
                return redirect('listar_clientes')
        # else:
        #     return HttpResponse('falhou')
    else:
        form = login_form()
    return render(request, 'login.html', {'form':form})

def sair(request):
    logout(request)
    return render(request, 'home.html')