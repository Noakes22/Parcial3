from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions,status
from rest_framework.response import Response
# Se importan los modulos Equipos, Jugadores,Noticias
# para acceder a ellos.
from .models import Equipos, Jugadores, Noticias
# Se importa el archivo serializer de nuestra app.
from .serializers import FrameSerialiazer,FrameSerialiazer1,FrameSerialiazer2
# Se utiliza tanto user_passes_test y el method_decorator para
# que evalue si el usuario es administrador o no.
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
# Parte Del código En La View De Nuestra APP.

# Confirmar si el usuario es administrador
def es_administrador(user):
    # Mostramos en terminal si lo es.
    ver_usuario = user.is_authenticated and user.is_staff
    print(f"Usuario: {user.username}, ¿Es administrador?: {ver_usuario}")
    return ver_usuario

# Home de las api
class InicioView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


# La primera Api
class APi_Clas(APIView):
    permission_classes=[permissions.IsAuthenticated]
    # Aquí se utiliza el method_decorator y el user_passes_test y se le pasa como parámetro
    # la función del administrador seguidamente confirmando hacia donde lo enviará si no lo es
    # es decir a un página que no tendrá acceso.
    @method_decorator(user_passes_test(es_administrador, login_url='/sin_permiso/'))
    def post(self,request,*args,**kwargs):
        informacion={
            "id": request.data.get("id"),
            "nombre": request.data.get("nombre"),
            "ciudad": request.data.get("ciudad"),
            "pais": request.data.get("pais"),
            "titulos": request.data.get("titulos"),
            "fundado": request.data.get("fundado")
        }
        serializares=FrameSerialiazer(data=informacion)
        if serializares.is_valid():
            serializares.save()
            return Response(serializares.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializares.errors, status=status.HTTP_400_BAD_REQUEST)
    # Se utiliza también para la función get.
    # Esto aplica para todas las Api.
    @method_decorator(user_passes_test(es_administrador, login_url='/sin_permiso/'))
    def get(self,request,*args,**kwargs):
        frame1=Equipos.objects.all()
        serializer=FrameSerialiazer(frame1,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# La segunda Api    
class APi_Clas2(APIView):
    permission_classes=[permissions.IsAuthenticated]
    @method_decorator(user_passes_test(es_administrador, login_url='/sin_permiso/'))
    def post(self,request,*args,**kwargs):
        informacion={
            "id": request.data.get("id"),
            "nombre": request.data.get("nombre"),
            "apellido": request.data.get("apellido"),
            "nacionalidad": request.data.get("nacionalidad"),
            "fecha_nacimiento": request.data.get("fecha_nacimiento"),
            "pertenece_id": request.data.get("pertenece_id")
        }
        serializares=FrameSerialiazer1(data=informacion)
        if serializares.is_valid():
            serializares.save()
            return Response(serializares.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializares.errors, status=status.HTTP_400_BAD_REQUEST)
    @method_decorator(user_passes_test(es_administrador, login_url='/sin_permiso/'))
    def get(self,request,*args,**kwargs):
        frame2=Jugadores.objects.all()
        serializer=FrameSerialiazer1(frame2,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# La tercera Api
class APi_Clas3(APIView):
    permission_classes=[permissions.IsAuthenticated]
    @method_decorator(user_passes_test(es_administrador, login_url='/sin_permiso/'))
    def post(self,request,*args,**kwargs):
        informacion={
            "id": request.data.get("id"),
            "resultado": request.data.get("resultados"),
            "encuentros": request.data.get("encuentros"),
            "analisis": request.data.get("analisis")
        }
        serializares=FrameSerialiazer2(data=informacion)
        if serializares.is_valid():
            serializares.save()
            return Response(serializares.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializares.errors, status=status.HTTP_400_BAD_REQUEST)
    @method_decorator(user_passes_test(es_administrador, login_url='/sin_permiso/'))
    def get(self,request,*args,**kwargs):
        frame3=Noticias.objects.all()
        serializer=FrameSerialiazer2(frame3,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
"""
def reg_user(request):
    if request.method == "POST":
        formulario=NewUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
        return HttpResponseRedirect("/")
    else:
        formulario=NewUserForm()
        return render(request,"Reg_user.html",{"form":formulario})
def index(request):
    return render(request, 'index.html')

# Función para iniciar sesión
def iniciar_sesion(request):
    if request.method=='POST':
        form=LoginForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})

# Cerrar sesión
def cerrar_sesion(request):
    logout(request)
    return redirect('login')

@login_required(login_url=login)
def index(request):
    return render(request,'index.html',{'user':request.user})

@login_required(login_url='login')
def index(request):
    es_usuario=request.user.groups.filter(name='Usuario').exists()
    es_admin=request.user.is_staff
    if es_usuario or es_admin:
        return render(request,'index.html',{'user':request.user,'es_usuario':es_usuario,'es_admin':es_admin})

# Archivo html para visualizar la lista de equipos y la observaremos en una tabla.
def list_equi(request):
    equipos = Equipos.objects.all()
    return render(request, "lisequi.html",{'lisequi':equipos})
# Establecemos una función para conocer si es administrador
# al intentar acceder a la url de add_equi,add_jug,add_notic en la terminal dirá si
# administrador junto con su usuaurio si no no tendrá acceso.

def es_administrador(user):
    ver_usuario = user.is_authenticated and user.is_staff
    print(f"Usuario: {user.username}, ¿Es administrador?: {ver_usuario}")
    return ver_usuario

# función no acceso
def sin_permiso(request):
    return render(request, 'sin_permiso.html')
"""
"""
# Usamos user_passes_test y como parámetros el nombre de la función
# del administrador, y el login /sin_permiso/ del archivo html si cumple.
# para añadir equipos,jugadores,noticias.
@user_passes_test(es_administrador,login_url='/sin_permiso/')
def add_equi(request):
    if request.method == "POST":
        formulario = fm.Add_Equi(request.POST)
        if formulario.is_valid():
            nuequ=Equipos() # Para la clase de la tabla Equipos
            nuequ.nombre=formulario.cleaned_data["nombre"] # Se obtiene el nombre
            nuequ.ciudad=formulario.cleaned_data["ciudad"] # La ciudad
            nuequ.pais=formulario.cleaned_data["pais"]
            nuequ.titulos=formulario.cleaned_data["titulos"]
            nuequ.fundado=formulario.cleaned_data["fundado"]
            nuequ.save()
            return HttpResponseRedirect("/")
    else:
        formulario=fm.Add_Equi()
    usuario_actual=request.user
    es_admin=usuario_actual.is_authenticated and usuario_actual.is_staff
    return render(request, "Add_equi.html",{"form":formulario, "es_admin":es_admin})
# Archivo html para visualizar la lista de jugadores y la observaremos en una tabla.
def list_jug(request):
    jugadores = Jugadores.objects.all()
    return render(request, "lisjug.html",{'lisjug':jugadores})

# Añadir jugador si es administrador.
@user_passes_test(es_administrador,login_url='/sin_permiso/')
def add_jug(request):
    if request.method == "POST":
        formulario = fm1.Add_jugad(request.POST)
        if formulario.is_valid():
            nuejug=Jugadores() # Para la clase de la tabla Equipos
            nuejug.nombre=formulario.cleaned_data["nombre"] # Se obtiene el nombre
            nuejug.apellido=formulario.cleaned_data["apellido"] # La ciudad
            nuejug.nacionalidad=formulario.cleaned_data["nacionalidad"]
            nuejug.fecha_nacimiento=formulario.cleaned_data["fecha_nacimiento"]
            perteneceid=formulario.cleaned_data["perteneceid"]
            nuejug.perteneceid=get_object_or_404(Equipos,id=perteneceid)
            nuejug.save()
            return HttpResponseRedirect("/")
    else:
        formulario=fm1.Add_jugad()
    usuario_actual=request.user
    es_admin=usuario_actual.is_authenticated and usuario_actual.is_staff
    return render(request, "Add_jug.html",{"form":formulario, "es_admin":es_admin})

# Archivo html para visualizar la lista de noticias y la observaremos en una tabla.
def list_notic(request):
    noticias = Noticias.objects.all()
    return render(request, "lisnotic.html",{'lisnotic':noticias})

# Añadir jugador si es administrador.
@user_passes_test(es_administrador,login_url='/sin_permiso/')
def add_notic(request):
    if request.method == "POST":
        formulario = fm3.Add_notic(request.POST)
        if formulario.is_valid():
            nuenot=Noticias() # Para la clase de la tabla Noticias
            nuenot.resultado=formulario.cleaned_data["resultado"] # Se obtiene el resultado
            nuenot.encuentros=formulario.cleaned_data["encuentras"] # Los encuentros próximos
            nuenot.analisis=formulario.cleaned_data["analisis"]
            nuenot.save()
            return HttpResponseRedirect("/")
    else:
        formulario=fm3.Add_notic()
    usuario_actual=request.user
    es_admin=usuario_actual.is_authenticated and usuario_actual.is_staff
    return render(request, "Add_notic.html",{"form":formulario, "es_admin":es_admin})
"""