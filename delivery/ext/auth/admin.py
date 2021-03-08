from flask_admin.contrib.sqla import ModelView
from flask_admin.actions import action
from delivery.ext.auth.models import User
from delivery.ext.db import db
from flask import flash


# def format_user(self, request, user, *args):
#     return user.email.split("@")[0]


class UserAdmin(ModelView):
    """Interface admin de user"""

    column_formatters = {
        "email": lambda s, r, u, *a: u.email.split("@")[0]
    }

    column_list = ["email", "admin"]
    column_searchable_list = ["email"]
    column_filters = ["email", "admin"]

    can_edit = False
    can_create = True
    can_delete = True

    @action(
        "toggle_admin",
        "Toggle admin status",
        "Are you sure?"
    )
    def toggle_admin_status(self, ids):
        for user in User.query.filter(User.id.in_(ids)).all():
            user.admin = not user.admin
        db.session.commit()
        flash("Usuários alterados com sucesso!", "success")
