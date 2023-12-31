from django.db import models


class Cliente(models.Model):
    SEXO = [
        ('F', 'Feminino'),
        ('M', 'Masculino'),
        ('I', 'Não definido')
    ]
    nome = models.CharField(max_length=256)
    sexo = models.CharField(max_length=1, choices=SEXO)
    data_nascimento = models.DateField('data de nascimento', blank=True, null=True)
    cidade = models.CharField(max_length=64, default='Teresina')
    bairro = models.CharField(max_length=64, default='Real Copagri')
    fone = models.CharField(max_length=16, blank=True, null=True)
    email = models.EmailField(max_length=64, blank=True, null=True)
    data_cadastro = models.DateField(auto_now=True)
    foto = models.ImageField(upload_to='cliente_fotos', blank=True, null=True)

    def __str__(self):
        return self.nome
