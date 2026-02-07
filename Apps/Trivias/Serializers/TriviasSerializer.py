from rest_framework import serializers
from Apps.Trivias.Models.TriviasModel import Trivias
from Apps.Base.Parametros import MensajesEnum
from Apps.Preguntas.Models.PreguntasModel import Preguntas
from Apps.Usuario.Models.UsuarioModel import Usuario


class CrearTriviasSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(max_length=100,
                                    label='Nombre de la trivia.',
                                    required=True,
                                    allow_blank=False,
                                    error_messages={
                                                        'required': MensajesEnum.mensajeCampoRequerido,
                                                        'null': MensajesEnum.mensajeCampoRequerido,
                                                    }
                                                    )

    descripcion = serializers.CharField(max_length=1000,
                                    label='Descripcion de la trivia.',
                                    required=True,
                                    allow_blank=False,
                                    error_messages={
                                                        'required': MensajesEnum.mensajeCampoRequerido,
                                                        'null': MensajesEnum.mensajeCampoRequerido,
                                                    }
                                                    )

    preguntas = serializers.ListField(label='Listado de preguntas de la trivia.',
                                        required=True,
                                        allow_blank=False,
                                        allow_empty=False,
                                        child=serializers.IntegerField(min_value=1),
                                        error_messages={
                                                            'required': MensajesEnum.mensajeCampoRequerido,
                                                            'null': MensajesEnum.mensajeCampoRequerido,
                                                        }
                                                        )

    usuarios = serializers.ListField(label='Listado de usuario asociados a la trivia.',
                                        required=True,
                                        allow_blank=False,
                                        allow_empty=False,
                                        child=serializers.IntegerField(min_value=1),
                                        error_messages={
                                                            'required': MensajesEnum.mensajeCampoRequerido,
                                                            'null': MensajesEnum.mensajeCampoRequerido,
                                                        }
                                                        )

    def validate_preguntas(self, value):
        if len(value) != len(set(value)):
            raise serializers.ValidationError(MensajesEnum.mensajeNoPermitePreguntasDuplicadas)

        if Preguntas.objects.filter(id__in=value).count() != len(value):
            raise serializers.ValidationError(MensajesEnum.mensajePreguntasNoExisten)

        return value

    def validate_usuarios(self, value):
        if len(value) != len(set(value)):
            raise serializers.ValidationError(MensajesEnum.mensajeUsuarioDuplicados)

        if Usuario.objects.filter(id__in=value).count() != len(value):
            raise serializers.ValidationError(MensajesEnum.mensajeUsuarioNoExisten)

        return value

    class Meta:
        model = Trivias
        fields = (
            'nombre',
            'descripcion',
            'preguntas',
            'usuarios'
            )

class ListaTriviasSerializer(serializers.Serializer):
    def to_representation(self, instance):
        return {
            'id': instance.get('id'),
            'nombre': instance.get('nombre'),
            'descripcion': instance.get('descripcion')
            }

class ListaTriviasUsuarioSerializer(serializers.Serializer):
    def to_representation(self, instance):
        return {
            'id': instance.get('id'),
            'nombre': instance.get('nombre'),
            'descripcion': instance.get('descripcion'),
            'cantidad_preguntas': instance.get('cantidad_preguntas')
            }

class ListaRankingSerializer(serializers.Serializer):
    posicion = serializers.IntegerField()
    id_usuario = serializers.IntegerField()
    nombre = serializers.CharField()
    apellidos = serializers.CharField()
    puntaje = serializers.IntegerField()
