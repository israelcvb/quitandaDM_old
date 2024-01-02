from django.db import models


class Cliente(models.Model):
    SEXO = [
        ('F', 'Feminino'),
        ('M', 'Masculino'),
        ('I', 'Não definido')
    ]
    STATUS = [
        ('1', 'Em dia'),
        ('2', 'Mensal'),
        ('3', 'Devedor'),
    ]
    nome = models.CharField(max_length=256)
    sexo = models.CharField(max_length=1, choices=SEXO)
    data_nascimento = models.DateField('data de nascimento', blank=True, null=True)
    cidade = models.CharField(max_length=64, default='Teresina')
    bairro = models.CharField(max_length=64, default='Real Copagri')
    contato = models.CharField(max_length=16, blank=True, null=True)
    email = models.EmailField(max_length=64, blank=True, null=True)
    data_cadastro = models.DateField('data do cadastro', auto_now=True)
    foto = models.ImageField(upload_to='cliente_fotos', blank=True, null=True)
    cpf = models.CharField('CPF', max_length=32, blank=True, null=True, unique=True)
    data_ultima_compra = models.DateTimeField('data da última compra', null=True)
    status = models.CharField(max_length=1, choices=STATUS, default='3')


    def __str__(self):
        return self.nome
