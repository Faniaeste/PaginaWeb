from flask import Flask

app = Flask(__name__)


from appWeb.routes import *
