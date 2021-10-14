from django.db import models
from django import forms

def subir_imagen(instance, filename):
	return 'imagenes/%s'% filename

def subir_sonido(instance, filename):
	return 'sonidos/%s'% filename

def subir_locucion(instance, filename):
	return 'locuciones/%s'% filename

def subir_categoria(instance, filename):
	return 'categorias/%s'% filename
	

class Categorias(models.Model):
	nombre = models.CharField(max_length=30)
	cuadro = models.ImageField(upload_to=subir_categoria, null=True)
	
	def __str__(self):
		return self.nombre
	

class BDPictogramas(models.Model):
	titulo = models.TextField (max_length=35)
	imagen = models.ImageField(upload_to=subir_imagen)
	sonido = models.FileField(upload_to=subir_sonido, blank=True, null=True)
	locucion = models.FileField(upload_to=subir_locucion)
	categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE, null=True)

	SONIDO_OPTIONS = (
	(1,'Tiene'),
	(2,'No tiene'),
	)
	consonido = models.IntegerField(choices=SONIDO_OPTIONS, default=SONIDO_OPTIONS)

	def __str__(self):
		return self.titulo

class Seguimiento(models.Model):
	fecha = models.DateField(auto_now=True)
	aciertos = models.IntegerField()
	errores = models.IntegerField()
	catelegida = models.ForeignKey(Categorias, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return str(self.fecha)