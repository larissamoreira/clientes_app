from django import forms
from .models import Cliente
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class novo_cliente_form(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'telefone', 'cep', 'logradouro', 'bairro', 'cidade', 'estado', 'numero', 'país',]
 
class cadastro_form(UserCreationForm):
    email = forms.EmailField(max_length=100, required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

class login_form(forms.ModelForm):
    email = forms.CharField(max_length=50, required=True, widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['email', 'password']
