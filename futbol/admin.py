from django.contrib import admin
from .models import Equipos, Jugadores, Noticias
# Para que se puedan visualizar las tablas cuando 
# ingresamos como admin. Cuando ejecutamos python manage.py runserver
# Y en la url de arriba a la par de los digitos colocamos /admin.
admin.site.register(Equipos)
admin.site.register(Jugadores)
admin.site.register(Noticias)
