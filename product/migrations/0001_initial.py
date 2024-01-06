# Generated by Django 5.0 on 2024-01-06 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=32, unique=True, verbose_name='Código')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Nome')),
                ('manufacturer', models.CharField(max_length=64, null=True, verbose_name='Fabricante')),
                ('description', models.TextField(max_length=128, null=True, verbose_name='Descrição')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço')),
                ('registration_date', models.DateField(auto_now_add=True, verbose_name='Data do cadastro')),
                ('manufacturing_date', models.DateField(null=True, verbose_name='Data de fabricação')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]