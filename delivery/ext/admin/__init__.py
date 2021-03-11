from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from delivery.ext.db import db
from delivery.ext.db.models import Category


admin = Admin()

def init_app(app):
    admin.name = app.config.get("ADMIN_NAME", "Codefoods")
    admin.template_mode = app.config.get("ADMIN_TAMPLATE_MODE","bootstrap2")
    admin.init_app(app)

    # TODO: proteger com senha

    admin.add_view(ModelView(Category, db.session))


