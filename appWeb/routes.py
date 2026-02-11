from appWeb import app
from flask import render_template


@app.route("/")
def index():
    return "Esta es tu página web"
