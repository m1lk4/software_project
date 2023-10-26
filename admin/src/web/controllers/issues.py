from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import session
from flask import url_for

from src.core import board
from src.core.board import Issue, db


issue_blueprint = Blueprint("issues", __name__, url_prefix="/consultas")


@issue_blueprint.get("/")
def index():
    issues = board.list_issues()

    return render_template("issues/index.html", issues=issues)


@issue_blueprint.get("/new")
def new():
    return render_template("issues/new.html")


@issue_blueprint.post("/")
def create():
    params = request.form
    board.create_issue(**params)
    return redirect("/consultas")


@issue_blueprint.get("/<int:id>/edit")
def edit(id):
    if "user" not in session:
        return redirect(url_for("auth.login"))
    else:
        issue = Issue.query.get(id)
        return render_template("issues/edit.html", issue=issue)


@issue_blueprint.post("/<int:id>")
def update(id):
    title = request.form["title"]
    description = request.form.get("description")
    status = request.form.get("status")
    issue = Issue.query.get(id)
    issue.title = title
    issue.description = description
    issue.status = status
    db.session.commit()
    return redirect("/consultas")


@issue_blueprint.get("/delete/<int:id>")
def delete(id):
    issue = Issue.query.get(id)
    if issue:
        db.session.delete(issue)
        db.session.commit()

        return redirect("/consultas")
    else:
        return "El issue no existe o no se puede eliminar"
