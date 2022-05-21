from django.contrib import admin
from . models import TipoEncuesta, Encuesta, Pregunta, PersonaEncuestada, ResultadoEncuesta

# Register your models here.

# Encuesta
admin.site.register(TipoEncuesta)
admin.site.register(Encuesta)
admin.site.register(Pregunta)
admin.site.register(PersonaEncuestada)
admin.site.register(ResultadoEncuesta)