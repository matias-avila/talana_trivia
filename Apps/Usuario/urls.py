from django.urls import path
from Apps.Usuario.Views.UsuarioView import CrearUsuarioView, ListarUsuariosView


urlpatterns=[
    path('crear_usuario', CrearUsuarioView.as_view(), name='Método que crea usuarios'),
    path('listar_usuario/<str:concepto>', ListarUsuariosView.as_view(), name='Método que lista usuarios'),
]