# Generated by Django 5.0 on 2024-01-06 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0006_alter_cliente_cpf_alter_cliente_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cliente',
        ),
    ]
