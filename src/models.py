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

    def __repr__(self):
        return (f"<Наименование объекта - {self.name_object}, "
                f"тип объекта - {self.type_object}, материал изготовления - {self.material}, "
                f"дата изготовления - {self.date_manufacture}, цена - {self.price}, "
                f"расположение объекта - {self.location} >")



class Service(db.Model):
    __tablename__ = 'service'
    id = db.Column(db.Integer(), primary_key=True) # идентификационный номер
    name_service = db.Column(db.String(100)) # название услуги

    department_name = db.Column(db.String(50)) # наименование отдела исполнителя
    deadlines_implementation = db.Column(db.String(50))# сроки выполнения услуги

    price = db.Column(db.Float())# стоимость работ
    department_contact_information = db.Column(db.Text()) # контакты отдела-исполнителя
    service_group_id = db.Column(db.ForeignKey("service_group.id"))  # id группы, к которой относится эта услуга
    service_group = db.Relationship("ServiceGroup")  # ссылка на группу(id которой указан в вышестоящей строчке)
    def __repr__(self):
        return (f"<Функция repr(): {self.name_service}, отдел исполнителя: {self.department_name}, "
                f"сроки исполнения: {self.deadlines_implementation}, стоимость услуги: {self.price},"
                f"контакты исполнителя: {self.department_contact_information}>")


class ServiceGroup(db.Model):
    __tablename__ = "service_group"
    id = db.Column(db.Integer(), primary_key=True)

    name = db.Column(db.String(100))  # название группы
    description = db.Column(db.Text())  # описание группы
    # создать руководителя группы
    def __repr__(self):
        return f"<Сервисная группа: {self.name}, описание группы: {self.description}>"
