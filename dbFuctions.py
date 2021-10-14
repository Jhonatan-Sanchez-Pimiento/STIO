import servidorSTIO

db = servidorSTIO.db
Usuario = servidorSTIO.Usuario



def nuevo_usuario(nombre, correo, contraseña) -> bool:
    """
    Los 3 parametros son Strings
    Agregar un nuevo usuario y regresa True si pudo agregar a la base de datos

    """
    usuarioTemp = Usuario(nombre.lower(), correo.lower(), contraseña)
    if consultar_usuario(correo) == None: 
        print("Guardado con exito")
        db.session.add(usuarioTemp)
        db.session.commit()
        return True
    else:
        return False
    

def consultar_usuario(correo):
    resultado = Usuario.query.filter(Usuario.correo == correo.lower()).first()
    return resultado

def validacion_login(correo, contraseña):
    usuarioTemp = consultar_usuario(correo.lower())
    if usuarioTemp and usuarioTemp.contraseña == contraseña:
        return True
    else:
        return False

