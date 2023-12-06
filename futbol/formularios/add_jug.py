from django import forms
# Se importa la app que almacena los modelos 
# y se importa la tabla/clase a la que está relacionada
# en este caso equipos.
from futbol.models import Equipos

# Tabla de jugadores
class Add_jugad(forms.Form):
    nombre=forms.CharField(max_length=100)
    apellido=forms.CharField(max_length=100)
    nacionalidad=forms.CharField(max_length=100)
    fecha_nacimiento=forms.DateField()
    # Se utilizó el ModelchoiceField para obtener todos los elementos del id de la tabla relaciona Equipos.
    pertenece_id=forms.ModelChoiceField(queryset=Equipos.objects.all(),empty_label=None, to_field_name="id")