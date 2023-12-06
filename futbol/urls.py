# Se crea un nuevo archivo llamado urls.py dentro
# de la carpeta app.
from django.urls import path
# Se importas las vistas de las api creadas en el archivo views_api.py
from.views_api import APi_Clas,APi_Clas2,APi_Clas3, InicioView

# Se establecen las url con sus Clases, y su nombre para cada api.
# De igual manera para su página de inicio.
urlpatterns = [
    path('api/', APi_Clas.as_view(), name='api_view1'),
    path('api2/',APi_Clas2.as_view(), name='api_view2'),
    path('api3/',APi_Clas3.as_view(), name='api_view3'),
    path('',InicioView.as_view(), name='inicio_view'),
]