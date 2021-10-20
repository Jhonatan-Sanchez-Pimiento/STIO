from datetime import timedelta


codigo_encriptacion = "ASDJSADKJ23432424DASKD" # con esto codifica la sesion y la cookie
duracion_max_sesion = timedelta(days = 3)
usuarioBd = "root" # usuario en la base de datos por defecto es root
contraseñaBd = "toor" #cambiar a tu contraseña de mysql
uri_db = f"mysql://{usuarioBd}:{contraseñaBd}@localhost/stio" # Aqui se dice utilizar la base de datos stio que esta en mysql y se le da las credencias
uri_db = f"sqlite:///tmp/test.db"
permitir_notificaciones_sql = False # esto es para que no moleste la base de datos al cambiar