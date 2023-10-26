from flask import Blueprint
from src.core import board


issue_api_blueprint = Blueprint("issues_api", __name__, url_prefix="/api/consultas")


@issue_api_blueprint.route("/", methods=["GET"])
def index():
    issues = board.list_issues()

    return {"status": "ok"}
