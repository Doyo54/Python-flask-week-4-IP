from flask import Flask
from config import DevConfig,config_options,Config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

# Initializing application
bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
# Initializing application
    app = Flask(__name__)


    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    app.config.from_object(config_options[config_name])
    app.config.from_object(DevConfig)
    app.config.from_object(Config)
    
    app.config['SECRET_KEY'] = '1234'


    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    return app