from db import db
from app import app
from models import Object


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
    objects = Object.query.all()
    for o in objects:
        print(o.name_object, o.type_object, o.material, o.date_manufacture,
              o.price, o.location )