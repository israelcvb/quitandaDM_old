from django.db import models

# Create your models here.
class Sector(models.Model):

    class Meta:
        verbose_name = 'setor'
        verbose_name_plural = 'setores'

    name = models.CharField('nome', max_length=256, unique=True)
    acronym = models.CharField('sigla', max_length=8, unique=True)
    service = models.TextField('descrição do serviço', max_length=512)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.acronym


class Desk(models.Model):

    class Meta:
        verbose_name = 'escritório'

    desk_city = models.CharField('escritório', max_length=128, unique=True)

    def __str__(self) -> str:
        return self.desk_city
