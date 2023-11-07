from app import app
from flask import render_template
from db_run import Object, Service


@app.route('/')
def index():
    return render_template('index.html')


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



