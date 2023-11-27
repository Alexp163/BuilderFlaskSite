from flask_admin import Admin
from app import app
from flask_admin.contrib.sqla import ModelView
from models import Object, Service, ServiceGroup
from db import db


admin = Admin(app, __name__, template_mode="bootstrap3")


class ObjectModelView(ModelView):
    column_list = ('name_object', 'type_object', 'material', 'date_manufacture', 'price',
                   'location')
    form_excluded_columns = ('created_at', 'updated_at')


class ServiceModelView(ModelView):
    column_list = ('name_service', 'department_name', 'deadlines_implementation',
                   'price', 'department_contact_information')
    form_excluded_columns = ('created_at', 'updated_at')


admin.add_view(ObjectModelView(Object, db.session))
admin.add_view(ServiceModelView(Service, db.session))
admin.add_view(ModelView(ServiceGroup, db.session))
