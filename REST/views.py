from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from django.http import Http404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from json import loads,dumps
import sqlite3 
import requests 
from .models import usuarios, Partida_Jugadores
from .serializers import usuariosSerializer, Partida_JugadoresSerializer
from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
import json
# Create your views here.


@api_view(['GET'])
@csrf_exempt
def getUsuarios(request):
    users = usuarios.objects.all()
    serializer = usuariosSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@csrf_exempt
def postUsuario(request):
    data = request.data
    user = usuarios.objects.create(
        password = data['password']
    ) 
    serializer = usuariosSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def putUsuario(request, pk):
    data = request.data
    user = usuarios.objects.get(id=pk)
    serializer = usuariosSerializer(instance=user, data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteUsuario(request, pk):
    user = usuarios.objects.get(id=pk)
    user.delete()
    return Response("Usuario eliminado")

class Partidas(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id>0):
            partidas=partidas = list(Partida_Jugadores.objects.filter(id=id).values())
            if len(partidas)>0:
                partida=partidas[0]
                datos = {'message': "Partida encontrada", 'partidas':partidas}
            else:
                datos = {'message':"No se encontró la partida"}
            return JsonResponse(datos)
        else:
            partidas = list(Partida_Jugadores.objects.values()) #serializamos
            if len(partidas)>0:
                datos = {'message': "Succes", 'partidas':partidas}
            else:
                datos = {'message':"No se encontraron partidas"}
            return JsonResponse(datos)
    
    def post(self,request):
        jd = json.loads(request.body)
        Partida_Jugadores.objects.create(fecha=jd['fecha'],id_usuario=usuarios.objects.get(pk = jd['id_usuario']),minutos_jugados=jd['minutos_jugados'],puntaje=jd['puntaje'])
        datos = {'message': "Partida añadida"}
        return JsonResponse(datos)
    
    def put(self, request,id):
        jd = json.loads(request.body)
        partidas=partidas = list(Partida_Jugadores.objects.filter(id=id).values())#Serializamos
        if len(partidas)>0:
            partidas=Partida_Jugadores.objects.get(id=id)
            partidas.fecha= jd['fecha']
            partidas.id_usuario= usuarios.objects.get(pk = jd['id_usuario'])
            partidas.minutos_jugados= jd['minutos_jugados']
            partidas.puntaje= jd['puntaje']
            partidas.save()
            datos = {'message':"Se modificó la partida"}
        else:
            datos = {'message':"No se encontró la pertida"}
        return JsonResponse(datos)
    
    def delete(self, request,id):
        partidas = list(Partida_Jugadores.objects.filter(id=id).values())
        if len(partidas)>0:
            Partida_Jugadores.objects.filter(id=id).delete()
            datos = {'message':"Se eliminó la partida"}
        else:
            datos = {'message':"No se encontró la pertida"}
        return JsonResponse(datos)

        