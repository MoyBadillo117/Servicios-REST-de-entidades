from django.contrib import admin
from .models import usuarios, Partida_Jugadores, Filtro

# Register your models here.
admin.site.register(usuarios)
admin.site.register(Partida_Jugadores)
admin.site.register(Filtro)