from flask import Blueprint
from flask import render_template
from flask import request
from flask import abort
from flask import session

from src.core import auth
from src.web.helpers.auth import login_required


users_blueprint = Blueprint("users", __name__, url_prefix="/usuarios")


@users_blueprint.route("/", methods=["GET"])
@login_required
def index():
    users = auth.list_users()

    return render_template("users/index.html", users=users)
