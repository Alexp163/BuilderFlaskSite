from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/case_costruite')
def case_costruite():
    """  Отображает страницу с построенными зданиями """
    return render_template('/case_costruite.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/registration')
def registration():
    return render_template('registration.html')
