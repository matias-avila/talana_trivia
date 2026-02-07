from django.core.exceptions import ValidationError
from datetime import datetime, timedelta
from rest_framework import serializers
from Apps.Usuario.Models.UsuarioModel import Usuario
from Apps.Base.Parametros import MensajesEnum


class CrearUsuarioSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(max_length=50,
                                    label='Nombre de usuario.',
                                    required=True,
                                    allow_blank=False,
                                    error_messages={
                                                        'required': MensajesEnum.mensajeCampoRequerido,
                                                        'null': MensajesEnum.mensajeCampoRequerido,
                                                    }
                                                    )

    apellidos = serializers.CharField(max_length=50,
                                    label='Apellidos de usuario.',
                                    required=True,
                                    allow_blank=False,
                                    error_messages={
                                                        'required': MensajesEnum.mensajeCampoRequerido,
                                                        'null': MensajesEnum.mensajeCampoRequerido,
                                                    }
                                                    )

    email = serializers.CharField(max_length=100,
                                    label='Email de usuario.',
                                    required=True,
                                    allow_blank=False,
                                    error_messages={
                                                        'required': MensajesEnum.mensajeCampoRequerido,
                                                        'null': MensajesEnum.mensajeCampoRequerido,
                                                    }
                                                    )

    login = serializers.CharField(max_length=50,
                                    label='Nombre de usuario para inicio de sesión.',
                                    required=True,
                                    allow_blank=False,
                                    error_messages={
                                                        'required': MensajesEnum.mensajeCampoRequerido,
                                                        'null': MensajesEnum.mensajeCampoRequerido,
                                                    }
                                                    )

    administrador = serializers.BooleanField(label='Indica si usuario es administrador.',
                                            required=True,
                                            allow_blank=False,
                                            error_messages={
                                                                'required': MensajesEnum.mensajeCampoRequerido,
                                                                'null': MensajesEnum.mensajeCampoRequerido,
                                                            }
                                                            )

    class Meta:
        model = Usuario
        fields = (
            'nombre',
            'apellidos',
            'email',
            'login',
            'administrador'
            )

class ListaUsuariosSerializer(serializers.Serializer):
    def to_representation(self, instance):
        return {
            'id': instance.get('id'),
            'nombre': instance.get('nombre') + " " + instance.get('apellidos'),
            'email': instance.get('email')
            }
