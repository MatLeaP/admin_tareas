# Generated by Django 4.1 on 2022-10-04 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tareas', '0012_area_tarea_usuario_carga_tarea_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='descripcion',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]