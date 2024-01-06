from django.db import models
from company_hierarchy.models import Desk, Sector


class Employee(models.Model):

    class Meta:
        verbose_name = 'empregado'
    
    name = models.CharField('nome', max_length=256)
    login = models.CharField(max_length=16, unique=True)
    sector_id = models.ForeignKey(Sector, on_delete=models.CASCADE)
    desk_id = models.ForeignKey(Desk, on_delete=models.CASCADE)
    admission_date = models.DateField('data de admissão')

    def __str__(self) -> str:
        return self.name
