# Generated by Django 4.1 on 2023-10-22 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0002_habilidades'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='habilidades',
            field=models.ManyToManyField(to='empleados.habilidades'),
        ),
    ]