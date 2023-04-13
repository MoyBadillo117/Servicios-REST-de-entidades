from django.urls import include,path
from . import views 
from .views import Partidas, Usuarios
urlpatterns = [
   path('partidas',  Partidas.as_view(),name='Partidas'),
   path('partidas/<int:id>',  Partidas.as_view(),name='Partida'),
   path('usuarios',  Usuarios.as_view(),name='Partidas'),
   path('usuarios/<int:id>',  Usuarios.as_view(),name='Partida'),
   path('table', views.table,name='table'),
]