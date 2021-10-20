import main

db = main.db
### ESTOS SON MODELOS QUE REPRESENTAN LAS TABLAS EN MYSQL
class Usuario(db.Model):
    nombre = db.Column("nombre", db.String(50))
    correo = db.Column("correo", db.String(50), primary_key = True)
    contraseña = db.Column("contraseña", db.String(80))
    __table_args__ = {'extend_existing': True}



    def __init__(self, nombre,correo,contraseña) -> None:
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña

    def __repr__(self) -> str: 
        return f"{self.correo}"


db.create_all() #SE EJECUTA PARA CREAR LAS TABLAS SEGUN LOS MODELOS ES MEJOR CREAR LAS TABLAS DESDE ACA