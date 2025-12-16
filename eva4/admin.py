from django.contrib import admin
from .models import Agente, Propietario, Propiedad, Visita
# Register your models here.
admin.site.register(Agente)
admin.site.register(Propietario)
admin.site.register(Propiedad)
admin.site.register(Visita)