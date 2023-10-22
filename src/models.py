from db import db

# id - число
# name_object - название объекта
# type_object - тип объекта
# material - материал изготовления
# date_manufacture - дата изготовления
# price - стоимость объекта
# location - расположение объекта
# ______________________________________
# db.String(50) - текстовое поле заданной длины
# db.Integer() - числовое поле
# db.Column() - создание колонки(дополнительные поля nullable, unique, primary_key)
# для id всегда задается primary_key=True

class Object(db.Model):
    __tablename__ = "object"

    id = db.Column(db.Integer(), primary_key=True) # идентификационный номер
    name_object = db.Column(db.String(50)) # название объекта

    type_object = db.Column(db.String(50)) # тип объекта
    material = db.Column(db.String(50)) # материал изготовления
    date_manufacture = db.Column(db.String(10)) # дата изготовления

    price = db.Column(db.Float()) # стоимость объекта
    location = db.Column(db.String(50)) # расположение объекта
