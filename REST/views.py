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
