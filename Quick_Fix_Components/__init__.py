# Quick_Fix_Website/__init__.py
from flask import Flask

app = Flask(__name__)

from Quick_Fix_Components.core.views import core
app.register_blueprint(core)