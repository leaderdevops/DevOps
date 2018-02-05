import json
from dsp3.models.manager import Manager
from ..utils import utils

username, password, tenant = utils.parse_dsas_crendentials()
dsm = Manager(username=username, password=password, tenant=tenant)
hosts = dsm.host_retrieve_all()

if len(hosts) > 0:
    host_model = dsm.get_host_by_name(hosts[0]['name'])     # check out utils -> dsp3_host.py file for model definition
    print(host_model.__dict__)
    print(json.dumps(host_model.__dict__))


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return 'I am an object of type {} found at memory address {}'.format(type(self), id(self))


jen = Person('Jen', 'Smith')
print(jen.first_name)
print(jen.last_name)
print(jen)

