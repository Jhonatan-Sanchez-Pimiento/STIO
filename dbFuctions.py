from main import db
from model_db import Usuario

import smtplib, ssl
from email.message import EmailMessage




def nuevo_usuario(nombre, correo, contraseña) -> bool:
    """
    Los 3 parametros son Strings
    Agregar un nuevo usuario y regresa True si pudo agregar a la base de datos

    """
    usuarioTemp = Usuario(nombre.lower(), correo.lower(), contraseña)
    if consultar_usuario(correo) == None: 
        db.session.add(usuarioTemp)
        db.session.commit()
        enviar_correo_registro(usuarioTemp)
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

def recuperar_contraseña(correo):
    usuarioTemp = consultar_usuario(correo.lower())
    if usuarioTemp:
        enviar_correo_recuperar_contraseña(usuarioTemp)
        return True
    else:
        return False


def enviar_correo_registro(usuario):
    """Enviar mensaje al usuario que acaban de registrar"""
    mensaje = EmailMessage()
    mensaje['Subject'] = "Registro en el sistema STIO"
    mensaje.set_content(f"Hola {usuario.nombre} te acaban de registrar en el sistema STIO (supervicion tecnica de obra).\n\n Tus credenciales para el login son:\ncorreo = {usuario.correo}\nContraseña = {usuario.contraseña}\n\nAhora si puedes entrar al sistema STIO sin problemas.")

    enviar_correo(usuario.correo, mensaje)

def enviar_correo_recuperar_contraseña(usuario):
    """enviar correo de recuperar contraseña al usuario que le pasen"""
    mensaje = EmailMessage()
    mensaje['Subject'] = "Recuperacion de contraseña en STIO"
    mensaje.set_content(f"Hola {usuario.nombre.title()} parece que olvidaste la contraseña, no te preocupes.\n\nTu contraseña es {usuario.contraseña}\n\nAhora si puedes entrar al sistema STIO sin problemas.")

    enviar_correo(usuario.correo, mensaje)



def enviar_correo(correo ,mensaje):
    """Enviar correo al correo que le pasen por parametro y el mensaje de tipo EmailMessage()"""
    #FIXME: agregar correo y contraseña del correo stio
    correo_stio = "" 
    contraseña = ""
    mensaje['From'] = correo_stio
    mensaje['To'] = correo

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port= 465, context=context) as server:
        server.login(correo_stio, contraseña)
        server.send_message(mensaje)
    
    
    print(f"email enviado a {correo}")