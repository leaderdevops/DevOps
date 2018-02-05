from dsp3.models.manager import Manager
from ..utils import utils

'''

Customer: Not disclosed in repo
They needed to add 300 aws accounts to the DSM

https://help.deepsecurity.trendmicro.com/Add-Computers/add-aws.html

Add by AK/SAK
https://help.deepsecurity.trendmicro.com/Add-Computers/add-aws.html#Add5

Add by cross account role
https://help.deepsecurity.trendmicro.com/Add-Computers/add-aws.html#Add2


run file from project root dir as:
python -m app.customer_examples.add_aws_account

'''


username, password, tenant = utils.parse_dsas_crendentials()
access_key, secret_key = utils.parse_aws_crendentials()
dsm = Manager(username=username, password=password, tenant=tenant)

print(dsm.get_cloudaccounts(), end='\n')

dsm.add_aws_cloud_account_with_keys(access_key=access_key, secret_key=secret_key)

# or

#dsm.add_aws_cloud_account_with_cross_account_role('randomsecret2', 'arn:aws:iam::5385xvxv281:role/DS_Cross_account')


print(dsm.get_cloudaccounts(), end='\n')
dsm.end_session()