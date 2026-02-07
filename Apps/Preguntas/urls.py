from django.urls import path
from Apps.Preguntas.Views.PreguntasView import CrearPreguntaView, ListarPreguntasView


urlpatterns=[
    path('crear_preguntas', CrearPreguntaView.as_view(), name='Método que crea preguntas'),
    path('listar_preguntas/<str:concepto>', ListarPreguntasView.as_view(), name='Método que lista preguntas'),
]