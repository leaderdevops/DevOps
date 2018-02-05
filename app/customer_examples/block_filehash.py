from dsp3.models.manager import Manager
from ..utils import utils

'''
Customer: Not disclosed in repo

run file from project root dir as:
python -m app.customer_examples.block_filehash


'''


username, password, tenant = utils.parse_dsas_crendentials()
dsm = Manager(username=username, password=password, tenant=tenant)

rules = dsm.list_block_by_hash_rules() # returns json object representing list of Block by Hash Rules

print(rules)
# How to get the sha256 has of a file on a mac: shasum -a 256 test.sh

# adds new block by hash rule. based on sha256 file hash.
# The blacklist rules are then applied and enforced on any agent that has AppControl turned on.
dsm.add_block_by_hash_rule("3c65c5bf26a8cb8912387e5f28c4b6192699185b70084739f4fcbe4200bc413c", "Block test.sh File")

dsm.delete_block_by_hash_rule(1) #deletes block by hash rule by rule id

dsm.end_session()





# ssh to host
# wget https://www.dropbox.com/s/icw8fnkufexetuo/test.sh
# chmod 755 test.sh
# ./test.sh

# run this script then try again
# ./test.sh
