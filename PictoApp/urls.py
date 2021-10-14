from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home,name="home"),
    path('categorias/', views.MostrarCategorias,name="categorias"),
    path('Jcategorias/', views.MostrarCategoriasJuego,name="categoriasJuego"),
    path('pictogramas/<categori>',views.Mostrando,name='pictogramas'),
    path('juego/<categori>',views.Jugando,name='juego'),
    path('puntuaciones/',views.Puntuaciones,name='puntuaciones'),
    path('historial/',views.Historial,name='historial'),
    #path('juego/<categori>',views.Jugando,name='juego'),
    #path('', views.Mostrando.as_view(),name='pictograms'),
    path('accounts/',include('django.contrib.auth.urls'),name='login'),
    path('abml/',views.Abml,name='abml'),
    path('agregar/',views.Agregar,name='agregar'),
    path('eliminar/',views.Eliminar,name='eliminar'),
    path('modificar/',views.Modificar,name='modificar'),
    path('modificar_ejec/',views.Modificar_Ejec,name='modificar_ejec'),
    path('pie/',views.Pie,name='pie'),
    path('error/',views.Error,name='error'),
    path('agregarCategoria/',views.AgregarCat,name='agregarCat'),
    path('eliminarCategoria/',views.EliminarCat,name='eliminarCat'),
    ] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
