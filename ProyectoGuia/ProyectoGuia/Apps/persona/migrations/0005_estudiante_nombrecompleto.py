# Generated by Django 3.1.7 on 2022-04-19 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0004_auto_20220412_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='nombreCompleto',
            field=models.CharField(blank=True, max_length=100, verbose_name='Nombre Completo'),
        ),
    ]
