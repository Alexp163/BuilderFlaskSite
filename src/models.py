from db import db
from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime, Float
from sqlalchemy.orm import Relationship
from sqlalchemy.sql import func


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

    id = Column(Integer(), primary_key=True) # идентификационный номер
    name_object = Column(String(50)) # название объекта

    type_object = Column(String(50)) # тип объекта
    material = Column(String(50)) # материал изготовления
    date_manufacture = Column(String(10)) # дата изготовления

    price = Column(Float()) # стоимость объекта
    location = Column(String(50)) # расположение объекта

    created_at = Column(DateTime, server_default=func.now())  # дата создания
    updated_at = Column(DateTime, server_onupdate=func.now())  # дата обновления

    def __repr__(self):
        return (f"<Наименование объекта - {self.name_object}, "
                f"тип объекта - {self.type_object}, материал изготовления - {self.material}, "
                f"дата изготовления - {self.date_manufacture}, цена - {self.price}, "
                f"расположение объекта - {self.location} >")



class Service(db.Model):
    __tablename__ = 'service'
    id = Column(Integer(), primary_key=True) # идентификационный номер
    name_service = Column(String(100)) # название услуги

    department_name = Column(String(50)) # наименование отдела исполнителя
    deadlines_implementation = Column(String(50))# сроки выполнения услуги

    price = Column(Float())# стоимость работ
    department_contact_information = Column(Text()) # контакты отдела-исполнителя
    service_group_id = Column(ForeignKey("service_group.id"))  # id группы, к которой относится эта услуга
    service_group = Relationship("ServiceGroup")  # ссылка на группу(id которой указан в вышестоящей строчке)

    created_at = Column(DateTime, server_default=func.now())  # дата создания
    updated_at = Column(DateTime, server_onupdate=func.now())  # дата обновления

    def __repr__(self):
        return (f"<Функция repr(): {self.name_service}, отдел исполнителя: {self.department_name}, "
                f"сроки исполнения: {self.deadlines_implementation}, стоимость услуги: {self.price},"
                f"контакты исполнителя: {self.department_contact_information}>")


class ServiceGroup(db.Model):
    __tablename__ = "service_group"
    id = Column(Integer(), primary_key=True)

    name = Column(String(100))  # название группы
    description = Column(Text())  # описание группы

    created_at = Column(DateTime, server_default=func.now())  # дата создания
    updated_at = Column(DateTime, server_onupdate=func.now())  # дата обновления

    # создать руководителя группы
    def __repr__(self):
        return f"<Сервисная группа: {self.name}, описание группы: {self.description}>"
