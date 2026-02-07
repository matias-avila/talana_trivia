import bcrypt
import secrets
from django.utils.crypto import get_random_string


def encripta_password(self, password):
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(prefix=b'2a')).decode('utf-8')
    return password_hash

def desencripta_password(self, password, password_hash):
    respuesta = {}
    if not bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8')):
        respuesta['valido'] = False
        return respuesta
    else:
        respuesta['valido'] = True
        return respuesta

def crear_password(self, length=12):
    return get_random_string(length)