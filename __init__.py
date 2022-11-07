from flask import Flask
from project import config

app = Flask(__name__)
app.config.from_object(config.DEVCONFIG)
