from django.urls import path
from . views import TipoEncuestaView, EncuestaView

urlpatterns = [
    # urls Tipo Encuesta
    path('tipo_encuestas/', TipoEncuestaView.as_view(), name='listar_tipo_encuestas'),
    path('tipo_encuestas/<int:id>/', TipoEncuestaView.as_view(), name='detalle_tipo_encuesta'),
    # urls Encuesta
    path('encuestas/', EncuestaView.as_view(), name='listar_encuestas'),
    path('encuestas/<int:id>/', EncuestaView.as_view(), name='detalle_encuesta'),
]

