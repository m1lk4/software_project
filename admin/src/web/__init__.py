import logging

from flask import Flask
from flask import render_template
from flask_session import Session

from src.core import database
from src.core import seeds
from src.web.config import config
from src.web.helpers import handlers
from src.web.helpers import auth
from src.web.controllers.issues import issue_blueprint
from src.web.controllers.users import users_blueprint
from src.web.controllers.auth import auth_blueprint
from src.web.controllers.api.issues import issue_api_blueprint

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)


def create_app(env="development", static_folder="static"):
    """Método de inicialización de la aplicación"""

    app = Flask(__name__, static_folder=static_folder)

    # Load config
    app.config.from_object(config[env])

    # Init database
    database.init_app(app)

    # Config session backend
    Session(app)

    @app.get("/")
    def home():
        return render_template("home.html")

    @app.get("/catalogo")
    def catalogo():
        return render_template("catalogo.html")

    # Controllers
    app.register_blueprint(issue_blueprint)
    app.register_blueprint(users_blueprint)
    app.register_blueprint(auth_blueprint)
    # API
    app.register_blueprint(issue_api_blueprint)

    app.register_error_handler(401, handlers.unauthorized)
    app.register_error_handler(404, handlers.not_found_error)
    app.register_error_handler(500, handlers.internal_server_error)

    app.jinja_env.globals.update(is_authenticated=auth.is_authenticated)

    @app.cli.command(name="resetdb")
    def reset_db():
        database.reset_db()

    @app.cli.command(name="seeds")
    def seedsdb():
        seeds.run()

    return app
