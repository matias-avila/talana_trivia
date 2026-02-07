from rest_framework import serializers
from Apps.Preguntas.Models.PreguntasModel import Preguntas
from Apps.Base.Parametros import MensajesEnum


class CrearPreguntasSerializer(serializers.ModelSerializer):
    texto = serializers.CharField(max_length=50,
                                    label='Texto de pregunta.',
                                    required=True,
                                    allow_blank=False,
                                    error_messages={
                                                        'required': MensajesEnum.mensajeCampoRequerido,
                                                        'null': MensajesEnum.mensajeCampoRequerido,
                                                    }
                                                    )

    dificultad = serializers.ChoiceField(label='Dificultad de pregunta.',
                                        required=True,
                                        allow_blank=False,
                                        error_messages={
                                                            'required': MensajesEnum.mensajeCampoRequerido,
                                                            'null': MensajesEnum.mensajeCampoRequerido,
                                                        }
                                                        )

    opciones = serializers.JSONField(label='Opciones de preguntas.',
                                    required=True,
                                    error_messages={
                                                        'required': MensajesEnum.mensajeCampoRequerido,
                                                        'null': MensajesEnum.mensajeCampoRequerido,
                                                    }
                                                    )

    opcion_correcta = serializers.IntegerField(label='Opción correcta de pregunta.',
                                    required=True,
                                    allow_blank=False,
                                    error_messages={
                                                        'required': MensajesEnum.mensajeCampoRequerido,
                                                        'null': MensajesEnum.mensajeCampoRequerido,
                                                    }
                                                    )

    def validate_opciones(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Las opciones deben ser una lista.")

        if len(value) < 2:
            raise serializers.ValidationError("Debe haber al menos 2 opciones.")

        for opcion in value:
            if not isinstance(opcion, str) or not opcion.strip():
                raise serializers.ValidationError("Cada opción debe ser un texto válido.")

        return value

    def validate(self, attrs):
        opciones = attrs.get("opciones", [])
        opcion_correcta = attrs.get("opcion_correcta")

        if opcion_correcta < 0 or opcion_correcta >= len(opciones):
            raise serializers.ValidationError({
                "opcion_correcta": "La opción correcta no corresponde a ninguna opción."
            })

        return attrs

    class Meta:
        model = Preguntas
        fields = (
            'texto',
            'dificultad',
            'opciones',
            'opcion_correcta'
            )

class ListaPreguntasSerializer(serializers.Serializer):
    def to_representation(self, instance):
        return {
            'id': instance.get('id'),
            'texto': instance.get('texto'),
            'dificultad': instance.get('dificultad'),
            'opciones': instance.get('opciones')
            }
