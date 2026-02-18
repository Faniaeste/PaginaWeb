from flask import Flask
from clave import *

app = Flask(__name__)

app.config.from_object("clave")


from appWeb.routes import *
