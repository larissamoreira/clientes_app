from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cliente
from .forms import novo_cliente_form

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
