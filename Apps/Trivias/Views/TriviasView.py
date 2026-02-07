

from rest_framework import status, generics
from Apps.Base.Parametros import MensajesEnum
from django.db import transaction
from Funciones.ObjetoControl import objeto_control
from rest_framework.response import Response
from Funciones.ValidacionJWT import valida_jwt
from Apps.Trivias.Models.TriviasModel import Trivias
from Apps.UsuarioTrivia.Models.UsuarioTriviaModel import UsuarioTrivia
from Apps.Trivias.Serializers.TriviasSerializer import CrearTriviasSerializer, ListaTriviasSerializer, ListaTriviasUsuarioSerializer, ListaRankingSerializer

class CrearTriviasView(generics.RetrieveAPIView):
    """
    Método que crea trivias.
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
        serializer = CrearTriviasSerializer(data=request.data)
        if serializer.is_valid():
            try:
                with transaction.atomic():
                    pregunta_creada = Trivias.create(self, id_usuario, request.data)
                return Response(objeto_control(status.HTTP_201_CREATED, 1, MensajesEnum.mensajeOk, pregunta_creada.id))
            except Exception as e:
                return Response(objeto_control(status.HTTP_500_INTERNAL_SERVER_ERROR, 0, MensajesEnum.mensajeErrorCreacion, {'Error':str(e)}))
        else:
            return Response(objeto_control(status.HTTP_400_BAD_REQUEST, 0, MensajesEnum.mensajeErrorValidacionDatos, serializer.errors))

class ListarTriviasView(generics.RetrieveAPIView):
    """
    Método que lista trivias.
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
        lista_trivias = list(Trivias.objects.por_concepto(concepto))
        if len(lista_trivias) == 0:
            return Response(objeto_control(status.HTTP_200_OK, 0, MensajesEnum.mensajeBusquedaSinResultados))
        lista = ListaTriviasSerializer(lista_trivias, many = True).data
        lista = sorted(lista, key=lambda x: x['dificultad'])
        return Response(objeto_control(status.HTTP_200_OK, 1, MensajesEnum.mensajeOk, lista, len(lista)))

class ListarTriviasUsuarioView(generics.RetrieveAPIView):
    """
    Método que lista las trivias asociadas al usuario en sesión.
    Returns:
        objeto_control: Objeto Control
    Remarks: Matias Avila 05-02-2025
    """

    def get(self, request):
        jwt = valida_jwt(self, autorizacion=request.headers.get('authorization'))
        if not jwt['valido']:
            return Response(objeto_control(status.HTTP_401_UNAUTHORIZED, 0, str(jwt['mensaje'])))
        id_usuario = jwt['payload'].get('id_usuario')
        lista_trivias = list(UsuarioTrivia.objects.por_usuario(id_usuario))
        if len(lista_trivias) == 0:
            return Response(objeto_control(status.HTTP_200_OK, 0, MensajesEnum.mensajeBusquedaSinResultados))
        lista = ListaTriviasUsuarioSerializer(lista_trivias, many = True).data
        return Response(objeto_control(status.HTTP_200_OK, 1, MensajesEnum.mensajeOk, lista, len(lista)))

class RankingTriviaView(generics.RetrieveAPIView):
    """
    Método que entrega ranking de usuario de una trivia.
    Returns:
        objeto_control: Objeto Control
    Remarks: Matias Avila 05-02-2025
    """

    def get(self, request, id_trivia):
        jwt = valida_jwt(self, autorizacion=request.headers.get('authorization'))
        if not jwt['valido']:
            return Response(objeto_control(status.HTTP_401_UNAUTHORIZED, 0, str(jwt['mensaje'])))
        es_administrador = jwt['payload'].get('es_administrador')
        if not es_administrador:
            return Response(objeto_control(status.HTTP_403_FORBIDDEN, 1, MensajesEnum.mensajeSinPrivilegios))
        lista_usuarios = list(UsuarioTrivia.objects.ranking(id_trivia))
        if len(lista_usuarios) == 0:
            return Response(objeto_control(status.HTTP_200_OK, 0, MensajesEnum.mensajeBusquedaSinResultados))

        for index, usuario in enumerate(lista_usuarios, start=1):
            usuario["posicion"] = index
        lista = ListaRankingSerializer(lista_usuarios, many = True).data
        return Response(objeto_control(status.HTTP_200_OK, 1, MensajesEnum.mensajeOk, lista, len(lista)))
