from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template,url_for , flash,  request, session, redirect

import app_config


app = Flask(__name__) # creacion de la app
app.secret_key = app_config.codigo_encriptacion # con esto codifica la sesion y la cookie
app.permanent_session_lifetime = app_config.duracion_max_sesion
app.config["SQLALCHEMY_DATABASE_URI"] = app_config.uri_db 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = app_config.permitir_notificaciones_sql

db = SQLAlchemy(app) # creamos la conexion con la base de datos

import dbFuctions



@app.route("/")
def home():
    if "correo" in session:
        # print(session["correo"])
        return redirect(url_for(("index")))

    else:
        return redirect(url_for("login"))




@app.route("/registrar", methods=["POST", "GET"])
def registrar():
    if (request.method == "POST") and "correo" in session:
        nombre = request.form['primer_nombre']
        apellido = request.form['apellidos']
        nombre_completo =  f"{nombre} {apellido}"
        correo = request.form["email"]
        contraseña = request.form["password"]
        contraseña_repetida = request.form["password_repeat"]
        print(nombre_completo)
        
        if (contraseña == contraseña_repetida):
            resultado_crear_usuario = dbFuctions.nuevo_usuario(nombre_completo, correo, contraseña)
            if resultado_crear_usuario:
                flash("Usuario registrado con exito")
                return redirect(url_for("registrar"))
            
            else:
                flash("Parece que ya existe el correo registrado")
                return redirect(url_for("registrar"))
      
        else:
            flash("La contraseña no son iguales o revisa los campos")
            return redirect(url_for("registrar"))
            
    
    if "correo" in session:
        return render_template("register.html")

    
    
    else:
        flash("no has iniciado sesion")
        return redirect(url_for("login"))


@app.route("/recuperar_contraseña", methods=["POST", "GET"])
def recuperar_contraseña():
    if request.method == "POST":
        correo= request.form["correo"]
        resultado_recuperar_contraseña = dbFuctions.recuperar_contraseña(correo)
        
        if resultado_recuperar_contraseña:
            flash("Contraseña enviada al correo por favor revise")
            return redirect(url_for("login"))
        else:
            flash("parece que no existe ese correo registrado")
            return redirect(url_for("recuperar_contraseña"))


    return render_template("forgot-password.html")


@app.route("/ingresar", methods=["POST", "GET"])
def login():
    if "correo" in session: # verificar si se encuntra logueado
        return redirect(url_for("index"))
    

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
                # return redirect(url_for("home"))
                return redirect(url_for("index"))
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


@app.route("/index")
def index():
    if "correo" in session:
        correo = session["correo"]
        usuario = dbFuctions.consultar_usuario(correo)
        return(render_template("index.html", nombre=usuario.nombre.title())) # pasar el nombre comenzando con mayusculas

    else: 
        flash("No has iniciado sesion")
        return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)

