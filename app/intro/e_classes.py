"""

Run Script from project root dir:
  python -m app.intro.e_classes

"""


import json
from dsp3.models.manager import Manager
from ..utils import utils
from .person import Person

username, password, tenant = utils.parse_dsas_crendentials()
dsm = Manager(username=username, password=password, tenant=tenant)
hosts = dsm.host_retrieve_all()

if len(hosts) > 0:
    host_model = dsm.get_host_by_name(hosts[0]['name'])     # check out utils -> dsp3_host.py file for model definition
    print(host_model.__dict__)
    print(json.dumps(host_model.__dict__))




jen = Person('Jen', 'Smith')
print(jen.first_name)
print(jen.last_name)
print(jen)

