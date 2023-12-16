from db import db
from app import app
from flask import render_template, flash, request
from models import Object, Service, ServiceGroup, User
from forms import LoginForm, RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user


@app.route('/')
def index():
    service_groups = ServiceGroup.query.all()
    return render_template('index.html', service_groups=service_groups)


@app.route('/objects')
def objects():
    objects = Object.query.all()
    """  Отображает страницу с построенными зданиями """
    return render_template('/objects.html', objects=objects)


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print("Кнопка нажата!!!")
        flash("Кнопка нажата")
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        if user is not None and check_password_hash(user.password_hash, password):
            login_user(user)
            flash("Авторизация успешна!")
        else:
            flash("Неверный логин или пароль!")
    return render_template('login.html', form=form)


@app.route('/registration', methods=['GET','POST'])
def registration():
    form = RegisterForm()
    if request.method=='POST' and form.validate():
        print("Кнопка нажата!!!")
        flash("Кнопка нажата")
        email = form.email.data
        pass_1 = form.password_1.data
        pass_2 = form.password_2.data
        if pass_1 == pass_2:
            if len(User.query.filter_by(email=email).all())==0:
                user = User(email=email, password_hash=generate_password_hash(pass_1))
                db.session.add(user)
                db.session.commit()
                flash("Регистрация прошла успешно!!!")
            else:
                flash("Вы уже проходили регистрацию!")
        else:
            flash("Пароли не совпадают!")
    return render_template('registration.html', form=form)


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



