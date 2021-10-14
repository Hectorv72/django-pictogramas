from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView
from .forms import FormCargar
from .forms import FormCargarPicto
from .forms import FormCargarCat
from .models import BDPictogramas
from .models import Categorias
from .models import Seguimiento
from django.contrib.auth.decorators import login_required
import matplotlib.pyplot as plt
import random


# Create your views here.
def home(request):
    return render(request,'PictoApp/home.html')

def Error(request):
    return render(request,'PictoApp/error.html')

@login_required
def Abml(request):
    return render(request,'PictoApp/abml.html')

@login_required
def Agregar(request):
    if request.method == "POST":
        form = FormCargarPicto(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            valido = True
            form = FormCargarPicto()
    else:
        form = FormCargarPicto()
        valido = False
    
    return render(request,'PictoApp/agregar.html',{
 'formulario':form, 'val':valido})

@login_required
def Eliminar(request):
    if request.method == "POST":
        id = request.POST['pictoid']
        instance = BDPictogramas.objects.get(id=id)
        instance.delete()
        carga = []
        for i in BDPictogramas.objects.all().order_by('categoria') :
            carga.append(i)
    else:
        carga = []
        for i in BDPictogramas.objects.all():
            carga.append(i)

    return render(request,'PictoApp/eliminar.html',{'formulario':carga})

@login_required
def AgregarCat(request):
    if request.method == "POST":
        form = FormCargarCat(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            valido = True
            form = FormCargarCat()
        carga = []
        for i in Categorias.objects.all():
            carga.append(i)
    else:
        valido = False
        form = FormCargarCat()
        carga = []
        for i in Categorias.objects.all():
            carga.append(i)

    return render(request,'PictoApp/agregarCategoria.html',{'formulario':form,
    'val':valido,
    'archivos':carga
    })

@login_required
def EliminarCat(request):
    val = 'No Elimino'
    if request.method == "POST":
        form = FormCargarCat(request.POST)
        id = request.POST['catid']
        instance = Categorias.objects.get(id=id)
        instance.delete()
        val = 'Se elimino categoria'

    return render(request,'PictoApp/eliminarCat.html',{'verif':val})

@login_required
def Modificar(request):
    tablas = ""
    carga = []
    form = FormCargarPicto()
    for i in BDPictogramas.objects.all():
        carga.append(i)

    if request.method == "POST":
        id = request.POST['pictogramas']
        valid = True
        tablas = random.choice(BDPictogramas.objects.all().filter(id=id))
    else:
        valid = False
        id = 0

    return render(request,'PictoApp/modificar.html',{'combo':carga,
    'validar':valid,
    'tablas':tablas,
    'formulario':form,
    'idpic':id,
    })

@login_required
def Modificar_Ejec(request):
    if request.method == "POST":
        form = FormCargarPicto(request.POST,request.FILES)
        if form.is_valid():
            post = BDPictogramas.objects.get( id = request.POST['idpic'] )
            post.titulo = request.POST['titulo']

            post.categoria_id = request.POST['categoria']
            post.consonido_id = request.POST['titulo']

            if request.FILES['imagen'] != "":
                post.imagen = request.FILES['imagen']

            if request.FILES.get('sonido', False) != False:
                post.sonido = request.FILES['sonido']
            else:
                post.categoria_id = 2

            if request.FILES['locucion'] != "":
                post.locucion = request.FILES['locucion']


            post.save()
            val = "Se modifico correctamente"
        else:
            val = "No se pudo modificar, por favor vuelva a intentarlo"
    else:
        val = "Ningun valor fue ingresado"

            
            

        
    return render(request,'PictoApp/modificar_ejec.html',{"verif":val})

#Mostrar Puntuacion del Juego
def Puntuaciones(request):
 if request.method == "POST":
  form = FormCargar(request.POST)
  if form.is_valid():
   if Seguimiento.objects.filter( catelegida = request.POST['catelegida'] ).exists():
    post = Seguimiento.objects.get( catelegida = request.POST['catelegida'] )

    valores = random.choice(Seguimiento.objects.all().filter( catelegida = request.POST['catelegida'] ))
    
    post.aciertos = valores.aciertos + int(request.POST['aciertos'])
    post.errores = valores.errores + int(request.POST['errores'])
    post.save()
   else:
    post = form.save(commit=False)
    post.save()
  aciertos = request.POST['aciertos']
  errores = request.POST['errores']
  categoria = random.choice(Categorias.objects.all().filter( id = request.POST['catelegida'] ))

 return render(request,'PictoApp/Puntuaciones.html',{
 'aciertos':aciertos,
 'errores':errores,
 'categoria':categoria,
 })

#Historial de Jugados
def Historial(request):
    histPuntaje = []
    
    for i in Seguimiento.objects.all():
        histPuntaje.append(i)
    return render(request,'PictoApp/Historial.html',{'Puntaje':histPuntaje})

#Mostrar Categorias de Mostrar Pictogramas
def MostrarCategorias(request):
    cantCategorias = []
    for i in Categorias.objects.all():
        cantCategorias.append(i)
    return render(request,'PictoApp/Categorias.html',{'Categoria': cantCategorias})

#Mostrar Categorias de Juego Preguntas
def MostrarCategoriasJuego(request):
    cantCategorias = []
    for i in Categorias.objects.all():
        cantCategorias.append(i)
    return render(request,'PictoApp/juegoCategorias.html',{'Categoria': cantCategorias})


#Monstrar Pictogramas
def Mostrando(request,categori):
    permitir = 0
    bd = BDPictogramas.objects.all().filter(categoria = categori)
    for i in bd:
        permitir += 1
    if permitir > 0:
        idC = categori
        Picto = random.choice(BDPictogramas.objects.filter(categoria = categori))
        valor = Picto.titulo
        valor = valor.upper()
        return render(request,'PictoApp/mostrarImagen.html',{'Pic':Picto,'idCategoria':idC,'nombre':valor})
    else:
        return render(request,'PictoApp/error.html')

#Juego de Preguntas
def Jugando(request,categori):
    permitir = 0
    bd = BDPictogramas.objects.all().filter(categoria = categori)
    for i in bd:
        permitir += 1

    if permitir > 1:
        bd = BDPictogramas.objects.filter(categoria = categori)
        RespCorrecta = random.choice(bd)
        azar = [1,2]
        eleccion = random.choice(azar)
        if eleccion == 1:
            Opcion1 = RespCorrecta
            Opcion2 = random.choice(bd)
            while Opcion2 == Opcion1:
                Opcion2 = random.choice(bd)
        else:
            Opcion2 = RespCorrecta
            Opcion1 = random.choice(bd)
            while Opcion1 == Opcion2:
                Opcion1 = random.choice(bd)

        Palabra = RespCorrecta.titulo
        UltLetra = Palabra[len(Palabra)-1]
        if UltLetra == 'a':
            EoA = 'una'
        else:
            EoA = 'un'
        form = FormCargar()
        return render(request,'PictoApp/juegoPregunta.html',{'Correcta':RespCorrecta,
        'Op1':Opcion1,
        'Op2':Opcion2,
        'formulario':form,
        'EoA':EoA,})
    else:
        return render(request,'PictoApp/error.html')


#Torta
def Pie(request):
    if request.method == "POST":
        id = request.POST['grafic']
        base = random.choice(Seguimiento.objects.filter(id = id))

    return render(request,'PictoApp/torta.html',{'Base':base})
