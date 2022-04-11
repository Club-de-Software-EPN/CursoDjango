# Generated by Django 3.1.7 on 2022-04-08 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('facultad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primerNombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('tipo', models.CharField(choices=[('0', 'Nivelación'), ('1', 'Pregrado'), ('2', 'Maestría'), ('3', 'Doctorado')], max_length=1, verbose_name='Tipo')),
                ('facultad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facultad.facultad')),
            ],
        ),
    ]