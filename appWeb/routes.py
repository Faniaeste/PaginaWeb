from appWeb import app
from flask import render_template




@app.route("/")
def base():
    return render_template("base.html")

@app.route("/ejercicio")
def ejercicio():
    return render_template("ejercicio.html")

@app.route("/nutricion")
def nutricion():
    return render_template("nutricion.html")
