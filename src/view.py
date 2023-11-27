from app import app
from flask import render_template
from models import Object, Service, ServiceGroup


@app.route('/')
def index():
    service_groups = ServiceGroup.query.all()
    return render_template('index.html', service_groups=service_groups)


@app.route('/objects')
def objects():
    objects = Object.query.all()
    """  Отображает страницу с построенными зданиями """
    return render_template('/objects.html', objects=objects)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/registration')
def registration():
    return render_template('registration.html')


@app.route('/objects/<int:object_id>')
def one_object(object_id):
    object = Object.query.get(object_id)
    return render_template('one_object.html', object=object)


@app.route('/our_service')
def our_service():
    service = Service.query.all()
    return render_template('our_service.html', service=service)


@app.route('/service_group/<int:service_group_id>')
def service_group(service_group_id):
    service_group = ServiceGroup.query.get(service_group_id)
    service_groups = ServiceGroup.query.all()
    service = Service.query.filter_by(service_group_id=service_group_id).all()
    return render_template("service_group.html", service_group=service_group,
                           service=service, service_groups=service_groups)



