from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
from flask import Flask, render_template,url_for , flash,  request, session, redirect
import dbFuctions


app = Flask(__name__) # creacion de la app
app.secret_key = "ASDJSADKJDASKD" # con esto codifica la sesion y la cookie
app.permanent_session_lifetime = timedelta(days = 3)
usuarioBd = "root" # usuario en la base de datos por defecto es root
contraseñaBd = "toor" #cambiar a tu contraseña de mysql
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql://{usuarioBd}:{contraseñaBd}@localhost/stio" # Aqui se dice utilizar la base de datos stio que esta en mysql y se le da las credencias
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # esto es para que no moleste la base de datos al cambiar

db = SQLAlchemy(app) # creamos la conexion


### ESTOS SON MODELOS QUE REPRESENTAN LAS TABLAS EN MYSQL
class Usuario(db.Model):
    nombre = db.Column("nombre", db.String(50), )
    correo = db.Column("correo", db.String(50), primary_key = True)
    contraseña = db.Column("contraseña", db.String(80))

    def __init__(self, nombre,correo,contraseña) -> None:
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña

    def __repr__(self) -> str: 
        return f"{self.correo}"

#db.create_all() #SE EJECUTA PARA CREAR LAS TABLAS SEGUN LOS MODELOS ES MEJOR CREAR LAS TABLAS DESDE ACA






@app.route("/registrar")
def registrar():
    if "correo" in session:
        print(session["correo"])
        return render_template("register.html")
    
    else:
        return redirect(url_for("login"))

@app.route("/recuperar_contraseña")
def recuperarContraseña():
    return render_template("forgot-password.html")


@app.route("/ingresar", methods=["POST", "GET"])
def login():
    if "correo" in session: # verificar si se encuntra logueado
        flash("Ya te encuentras Logueado")
        return redirect(url_for("registrar"))
    
    
    if request.method == "POST": #verifica si es post y si el correo no esta vacio
        if request.form["email"]: # si el correo no esta vacio
            correo= request.form["email"]  # coger el correo del formulario
            contraseña = request.form["password"] # coger la contraseña del formulario
            #este try es para intentar coger el valor del checkbox
            try: 
                recordar = request.form["recuerdame"] 
                
            except:
                recordar = False # en caso de que no marque la casilla
                
            if dbFuctions.validacion_login(correo, contraseña): # validar en la base datos correo y contraseña
                session["correo"] = correo # agregar una session que se almacena como una cookie en el navegador del cliente con la informacion correo
                session.permanent = False # esto hace que se cierre la sesion cuando se cierre el navegador
                if recordar: # en caso de que recuerdame estuviese seleccionado
                    session.permanent = True # la session durara 3 dias
                flash("has iniciado sesion correctamente")
                return redirect(url_for("registrar")) 
            else:
                flash("Correo o contraseña erronea")  # mensajes de advertencias para las validaciones
        else:
            flash("No puedes dejar los campos vacio")

    return render_template("login.html")




@app.route("/salir")
def logout():
    session.pop("correo")
    flash("Cesion cerrada correctamente")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)

