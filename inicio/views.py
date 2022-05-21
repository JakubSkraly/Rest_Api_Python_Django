from django.shortcuts import render

# Create your views here.

def inicio(request):
    title = "Happy Healthy Mind | Inicio"
    nombre_app = "Happy Healthy Mind"
    return render(request, 'inicio/inicio.html',{
        'title': title,
        'nombre_app': nombre_app,
    })