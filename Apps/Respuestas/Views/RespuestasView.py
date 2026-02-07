


from rest_framework import status, generics
from Apps.Base.Parametros import MensajesEnum
from django.db import transaction
from Funciones.ObjetoControl import objeto_control
from rest_framework.response import Response
from Funciones.ValidacionJWT import valida_jwt
from Apps.Trivias.Models.TriviasModel import Trivias
from Apps.TriviaPregunta.Models.TriviaPreguntaModel import TriviaPregunta
from Apps.UsuarioTrivia.Models.UsuarioTriviaModel import UsuarioTrivia
from Apps.Respuestas.Models.RespuestasModel import Respuestas
from Apps.Preguntas.Models.PreguntasModel import Preguntas
from Apps.Respuestas.Serializers.RespuestasSerializer import ResponderTriviaSerializer

class ResponderTriviaView(generics.RetrieveAPIView):
    """
    Método que guarda respuestas de usuario a una trivia.
    Returns:
        objeto_control: Objeto Control
    Remarks: Matias Avila 05-02-2025
    """

    def post(self, request, id_trivia):
        jwt = valida_jwt(self, autorizacion=request.headers.get('authorization'))
        if not jwt['valido']:
            return Response(objeto_control(status.HTTP_401_UNAUTHORIZED, 0, str(jwt['mensaje'])))
        id_usuario = jwt['payload'].get('id_usuario')
        serializer = ResponderTriviaSerializer(data=request.data)
        if serializer.is_valid():
            try:
                respuestas_data = serializer.validated_data['respuestas']

                usuario_trivia = UsuarioTrivia.objects.por_usuario_trivia(id_usuario, id_trivia)
                if usuario_trivia.finalizada:
                    return Response(objeto_control(status.HTTP_400_BAD_REQUEST, 0, MensajesEnum.mensajeTriviaFinalizada))

                trivia_preguntas = TriviaPregunta.objects.por_usuario_trivia(id_usuario, id_trivia)
                trivia_preguntas = set(trivia_preguntas)
                puntaje_trivia = 0

                with transaction.atomic():

                    for respuesta in respuestas_data:
                        id_pregunta = respuesta["id_pregunta"]
                        opcion_seleccionada = respuesta["opcion_seleccionada"]

                        if id_pregunta not in trivia_preguntas:
                            return Response(objeto_control(status.HTTP_400_BAD_REQUEST, 0, MensajesEnum.mensajePreguntaInvalida))

                        pregunta = Preguntas.objects.por_id(id_pregunta)
                        es_correcta = opcion_seleccionada == pregunta.opcion_correcta
                        puntaje = 0
                        if es_correcta:
                            puntaje = pregunta.dificultad
                            puntaje_trivia += puntaje
                        Respuestas.objects.create(usuario_trivia, pregunta, opcion_seleccionada, es_correcta, puntaje, id_usuario)

                    usuario_trivia.puntaje = puntaje_trivia
                    usuario_trivia.finalizada = True
                    usuario_trivia.save()
                return Response(objeto_control(status.HTTP_201_CREATED, 1, MensajesEnum.mensajeOk))
            except Exception as e:
                return Response(objeto_control(status.HTTP_500_INTERNAL_SERVER_ERROR, 0, MensajesEnum.mensajeErrorCreacion, {'Error':str(e)}))
        else:
            return Response(objeto_control(status.HTTP_400_BAD_REQUEST, 0, MensajesEnum.mensajeErrorValidacionDatos, serializer.errors))

