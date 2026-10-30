from django.db import models
from django.utils import timezone

# Create your models here.
class RamaDerecho(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50) #publico o privado
    descripcion = models.TextField()
    ejemplo= models.TextField(blank=True)

    class Meta:
        ordering=['nombre']

    def __str__(self):
        return self.nombre


class Termino(models.Model):
    palabra=models.CharField(max_length=100)
    definicion=models.TextField()
    ejemplo=models.TextField(blank=True)
    rama=models.ForeignKey(RamaDerecho, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_creacion=models.DateTimeField(default=timezone.now)

    class Meta:
        ordering=['palabra']

    def __str__(self):
        return self.palabra


class Sugerencia(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    mensaje = models.TextField()
    fecha = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.palabra
