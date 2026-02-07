from django.urls import path
from Apps.Respuestas.Views.RespuestasView import ResponderTriviaView

urlpatterns=[
    path('responder_trivia/<int:id_trivia>', ResponderTriviaView.as_view(), name='Método que guarda respuestas de usuario a una trivia'),
]