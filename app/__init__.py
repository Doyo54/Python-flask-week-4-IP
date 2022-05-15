from flask import Flask
from config import DevConfig
from flask_bootstrap import Bootstrap
# Initializing application

bootstrap = Bootstrap()

app = Flask(__name__,instance_relative_config = True)

bootstrap.init_app(app)


app.config.from_object(DevConfig)

from .main import main as main_blueprint
app.register_blueprint(main_blueprint)