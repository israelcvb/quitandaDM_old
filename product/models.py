from django.db import models


class Product(models.Model):
    code = models.CharField("Código", max_length=32, unique=True)
    name = models.CharField("Nome", max_length=64, unique=True)
    manufacturer = models.CharField("Fabricante", max_length=64, null=True)
    description = models.TextField("Descrição", max_length=128, null=True)
    price = models.DecimalField("Preço", max_digits=8, decimal_places=2)
    registration_date = models.DateField("Data do cadastro", auto_now_add=True)
    manufacturing_date = models.DateField("Data de fabricação", null=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'produto'

    def __str__(self):
        return self.name