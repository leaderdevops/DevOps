# Lesson 1 Variables  USE iPython Interactve
from dsp3.models.manager import Manager  #import statement needed for 3rd party packages
from ..utils import utils
from .person import Person

'''
  * In Python, everything: booleans, integers, floats, strings, even large data structures, functions, and programs—is implemented as an object. 
  * An object is like a clear plastic box that contains a piece of data
  
  Run Script from project root dir:
  python -m app.intro.a_variables

'''


username, password, tenant = utils.parse_dsas_crendentials()

type(tenant)


dsm = Manager(username=username, password=password, tenant=tenant)

type(dsm)

api_version = dsm.get_api_version()
type(api_version)

api_version == 99

type(api_version == 99)


# variables vs objects
a = 9
b = a
a = 10
print('b = %d' % b)



david = Person(first_name='David', last_name='Girard', favorite_product='DD', citizenship='Canadian')
american = david
american.favorite_product = 'DS'
print("David's favorite product is: %s" % david.favorite_product) # what the?


dsm.end_session()