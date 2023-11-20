from src.models import Object, Service, ServiceGroup
from src.app import app


with app.app_context():
    object = Object.query.all()
    for o in object:
        print(o)


with app.app_context():
    services = Service.query.all()
    for s in services:
        print(s)


with app.app_context():
    service_groups = ServiceGroup.query.all()
    print(service_groups)


with app.app_context():
    services = Service.query.filter_by(service_group_id=1).all()
    service = Service.query.filter_by(service_group_id=3).all()
    for s in  services:
        print(f"id=1 {s}")
    for ss in service:
        print(f"id=3 {ss}")
