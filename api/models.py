from django.db import models

# Create your models here.

class PersonaEncuestada(models.Model):
    id_persona_encuestada = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=100, verbose_name='Nombre Completo de la Persona Encuestada', null=False)
    sexo = models.CharField(max_length=10, verbose_name='Sexo de la Persona Encuestada', null=False)
    correo = models.EmailField(verbose_name='Correo de la Persona Encuestada', null=False)

    def __str__(self):
        fila = 'Persona Encuestada: ' + self.nombre_completo + ' - ' + 'Correo: ' + self.correo
        return fila

class TipoEncuesta(models.Model):
    id_tipo_encuesta = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre del Tipo de Encuesta', null=False)

    def __str__(self):
        fila = 'Tipo de Encuesta: ' + self.nombre
        return fila

class Encuesta(models.Model):
    id_encuesta = models.AutoField(primary_key=True)
    nombre_encuesta = models.CharField(max_length=100, verbose_name='Nombre de la Encuesta', null=False)
    fecha = models.DateTimeField(verbose_name='Fecha de la Encuesta', null=False)
    tipo_encuesta = models.ForeignKey(TipoEncuesta, on_delete=models.CASCADE, verbose_name='Tipo de Encuesta', null=False)

    def __str__(self):
        fila = 'Encuesta: ' + self.nombre_encuesta + ' - ' + 'Fecha: ' + str(self.fecha)
        return fila

class Pregunta(models.Model):
    id_pregunta = models.AutoField(primary_key=True)
    pregunta = models.CharField(max_length=100, verbose_name='Pregunta', null=False)
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE, verbose_name='Encuesta', null=False)

    def __str__(self):
        fila = 'Pregunta: ' + self.pregunta
        return fila

class ResultadoEncuesta(models.Model):
    id_resultado_encuesta = models.AutoField(primary_key=True)
    respuesta = models.CharField(max_length=100, verbose_name='Respuesta', null=False)
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE, verbose_name='Encuesta', null=False)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, verbose_name='Pregunta', null=False)
    persona_encuestada = models.ForeignKey(PersonaEncuestada, on_delete=models.CASCADE, verbose_name='Persona Encuestada', null=False)

    def __str__(self):
        fila = 'Respuesta: ' + self.id_encuesta.nombre_encuesta + ' - ' +self.id_pregunta.pregunta + ' - ' + self.id_persona_encuestada.nombre_completo + ' - ' + self.respuesta
        return fila