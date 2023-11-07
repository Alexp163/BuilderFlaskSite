from db import db
from app import app
from models import Object, Service, ServiceGroup


with app.app_context():
    db.drop_all()
    db.create_all()


with app.app_context():
    object = Object(name_object="Лесная сказка", type_object="Двухэтажный дом",
                    material="кирпич", date_manufacture="10.10.2022",
                    price="5000000.00", location="Самара, Пос.Волжский")
    db.session.add(object)
    object1 = Object(name_object="Дом моряка", type_object="Одноэтажный дом",
                    material="пеноблок и кирпич", date_manufacture="08.10.2022",
                    price="4000000.00", location="Самара, Пос.Управленческий")
    db.session.add(object1)
    db.session.commit()


with app.app_context():
    service = Service(name_service = "Строительство домов",
                      department_name = "отдел строительства",
                      deadlines_implementation = "6 месяцев", price = "8000000.00",
                      department_contact_information = "Самара, Луговая, 24, тел. +7929987876")
    db.session.add(service)
    service1 = Service(name_service = "Продажа домов с оформлением документации",
                      department_name = "Отдел продаж",
                      deadlines_implementation = "1 месяц", price = "10000.00",
                      department_contact_information = "Самара, Ленина , 33, тел. +7929987876")
    db.session.add(service1)
    db.session.commit()


with app.app_context():
    group1 = ServiceGroup(name="Отдел строительства",
                          description="здесь будет описана группа")
    group2 = ServiceGroup(name="Административно правовой отдел",
                          description="здесь будет описана группа")
    group3 = ServiceGroup(name="Отдел продаж",
                          description="здесь будет описана группа")
    group4 = ServiceGroup(name="Отдел снабжения",
                          description="здесь будет описана группа")
    db.session.add(group1)
    db.session.add(group2)
    db.session.add(group3)
    db.session.add(group4)
    db.session.commit()
    service = Service(name_service = "Строительство домов",
                      department_name = "отдел строительства",
                      deadlines_implementation = "6 месяцев", price = "8000000.00",
                      department_contact_information = "Самара, Луговая, 24, тел. +7929987872",
                      service_group=group1)
    db.session.add(service)
    service1 = Service(name_service = "Административно правовой отдел",
                      department_name = "Юридическое и финансовое сопровождение сделки",
                      deadlines_implementation = "На протяжении всего этапа строительства или продажи",
                       price = "10000.00",
                      department_contact_information = "Самара, Ленина , 33, тел. +7929987871",
                       service_group=group2)
    db.session.add(service1)
    service2 = Service(name_service = "Подбор, продажа домов",
                      department_name = "Отдел продаж",
                      deadlines_implementation = "1 месяц", price = "20000.00",
                      department_contact_information = "Самара, Бетховена , 44, тел. +7929987874",
                       service_group=group3)
    db.session.add(service2)
    service3 = Service(name_service = "Закупка и снабжение строительными материалами",
                      department_name = "Отдел снабжения",
                      deadlines_implementation = "2-3 месяца", price = "80000.00",
                      department_contact_information = "Самара, Дзержинского , 12, тел. +7929987877",
                       service_group=group4)
    db.session.add(service3)
    db.session.commit()