from rest_framework import serializers
from Apps.Preguntas.Models.PreguntasModel import Preguntas
from Apps.Base.Parametros import MensajesEnum

class RespuestaPreguntaSerializer(serializers.Serializer):
    id_pregunta = serializers.IntegerField(label='Identificador de pregunta.',
                                            required=True,
                                            allow_blank=False,
                                            error_messages={
                                                                'required': MensajesEnum.mensajeCampoRequerido,
                                                                'null': MensajesEnum.mensajeCampoRequerido,
                                                            }
                                            )
    opcion_seleccionada = serializers.IntegerField(label='Identificador de opcion selecionada.',
                                                    required=True,
                                                    allow_blank=False,
                                                    error_messages={
                                                                        'required': MensajesEnum.mensajeCampoRequerido,
                                                                        'null': MensajesEnum.mensajeCampoRequerido,
                                                                    }
                                                    )

    def validate_opcion_seleccionada(self, value):
        if value < 0:
            raise serializers.ValidationError(MensajesEnum.mensajeOpcionNoValida)
        return value

    class Meta:
        model = Preguntas
        fields = (
            'id_pregunta',
            'opcion_seleccionada'
            )

class ResponderTriviaSerializer(serializers.ModelSerializer):
    respuestas = RespuestaPreguntaSerializer(many=True,
                                            required=True,
                                            allow_empty=False
                                            )

    def validate(self, attrs):
        respuestas = attrs.get('respuestas')

        ids = [r['id_pregunta'] for r in respuestas]

        if len(ids) != len(set(ids)):
            raise serializers.ValidationError(MensajesEnum.mensajeNoRepetirPreguntas)

        return attrs

    class Meta:
        model = Preguntas
        fields = (
            'respuestas'
            )