# Generated by Django 4.1.7 on 2023-03-09 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('correo', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha_prestamo', models.DateTimeField()),
                ('Fecha_devolucion', models.DateTimeField()),
                ('Equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laboratorio.equipo')),
                ('Personal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laboratorio.personal')),
            ],
        ),
    ]
