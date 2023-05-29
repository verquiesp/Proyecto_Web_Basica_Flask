from flask import Flask, render_template
from flask_mysqldb import MySQL

app=Flask(__name__)

db=MySQL(app)

@app.route("/")
def index():
    data={
        "canal": "verquiesp",
        "lenguajes": ["PHP","Java","Python"]
    }
    return render_template("index.html", data=data)

@app.route("/paises")
def listadoPiases():
    data={
        "paises": ["España","Portugal","Francia", "Inglaterra"]
    }
    return render_template("paises.html", data=data)

@app.route("/equipos")
def listadoEquipos():
    try:
        cursor=db.connection.cursor()
        sql="SELECT nombre FROM Equipos ORDER BY nombre ASC"
        cursor.execute(sql)
        data=cursor.fetchall()
        return render_template("autores.html", data=data)
    except Exception as ex:
        return "Error"

def inicializarApp(config):
    app.config.from_object(config)
    return app