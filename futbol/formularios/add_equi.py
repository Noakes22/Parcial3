from django import forms
# Para la visualización en el form.
# Tabla Para los equipos
class Add_Equi(forms.Form):
    nombre=forms.CharField(max_length=100)
    ciudad=forms.CharField(max_length=100)
    pais=forms.CharField(max_length=80)
    titulos=forms.IntegerField()
    fundado=forms.DateField() # Formato Ej: YYYY-MMMM-DD