from django.shortcuts import render,redirect,get_object_or_404
from .formularios.registroform import NewUserForm
from .formularios.loginform import LoginForm
from .formularios import add_equi as fm
from .formularios import add_jug as fm1
from .formularios import add_notic as fm3
from django.http import HttpResponseRedirect
from .models import Equipos, Jugadores, Noticias
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,user_passes_test

# Se crea la función para registrar un usuario.
def reg_user(request):
    if request.method == "POST":
        formulario=NewUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
        return HttpResponseRedirect("/")
    else:
        formulario=NewUserForm()
        return render(request,"Reg_user.html",{"form":formulario})
# Se crea una función para el inicio principal de la página.
def index(request):
    return render(request, 'index.html')
# Se crea una función para conocer si es administrador.
def es_administrador(user):
    ver_usuario = user.is_authenticated and user.is_staff
    print(f"Usuario: {user.username}, ¿Es administrador?: {ver_usuario}")
    return ver_usuario

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

# Se utliza login_required para que se guarde el usuario registrado acceda
# a la página principal.
@login_required(login_url=login)
def index(request):
    return render(request,'index.html',{'user':request.user})

# Cuando el usuario ingrese su usuario y su contraseña. 
@login_required(login_url='login')
def index(request):
    es_usuario = request.user.groups.filter(name='Usuario').exists()
    es_admin = request.user.is_staff
    # Establecemos una condición si es ausuario o admiinistrador entrará 
    # a la página principal.
    if es_usuario or es_admin:
        return render(request, 'index.html', {'user': request.user, 'es_usuario': es_usuario, 'es_admin': es_admin})
    # Si no es ni usuario o administrador simplemente se le mostrará
    # la página principal.
    else:
        return render(request, 'index.html')

# Archivo html para visualizar la lista de equipos y la observaremos en una tabla.
@user_passes_test(es_administrador,login_url='/sin_permiso/')
def list_equi(request):
    equipos = Equipos.objects.all()
    return render(request, "lisequi.html",{'lisequi':equipos})
# Establecemos una función para conocer si es administrador
# al intentar acceder a la url de add_equi,add_jug,add_notic en la terminal dirá si
# administrador junto con su usuaurio si no no tendrá acceso.

# función no acceso
def sin_permiso(request):
    return render(request, 'sin_permiso.html')


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
@user_passes_test(es_administrador,login_url='/sin_permiso/')
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
            pertenece_id=formulario.cleaned_data["pertenece_id"]
            nuejug.pertenece_id=pertenece_id
            nuejug.save()
            return HttpResponseRedirect("/")
    else:
        formulario=fm1.Add_jugad()
    usuario_actual=request.user
    es_admin=usuario_actual.is_authenticated and usuario_actual.is_staff
    return render(request, "Add_jug.html",{"form":formulario, "es_admin":es_admin})

# Archivo html para visualizar la lista de noticias y la observaremos en una tabla.
@user_passes_test(es_administrador,login_url='/sin_permiso/')
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
