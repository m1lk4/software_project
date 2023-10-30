from flask import Blueprint
from flask import render_template

from src.core import board


item_blueprint = Blueprint("items", __name__, url_prefix="/items")


@item_blueprint.get("/")
def index():
    items = board.list_items()

    return render_template("items/index.html", items=items)
