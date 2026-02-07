from django.urls import path
from Apps.Trivias.Views.TriviasView import CrearTriviasView, ListarTriviasView, ListarTriviasUsuarioView, RankingTriviaView


urlpatterns=[
    path('crear_trivias', CrearTriviasView.as_view(), name='Método que crea trivias'),
    path('listar_trivias/<str:concepto>', ListarTriviasView.as_view(), name='Método que lista trivias'),
    path('listar_trivias_usuario', ListarTriviasUsuarioView.as_view(), name='Método que lista las trivias asociadas al usuario en sesión'),
    path('ranking_trivia/<int:id_trivia>', RankingTriviaView.as_view(), name='Método que entrega ranking de usuario de una trivia'),
]