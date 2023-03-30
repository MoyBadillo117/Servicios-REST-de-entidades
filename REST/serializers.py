from rest_framework import serializers
from . models import usuarios,Partida_Jugadores


class usuariosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = usuarios
        fields = ('id','password')

class Partida_JugadoresSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Partida_Jugadores
        fields = ('id','fecha','id_usuario','minutos_jugados','puntaje')