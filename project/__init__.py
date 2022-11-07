from flask import Flask
from project.main.routes import main
from project.admin.routes import admin
from project.config import BasecConfig, DEVCONFIG, TestingConfig
from project.models import db

app = Flask(__name__)

app.register_blueprint(main, url_prefix='/')
app.register_blueprint(admin, url_prefix='/admin')

app.config.from_object(DEVCONFIG)
with app.app_context():
    db.init_app()


