# Generated by Django 3.1.7 on 2022-04-07 14:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='A',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Publicaciones',
            fields=[
                ('idPublicacion', models.AutoField(primary_key=True, serialize=False)),
                ('tituloPublicacion', models.CharField(max_length=1020)),
                ('descripcionPublicacion', models.CharField(default='Descripción no disponible', max_length=5000)),
                ('fecha', models.DateField(default=datetime.date.today, verbose_name='Date')),
            ],
        ),
    ]
