# Generated by Django 5.0 on 2023-12-31 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_cliente_foto_alter_cliente_data_nascimento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='cliente_fotos'),
        ),
    ]
