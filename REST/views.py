from django.views.decorators.csrf import csrf_exempt
from .models import usuarios, Partida_Jugadores
from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
import json
from json import loads, dumps
from django.shortcuts import render
from django.http import HttpResponse
import sqlite3
# Create your views here.

class Usuarios(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id>0):
            users=list(usuarios.objects.filter(id=id).values())
            if len(users)>0:
                user=users[0]
                datos = {'message': "Usuario encontrado", 'users':user}
            else:
                datos = {'message':"No se ha encontrado el usuario"}
            return JsonResponse(datos)
        else:
            users = list(usuarios.objects.values()) #serializamos
            if len(users)>0:
                datos = {'message': "Succes", 'users':users}
            else:
                datos = {'message':"No se enconteraron usuarios"}
            return JsonResponse(datos)
    
    def post(self,request):
        jd = json.loads(request.body)
        usuarios.objects.create(password=jd['password'])
        datos = {'message': "Usuario añadido"}
        return JsonResponse(datos)
    
    def put(self, request,id):
        jd = json.loads(request.body)
        users= list(usuarios.objects.filter(id=id).values())#Serializamos
        if len(users)>0:
            users=usuarios.objects.get(id=id)
            users.password= jd['password']
            users.save()
            datos = {'message':"Se modificó la contraseña del usuario"}
        else:
            datos = {'message':"No se encontró el usuario"}
        return JsonResponse(datos)
    
    def delete(self, request,id):
        users = list(usuarios.objects.filter(id=id).values())
        if len(users)>0:
            usuarios.objects.filter(id=id).delete()
            datos = {'message':"Se eliminó el usuario"}
        else:
            datos = {'message':"No se encontró el usuario"}
        return JsonResponse(datos)


class Partidas(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id>0):
            partidas= list(Partida_Jugadores.objects.filter(id=id).values())
            if len(partidas)>0:
                partida=partidas[0]
                datos = {'message': "Partida encontrada", 'partidas':partida}
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
        partidas= list(Partida_Jugadores.objects.filter(id=id).values())#Serializamos
        if len(partidas)>0:
            partidas=Partida_Jugadores.objects.get(id=id)
            partidas.fecha= jd['fecha']
            partidas.id_usuario= usuarios.objects.get(pk = jd['id_usuario'])
            partidas.minutos_jugados= jd['minutos_jugados']
            partidas.puntaje= jd['puntaje']
            partidas.save()
            datos = {'message':"Se modificó la partida"}
        else:
            datos = {'message':"No se encontró la partida"}
        return JsonResponse(datos)
    
    def delete(self, request,id):
        partidas = list(Partida_Jugadores.objects.filter(id=id).values())
        if len(partidas)>0:
            Partida_Jugadores.objects.filter(id=id).delete()
            datos = {'message':"Se eliminó la partida"}
        else:
            datos = {'message':"No se encontró la partida"}
        return JsonResponse(datos)
    

"""""
def table(request):
    #data = []
    #resultados = Partida_Jugadores.objects.all() #Select * From Partida_Jugadores;
    ID = 100
    fecha = "21-02-2023"
    minutos = 30
    puntaje = 96
    #data.append([str(ID),str(fecha),str(minutos),str(puntaje)])
    elJSON = {'ID':ID,"fecha":fecha,"minutos":minutos,"puntaje":puntaje}
    return render(request,'table.html',elJSON)
"""""
    

def table(request):
    data = []
    #data.append(['Partida','Fecha','Minutos Jugados','Puntaje'])
    resultados = Partida_Jugadores.objects.all() #Select * From Partida_Jugadores;
    if len(resultados)>0:
        for registro in resultados:
            ID = registro.id
            fecha = registro.fecha
            minutos = registro.minutos_jugados     
            puntaje = registro.puntaje
            data.append([ID,str(fecha),minutos,puntaje])
        data_formato = dumps(data) #formatear los datos en string para JSON 
        elJSON = {'losDatos':data_formato}
        return render(request,'table.html',elJSON)
    else:
        return HttpResponse("<h1> No hay registros a mostrar</h1>")

