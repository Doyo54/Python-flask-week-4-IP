from flask import Flask
from config import DevConfig
from flask_bootstrap import Bootstrap
# Initializing application

bootstrap = Bootstrap()

app = Flask(__name__)

bootstrap.init_app(app)


app.config.from_object(DevConfig)
app.config['SECRET_KEY'] = '1234'

from .main import main as main_blueprint
app.register_blueprint(main_blueprint)