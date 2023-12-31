from src.core.database import db
from src.core.board.issue import Issue
from src.core.board.label import Label
from src.core.board.item import Item


def create_item(**kwargs):
    item = Item(**kwargs)
    db.session.add(item)
    db.session.commit()

    return item


def list_items():
    return Item.query.all()


def list_issues():
    return Issue.query.all()


def create_issue(**kwargs):
    issue = Issue(**kwargs)
    db.session.add(issue)
    db.session.commit()

    return issue


def assign_user(issue, user):
    issue.user = user
    db.session.add(issue)
    db.session.commit()

    return issue


def assign_labels(issue, labels):
    issue.labels.extend(labels)
    db.session.add(issue)
    db.session.commit()

    return issue


def create_label(**kwargs):
    label = Label(**kwargs)
    db.session.add(label)
    db.session.commit()

    return label
