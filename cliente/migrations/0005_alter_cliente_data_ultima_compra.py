# Generated by Django 5.0 on 2024-01-01 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0004_rename_fone_cliente_contato_cliente_cpf_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='data_ultima_compra',
            field=models.DateTimeField(null=True, verbose_name='data da última compra'),
        ),
    ]