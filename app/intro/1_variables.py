# Lesson 1 Variables  USE iPython Interactve
from dsp3.models.manager import Manager  #import statement needed for 3rd party packages
from ..utils import utils

'''
  * In Python, everything: booleans, integers, floats, strings, even large data structures, functions, and programs—is implemented as an object. 
  * An object is like a clear plastic box that contains a piece of data
'''


username, password, tenant = utils.parse_dsas_crendentials()

type(tenant)


dsm = Manager(username=username, password=password, tenant=tenant)

type(dsm)

api_version = dsm.get_api_version()
type(api_version)

api_version == 99

type(api_version == 99)


dsm.end_session()