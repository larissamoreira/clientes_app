from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=30, unique=True)    
    telefone = models.CharField(max_length=11)
    logradouro = models.CharField(max_length=80)
    bairro = models.CharField(max_length=50)
    numero = models.IntegerField()
    cidade = models.CharField(max_length=80)
    estado = models.CharField(max_length=50)
    país = models.CharField(max_length=30)
    cep = models.CharField(max_length=8)

    def __str__(self):
        return self.nome
