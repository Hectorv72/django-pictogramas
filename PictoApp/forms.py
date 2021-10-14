from django.forms import ModelForm
from django import forms
from .models import Seguimiento
from .models import BDPictogramas
from .models import Categorias

class FormCargar(ModelForm):
	class Meta:
		model = Seguimiento
		fields = ['aciertos','errores','catelegida']
		widgets = {'aciertos': forms.HiddenInput(),
		'errores': forms.HiddenInput(),
		'catelegida': forms.HiddenInput() }

class FormCargarPicto(ModelForm):
	class Meta:
		model = BDPictogramas
		fields = ['titulo','imagen','sonido','locucion','categoria','consonido']
		widgets = {
			
		}

class FormCargarCat(ModelForm):
	class Meta:
		model = Categorias
		fields = ['nombre','cuadro']