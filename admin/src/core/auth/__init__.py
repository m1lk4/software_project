from src.core.database import db
from src.core.auth.user import User


def list_users():
    return User.query.all()


def create_user(**kwargs):
    user = User(**kwargs)
    db.session.add(user)
    db.session.commit()

    return user


def find_user_by_email_and_pass(email, password):
    return User.query.filter(User.email == email, User.password == password).first()


def find_user_by_email(email):
    return User.query.filter(User.email == email).first()
