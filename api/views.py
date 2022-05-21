from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from . models import TipoEncuesta, Encuesta, Pregunta, PersonaEncuestada, ResultadoEncuesta
import json
from django.http import JsonResponse
from django.utils import timezone
from datetime import datetime

# Create your views here.

class TipoEncuestaView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            tipo_encuestas = list(TipoEncuesta.objects.filter(id_tipo_encuesta=id).values())
            if len(tipo_encuestas) > 0:
                tipo_encuesta = tipo_encuestas[0]
                datos = {'status': 'success', 'tipo_encuesta': tipo_encuesta}
            else:
                datos = {'status': 'error', 'mensaje': 'No existe el tipo de encuesta con id: ' + str(id)}
            return JsonResponse(datos)
        else:
            tipo_encuestas = list(TipoEncuesta.objects.values())
            if len(tipo_encuestas) > 0:
                datos = {'status': 'success', 'tipo_encuestas': tipo_encuestas}
            else:
                datos = {'status': 'error', 'mensaje': 'No hay tipos de encuestas'}
            return JsonResponse(datos)
    
    def post(self, request):
        jd = json.loads(request.body)
        if(jd['nombre'] != ''):
            TipoEncuesta.objects.create(nombre=jd['nombre'])
            datos = {'status': 'success'}
            return JsonResponse(datos)
        else:
            datos = {'status': 'error', 'mensaje': 'El nombre no puede estar vacio'}
            return JsonResponse(datos)
    
    def put(self, request, id=0):
        jd = json.loads(request.body)
        tipo_encuestas = list(TipoEncuesta.objects.filter(id_tipo_encuesta=id).values())
        if len(tipo_encuestas) > 0:
            tipo_encuesta = TipoEncuesta.objects.get(id_tipo_encuesta=id)
            tipo_encuesta.nombre = jd['nombre']
            tipo_encuesta.save()
            datos = {'status': 'success'}
            return JsonResponse(datos)
        else:
            datos = {'status': 'error', 'mensaje': 'No existe el tipo de encuesta con id: ' + str(id)}
            return JsonResponse(datos)
    
    def delete(self, request, id=0):
        tipo_encuesta = list(TipoEncuesta.objects.filter(id_tipo_encuesta=id).values())
        if len(tipo_encuesta) > 0:
            tipo_encuesta = TipoEncuesta.objects.get(id_tipo_encuesta=id)
            tipo_encuesta.delete()
            datos = {'status': 'success'}
            return JsonResponse(datos)
        else:
            datos = {'status': 'error', 'mensaje': 'No existe el tipo de encuesta con id: ' + str(id)}
            return JsonResponse(datos)

class EncuestaView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            encuestas = list(Encuesta.objects.filter(id_encuesta=id).values())
            if len(encuestas) > 0:
                encuesta = encuestas[0]
                datos = {'status': 'success', 'encuesta': encuesta}
            else:
                datos = {'status': 'error', 'mensaje': 'No existe la encuesta con id: ' + str(id)}
            return JsonResponse(datos)
        else:
            encuestas = list(Encuesta.objects.values())
            if len(encuestas) > 0:
                datos = {'status': 'success', 'encuestas': encuestas}
            else:
                datos = {'status': 'error', 'mensaje': 'No hay encuestas'}
            return JsonResponse(datos)
    
    def post(self, request):
        jd = json.loads(request.body)
        # timezone.now() datetime.today() datetime.now()
        # now = timezone.now() => now.year now.month now.day now.hour now.minute now.second
        if(jd['nombre_encuesta'] != '' and ['tipo_encuesta_id'] != ''):
            fecha_completa = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
            Encuesta.objects.create(nombre_encuesta=jd['nombre_encuesta'], fecha=fecha_completa, tipo_encuesta_id=jd['tipo_encuesta_id'])
            datos = {'status': 'success'}
            return JsonResponse(datos)
        else:
            datos = {'status': 'error', 'mensaje': 'El nombre_encuesta, tipo_encuesta_id no puede estar vacio'}
            return JsonResponse(datos)
    
    def put(self, request, id=0):
        jd = json.loads(request.body)
        if(jd['nombre_encuesta'] != '' and ['tipo_encuesta_id'] != ''):
            encuesta = list(Encuesta.objects.filter(id_encuesta=id).values())
            if len(encuesta) > 0:
                fecha_hora = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                encuesta = Encuesta.objects.get(id_encuesta=id)
                encuesta.nombre = jd['nombre']
                encuesta.fecha = fecha_hora
                encuesta.tipo_encuesta_id = jd['tipo_encuesta_id']
                encuesta.save()
                datos = {'status': 'success'}
                return JsonResponse(datos)
            else:
                datos = {'status': 'error', 'mensaje': 'No existe la encuesta con id: ' + str(id)}
                return JsonResponse(datos)
        else:
            datos = {'status': 'error', 'mensaje': 'El nombre_encuesta, tipo_encuesta_id no puede estar vacio'}
            return JsonResponse(datos)
    
    def delete(self, request, id=0):
        encuesta = list(Encuesta.objects.filter(id_encuesta=id).values())
        if len(encuesta) > 0:
            encuesta = Encuesta.objects.get(id_encuesta=id)
            encuesta.delete()
            datos = {'status': 'success'}
            return JsonResponse(datos)
        else:
            datos = {'status': 'error', 'mensaje': 'No existe la encuesta con id: ' + str(id)}
            return JsonResponse(datos)