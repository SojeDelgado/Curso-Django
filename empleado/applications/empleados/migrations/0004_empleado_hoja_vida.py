# Generated by Django 4.1 on 2023-10-22 17:44

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0003_empleado_habilidades'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='hoja_vida',
            field=ckeditor.fields.RichTextField(default='texto'),
            preserve_default=False,
        ),
    ]
