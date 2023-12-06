from django.db import models
from django.db import models
from django.contrib.auth.models import Group,User
# Se mostrará tipo select cuando la persona se registre.
Group.objects.get_or_create(name='Usuario')
Group.objects.get_or_create(name='Administrador')

# Primera tabla
class Equipos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=80)
    pais =models.CharField(max_length=70)
    titulos = models.PositiveIntegerField()
    fundado = models.DateField() # Formato Ej: YYYY-MMMM-DD
    def __str__(self):
        return self.nombre
# Segunda Tabla
class Jugadores(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField() # Formato Ej: YYYY-MMMM-DD
    # Para este campo que es relacionado con la tabla Equipos se utiliza ForeingKey(TablaEquipos, se utiliza el modelo CASCADE)
    # Para que cuando un administrador elimine un dato se modifique quede como valor único.
    pertenece_id = models.ForeignKey(Equipos, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
# Tercer Tabla.
class Noticias(models.Model):
    id = models.AutoField(primary_key=True)
    resultado = models.CharField(max_length=50)
    encuentros = models.CharField(max_length=100)
    analisis = models.CharField(max_length=100)

    def __str__(self):
        return self.resultado