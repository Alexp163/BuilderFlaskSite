from app import app
from flask import render_template
from db_run import Object


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/case_costruite')
def case_costruite():
    objects = Object.query.all()
    """  Отображает страницу с построенными зданиями """
    return render_template('/case_costruite.html', objects=objects)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/registration')
def registration():
    return render_template('registration.html')


@app.route('/building/1')
def one_object():
    return render_template('one_object.html')
