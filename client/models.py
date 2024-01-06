from django.db import models


class Client(models.Model):

    GENDER = [
        ('F', 'Feminino'),
        ('M', 'Masculino'),
        ('I', 'Não definido')
    ]
    STATUS = [
        ('1', 'Em dia'),
        ('2', 'Mensal'),
        ('3', 'Devedor'),
    ]
    name = models.CharField('nome', max_length=256)
    gender = models.CharField('sexo', max_length=1, choices=GENDER)
    birth_date = models.DateField('data de nascimento', blank=True, null=True)
    city = models.CharField('cidade', max_length=64, default='Teresina')
    district = models.CharField('bairro', max_length=64, default='Real Copagri')
    contact = models.CharField('contato', max_length=16, blank=True, null=True)
    email = models.EmailField('e-mail', max_length=64, blank=True, null=True)
    registration_date = models.DateField('data do cadastro', auto_now=True)
    photo = models.ImageField('foto', upload_to='cliente_fotos', blank=True, null=True)
    cpf = models.CharField('CPF', max_length=32, blank=True, null=True, unique=True)
    last_purchase_date = models.DateTimeField('data da última compra', null=True)
    status = models.CharField(max_length=1, choices=STATUS, default='3')


    def __str__(self):
        return self.name
