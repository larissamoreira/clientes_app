from django import forms
from .models import Cliente

class novo_cliente_form(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'telefone', 'cep', 'logradouro', 'bairro', 'cidade', 'estado','país', 'numero']
 