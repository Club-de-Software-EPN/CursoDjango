# Generated by Django 3.1.7 on 2022-04-12 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0002_auto_20220412_0934'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='estudiante',
            options={'ordering': ['apellido', 'primerNombre'], 'verbose_name': 'Estudiante', 'verbose_name_plural': 'Estudiantes matriculados'},
        ),
    ]
