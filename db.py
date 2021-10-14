from flask_sqlalchemy import SQLAlchemy # tambien hay que descargar mysqlclient
from app import app as app #importar la aplicacion app de flask

usuarioBd = "root"
contraseñaBd = "toor" #cambiar a tu contraseña de mysql
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:toor@localhost/stio"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Usuario(db.Model):
    nombre = db.Column("nombre", db.String(30), )
    correo = db.Column("correo", db.String(20), primary_key = True)
    contraseña = db.Column("contraseña", db.String(80))

    def __init__(self, nombre,correo,contraseña) -> None:
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña

#db.create_all() #se ejecuta una vez para crear las tablas





