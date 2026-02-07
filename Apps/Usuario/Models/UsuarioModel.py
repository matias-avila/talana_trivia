from django.db import models
from django.db.models.deletion import PROTECT
from Apps.Base.BaseModel import ModeloBase
from Apps.Usuario.Querysets.UsuarioQueryset import UsuarioQueryset
from django.utils import timezone
from Funciones.Encriptacion import crear_password
from django.contrib.auth.hashers import make_password

class Usuario(ModeloBase):
    #region Atributos
    id = models.AutoField(primary_key= True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    login = models.CharField( max_length=50)
    password = models.CharField(max_length=150)
    es_administrador = models.BooleanField()

    objects = UsuarioQueryset.as_manager()
    #endregion

    #region Meta
    class Meta:
        db_table = 'Usuario'
        managed = False
    #endregion

    def create(self, id_usuario, data):
        password = crear_password()
        registro = {}
        registro['nombre'] = data.get('nombre')
        registro['apellidos'] = data.get('apellidos')
        registro['email'] = data.get('email')
        registro['login'] = data.get('login')
        registro['password'] = make_password(password)
        registro['es_administrador'] = data.get('administrador')
        registro['activo'] = True
        registro['id_usuario_creacion'] = id_usuario
        registro['fecha_creacion'] = timezone.now()

        return Usuario.objects.create(**registro)