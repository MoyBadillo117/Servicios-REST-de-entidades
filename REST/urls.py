from django.urls import include,path
from rest_framework import routers
from . import views 

urlpatterns = [
   path('get', views.getUsuarios),
   path('post', views.postUsuario),
   path('put/<int:pk>', views.putUsuario),
]