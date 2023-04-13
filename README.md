# Servicios-REST-de-entidades

Se crearon servicios REST a través de Django-Python para dos entidades relacionadas entre sí.

Después del tercer intento finalmente salió.

En este tercer intento no se usó la libreria de rest_framework por motivos de practicidad. 

Para probar este código es necesario usar el software PostMan y no RestMan debido a que el host de RestMan esta bloqueado. 

Una vez en Postman añadir la IP y la API que se quiera probar, ya sea usuarios o partidas. Una vez se ingrese la API, se selecciona el método ya sea GET, POST, PUT o delete.

Ejemplos de como se debe ingresar los Json de entrada:
usuarios:
{
	"password": "EstaEsLaPrueba8"
}

partidas:
{
"fecha": "2023-04-05",
"id_usuario": 8,
"minutos_jugados": 50,
"puntaje": 100
}

"direccion"/usuarios
"direccion"/usuarios/<NúmeroEntero>
"direccion"/partidas
"direccion"/partidas/<NúmeroEntero>
