from flask import Flask , render_template, url_for

app = Flask(__name__)

@app.route("/registrar")
def registrar():
    return render_template("register.html")

@app.route("/recuperar_contraseña")
def recuperarContraseña():
    return render_template("forgot-password.html")


@app.route("/ingresar")
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app.run()
