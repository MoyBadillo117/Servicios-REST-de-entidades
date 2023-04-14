from django.db import models

# Create your models here.

class usuarios(models.Model):
    password = models.CharField(max_length=10)

class Partida_Jugadores(models.Model):
    fecha = models.DateField()
    id_usuario = models.ForeignKey(usuarios, on_delete=models.CASCADE) 
    minutos_jugados = models.IntegerField()
    puntaje = models.IntegerField()

class Filtro(models.Model):
    idUsuario = models.IntegerField()