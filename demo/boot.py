from flask import Flask

from . import loader

app = Flask(__name__)
app.config.from_object('demo.config')

loader.load(app)
