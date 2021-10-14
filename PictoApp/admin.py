from django.contrib import admin
from .models import BDPictogramas
from .models import Seguimiento
from .models import Categorias
# Register your models here.
admin.site.register(BDPictogramas)
admin.site.register(Seguimiento)
admin.site.register(Categorias)