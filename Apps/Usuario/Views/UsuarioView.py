
from rest_framework import status, generics
from Apps.Base.Parametros import MensajesEnum
from django.db import transaction
from Funciones.ObjetoControl import objeto_control
from rest_framework.response import Response
from Funciones.ValidacionJWT import valida_jwt
from Apps.Usuario.Models.UsuarioModel import Usuario
from Apps.Usuario.Serializers.UsuarioSerializer import CrearUsuarioSerializer, ListaUsuariosSerializer

class CrearUsuarioView(generics.RetrieveAPIView):
    """
    Método que crea usuarios.
    Returns:
        objeto_control: Objeto Control
    Remarks: Matias Avila 05-02-2025
    """

    def post(self, request):
        jwt = valida_jwt(self, autorizacion=request.headers.get('authorization'))
        if not jwt['valido']:
            return Response(objeto_control(status.HTTP_401_UNAUTHORIZED, 0, str(jwt['mensaje'])))
        id_usuario = jwt['payload'].get('id_usuario')
        es_administrador = jwt['payload'].get('es_administrador')
        if not es_administrador:
            return Response(objeto_control(status.HTTP_403_FORBIDDEN, 1, MensajesEnum.mensajeSinPrivilegios))
        serializer = CrearUsuarioSerializer(data=request.data)
        if serializer.is_valid():
            try:
                with transaction.atomic():
                    usuario_creado = Usuario.create(self, id_usuario, request.data)
                return Response(objeto_control(status.HTTP_201_CREATED, 1, MensajesEnum.mensajeOk, usuario_creado.id))
            except Exception as e:
                return Response(objeto_control(status.HTTP_500_INTERNAL_SERVER_ERROR, 0, MensajesEnum.mensajeErrorCreacion, {'Error':str(e)}))
        else:
            return Response(objeto_control(status.HTTP_400_BAD_REQUEST, 0, MensajesEnum.mensajeErrorValidacionDatos, serializer.errors))

class ListarUsuariosView(generics.RetrieveAPIView):
    """
    Método que lista usuarios.
    Returns:
        objeto_control: Objeto Control
    Remarks: Matias Avila 05-02-2025
    """

    def get(self, request, concepto):
        jwt = valida_jwt(self, autorizacion=request.headers.get('authorization'))
        if not jwt['valido']:
            return Response(objeto_control(status.HTTP_401_UNAUTHORIZED, 0, str(jwt['mensaje'])))
        es_administrador = jwt['payload'].get('es_administrador')
        if not es_administrador:
            return Response(objeto_control(status.HTTP_403_FORBIDDEN, 1, MensajesEnum.mensajeSinPrivilegios))
        lista_usuarios = list(Usuario.objects.por_concepto(concepto))
        if len(lista_usuarios) == 0:
            return Response(objeto_control(status.HTTP_200_OK, 0, MensajesEnum.mensajeBusquedaSinResultados))
        lista = ListaUsuariosSerializer(lista_usuarios, many = True).data
        lista = sorted(lista, key=lambda x: x['nombre'])
        return Response(objeto_control(status.HTTP_200_OK, 1, MensajesEnum.mensajeOk, lista, len(lista)))