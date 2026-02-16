from appWeb import app
from flask import render_template




@app.route("/")
def base():
    return render_template("index.html")

@app.route("/ejercicio")
def ejercicio():
    return render_template("ejercicio.html")

@app.route("/nutricion")
def nutricion():
    return render_template("nutricion.html")

@app.route("/data")
def data():
    return render_template("data.html")
