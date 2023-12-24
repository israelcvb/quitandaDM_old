from django.db import models


class Documento(models.Model):
    num_doc = models.CharField(max_length=64)

    def __str__(self):
        return self.num_doc


class Todo(models.Model):
    nome = models.CharField(max_length=128)
    feito = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)
