import json
from ..utils import utils
from dsp3.models.manager import Manager


username, password, tenant = utils.parse_dsas_crendentials()
dsm = Manager(username=username, password=password, tenant=tenant)
api_version = dsm.get_api_version()

#string interpolation
print('API version is: %d' %  api_version)
print(f'API version is: {api_version}')
print('API version is {}'.format(api_version))

# conditional logic
if api_version > 10:
    print('we are good')


if api_version < 20:
    print('we are good')
else:
    print('what is going on in Ottawa?')

print('we are good\n') if api_version > 20 else print('I am on the wrong version\n')

if api_version > 0 and api_version <= 5:
    print('we are on old school version')
elif 5 > api_version < 10:                        #chained comparison
    print('we are on 2nd gen 3b apis')
elif 19 >= api_version < 30:
    print('we are living in present day')


cloud_accounts = dsm.get_cloudaccounts()
print(type(cloud_accounts))

# looping mechanisms: for loop
for account in cloud_accounts['ListCloudAccountsResponse']['cloudAccount']:
    print(account)


dsm.end_session()