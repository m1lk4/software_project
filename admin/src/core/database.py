from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app):
    db.init_app(app)
    config_db(app)

    return db


def config_db(app):
    @app.teardown_request
    def close_session(exception=None):
        db.session.remove()


def reset_db():
    print("Eliminando base de datos...")
    db.drop_all()
    print("Creando base de datos...")
    db.create_all()
    print("Done!")
