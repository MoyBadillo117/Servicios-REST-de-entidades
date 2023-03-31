from django.urls import include,path
from rest_framework import routers
from . import views 
from .views import Partidas 
urlpatterns = [
   path('get', views.getUsuarios),
   path('post', views.postUsuario),
   path('put/<int:pk>', views.putUsuario),
   path('delete/<int:pk>', views.deleteUsuario), 
   path('partidas',  Partidas.as_view(),name='Partidas'),
   path('partidas/<int:id>',  Partidas.as_view(),name='Partida'),
]