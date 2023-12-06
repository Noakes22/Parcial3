# Se utiliza el rest_framework instalado en nuestra terminal
# y el establecido en la INSTALLED APPS.
from rest_framework import serializers
# Se utilizan los modelos de las APP
from .models import Equipos,Jugadores,Noticias

# Se crean el frame para cada modelo
class FrameSerialiazer(serializers.ModelSerializer):
    class Meta:
        # Se establece la tabla a necesitar.
        model=Equipos
        # Se utilizan los campos de las tablas.
        fields = ["id","nombre","ciudad","pais","titulos","fundado"]
# De igual manera se hace con las otras, y en esta como es una tabla relacionada
# con la tabla Equipos se necesita el campo pertenece_id.
class FrameSerialiazer1(serializers.ModelSerializer):
    class Meta:
        model=Jugadores
        fields = ["id","nombre","apellido","nacionalidad","fecha_nacimiento","pertenece_id"]

class FrameSerialiazer2(serializers.ModelSerializer):
    class Meta:
        model=Noticias
        fields = ["id","resultado","encuentros","analisis"]
