from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cliente
from .forms import novo_cliente_form, cadastro_form, login_form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User

def home(request):
    clientes = Cliente.objects.all()
    return render(request, 'home.html', {'clientes':clientes})

def novo_cliente(request):
    if request.method == 'POST':
        form = novo_cliente_form(request.POST)
        if form.is_valid():
            cliente = Cliente.objects.create(
                nome = form.cleaned_data.get('nome'),
                telefone = form.cleaned_data.get('telefone'),
                cep = form.cleaned_data.get('cep'),
                logradouro = form.cleaned_data.get('logradouro'),
                bairro = form.cleaned_data.get('bairro'),
                cidade = form.cleaned_data.get('cidade'),
                estado = form.cleaned_data.get('estado'),
                país = form.cleaned_data.get('país'),
                numero = form.cleaned_data.get('numero')
            )
            return redirect('home')
    else:
        form = novo_cliente_form()
    return render(request, 'novo_cliente.html', {'form':form})

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
                return redirect('home.html')
    else:
        form = login_form()
    return render(request, 'login.html', {'form':form})
