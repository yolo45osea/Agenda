from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Eventos(models.Model):
    idevento = models.AutoField(primary_key=True)
    fecha = models.DateField()
    nombre = models.CharField(max_length=255)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=255)

