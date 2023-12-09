from django.db import models


class Produto(models.Model):
    codigo = models.CharField("Código", max_length=32, unique=True)
    nome = models.CharField("Nome", max_length=64, unique=True)
    fabricante = models.CharField("Fabricante", max_length=64, null=True)
    peso_bruto = models.DecimalField("Peso bruto", max_digits=8, decimal_places=2, null=True)
    unidade_peso = models.CharField("Unidade", max_length=3, null=True)
    descricao = models.TextField("Descrição", max_length=128, null=True)
    preco = models.DecimalField("Preço", max_digits=8, decimal_places=2)
    data_cadastro = models.DateField("Data do cadastro", auto_now_add=True)
    data_fabricacao = models.DateField("Data de fabricação", null=True)
    unidade_medida = models.CharField("Unidade de medida", max_length=2, null=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome
