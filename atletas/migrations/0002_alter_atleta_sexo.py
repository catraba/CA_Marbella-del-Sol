# Generated by Django 3.2.4 on 2021-07-21 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atletas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atleta',
            name='sexo',
            field=models.CharField(choices=[('Masculino', 'M'), ('Femenino', 'F')], max_length=9),
        ),
    ]
