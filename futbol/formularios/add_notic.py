from django import forms
# Tabla de noticias
# Para la visualización en el form.
class Add_notic(forms.Form):
    resultado=forms.CharField(max_length=50)
    encuentros=forms.CharField(max_length=100)
    analisis=forms.CharField(max_length=100)