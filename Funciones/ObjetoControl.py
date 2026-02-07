def objeto_control(codigo_estado, estado, mensaje=None, datos=None, total_registros=None):
    control={}
    control['codigo_estado'] = codigo_estado
    control['estado'] = estado
    control['mensaje'] = mensaje
    control['datos']= datos
    control['total_registros'] = total_registros
    return control