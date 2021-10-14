from datetime import timedelta
from flask import Flask, render_template, url_for, request, session

app = Flask(__name__)
app.secret_key = "ASDJSADKJDASKD"
#app.permanent_session_lifetime = timedelta(minutes= 180)


@app.route("/registrar")
def registrar():
    return render_template("register.html")

@app.route("/recuperar_contraseña")
def recuperarContraseña():
    return render_template("forgot-password.html")


@app.route("/ingresar", methods=["POST", "GET"])
def login():
    if request.method == "POST" and request.form["email"]: #verifica si es post y si el correo no esta vacio
        correo= request.form["email"]
        contraseña = request.form["password"]
        recordar = request.form["recuerdame"]
        session["nombre"] = correo
        return render_template("login.html")
    else:    
        return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
