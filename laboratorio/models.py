from django.db import models


# Create your models here.
class Equipo(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200, null=True)


class Personal(models.Model):
    nombre = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)


class Prestamo(models.Model):
    Equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    Personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
    Fecha_prestamo = models.DateTimeField()
    Fecha_devolucion = models.DateTimeField()
