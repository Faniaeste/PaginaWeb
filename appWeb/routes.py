from appWeb import app
from flask import render_template
from appWeb.forms import TribuForm




@app.route("/",methods=['GET','POST'])
def base():
    form = TribuForm()
    if form.validate_on_submit():
        return "Ya perteneces a nuestra Tribu!"
    else:
        return render_template("index.html", form=form)

@app.route("/ejercicio")
def ejercicio():
    return render_template("ejercicio.html")

@app.route("/nutricion")
def nutricion():
    return render_template("nutricion.html")

@app.route("/data")
def data():
    return render_template("data.html")
