from django.db import models


class Cliente(models.Model):
    SEXO = [
        ('F', 'Feminino'),
        ('M', 'Masculino'),
        ('I', 'Não definido')
    ]
    nome = models.CharField(max_length=256)
    sexo = models.CharField(max_length=1, choices=SEXO)
    data_nascimento = models.DateField('data de nascimento', null=True)
    cidade = models.CharField(max_length=64, default='Teresina')
    bairro = models.CharField(max_length=64, default='Real Copagri')
    fone = models.CharField(max_length=16)
    email = models.EmailField(max_length=64)
    data_cadastro = models.DateField(auto_now=True)
