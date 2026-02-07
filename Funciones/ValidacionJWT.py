import jwt
from django.conf import settings

def valida_jwt(self, autorizacion):
    respuesta = {}
    if autorizacion is None:
        respuesta['valido']= False
        respuesta['mensaje'] = 'Bearer token no se encuentra disponible.'
        return respuesta

    if autorizacion == "":
        respuesta['valido']= False
        respuesta['mensaje'] = 'Bearer token no se encuentra disponible.'
        return respuesta

    if len(autorizacion) == 1:
        respuesta['valido']= False
        respuesta['mensaje'] = 'Bearer token inválido.'
        return respuesta

    if autorizacion.split()[0] != "Bearer":
        respuesta['valido']= False
        respuesta['mensaje'] = 'Debe indicar Bearer.'
        return respuesta

    if autorizacion.split(' ')[1] == "null":
        respuesta['valido']= False
        respuesta['mensaje'] = 'Token inválido.'
        return respuesta
    else:
        autorizacion = autorizacion.split(' ')[1]

    if autorizacion:
        try:
            payload = jwt.decode(autorizacion, settings.SECRET_KEY_JWT, algorithms=['HS256'], require=["exp"])
            respuesta['valido']= True
            respuesta['mensaje'] = 'Válido.'
            respuesta['payload'] = payload
            return respuesta
        except jwt.ExpiredSignatureError:
            respuesta['valido']= False
            respuesta['mensaje'] = 'Token expirado.'
            return respuesta

        except (jwt.DecodeError, jwt.InvalidTokenError):
            respuesta['valido']= False
            respuesta['mensaje'] = 'Autorización errónea, intente con un nuevo token.'
            return respuesta

    else:
        respuesta['valido']= False
        respuesta['mensaje'] = 'No se detecta autorización, por favor enviar token.'
        return respuesta