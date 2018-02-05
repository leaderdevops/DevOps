import time
import requests
from dsp3.models.manager import Manager
from ..utils import utils


'''
CUSTOMER: Not disclosed in repo

run file from project root dir as: 
python -m app.customer_examples.xforward_ipsrule

'''


username, password, tenant = utils.parse_dsas_crendentials()
elb_url = utils.parse_elb_url()
dsm = Manager(username=username, password=password, tenant=tenant)

ruleXML = ""
my_public_ip = utils.get_public_ip()
ip_addresses = utils.process_ips(my_public_ip)

for ip in ip_addresses:
    rule = '<rule pat="X-Forwarded-For: %s" cmask="0x3" ctest="0x1">\n' % ip
    rule = rule + 'drop "Found IP from Block List in XFF Header"\n'
    rule = rule + "</rule>\n"
    ruleXML = ruleXML + rule

result = dsm.dpi_rule_save("Web Server Common", "Block-X-Forward-List", True, True, "CUSTOM_XML", "DROP_CLOSE", "ANY_PATTERNS_FOUND", "NORMAL", "DROP_CLOSE", "MEDIUM", ruleXML)

# Lets try a gui less demo now :-)

print("Let's makes sure our policy is in dectect mode")
xforward_policy = dsm.get_security_profile_by_name('xforward test')
print('Current state of Block-X-Forward-List is: ', xforward_policy.DPIState)
xforward_policy.DPIState = "PASSIVE"  #put policy in prvent mode
dsm.security_profile_save(xforward_policy)
xforward_policy = dsm.get_security_profile_by_name('xforward test')
print('New state of Block-X-Forward-List is: ', xforward_policy.DPIState, end='\n\n')
print('Now sleeping 15 secs so DS can deploy new policy')
time.sleep(15)

print("Now lets make an HTTP GET request to the elb and see what happens")
requests.get(url=elb_url, headers={"Cache-Control": "no-cache"})
requests.get(url=elb_url, headers={"Cache-Control": "no-cache"})
requests.get(url=elb_url, headers={"Cache-Control": "no-cache"})
print(requests.get(url=elb_url, headers={"Cache-Control": "no-cache"},).content,  end='\n\n')

dsm.host_getevents_now(6035)
dsm.host_getevents_now(6023)
time.sleep(15)
dpi_events = dsm.dpi_event_retrieve(time_type='LAST_HOUR')

if dpi_events is not None and len(dpi_events) > 0:
    print("Getting latest DPI event. Reason:[{}] Action:[{}]  at [{}] ".format(dpi_events[-1].reason, dpi_events[-1].action, dpi_events[-1].startTime))
else:
    print('No DPI events found. X-Forwarded-For may contain multiple ips.')

dsm.dpi_event_retrieve()
print("Let's turn our policy on prevent mode now")
xforward_policy.DPIState = "ON"  #put policy in prvent mode
dsm.security_profile_save(xforward_policy)
xforward_policy = dsm.get_security_profile_by_name('xforward test')
print('New state of Block-X-Forward-List is: ', xforward_policy.DPIState, end='\n\n')
print('Now sleeping 15 secs so DS can deploy new policy')
time.sleep(15)

print("Now lets make an HTTP GET request to the elb and see what happens")
requests.get(url=elb_url, headers={"Cache-Control": "no-cache"})
requests.get(url=elb_url, headers={"Cache-Control": "no-cache"})
requests.get(url=elb_url, headers={"Cache-Control": "no-cache"})
print(requests.get(url=elb_url, headers={"Cache-Control": "no-cache"}).content)

dsm.host_getevents_now(6035)
dsm.host_getevents_now(6023)
time.sleep(15)
dpi_events = dsm.dpi_event_retrieve(time_type='LAST_HOUR')

if dpi_events is not None and len(dpi_events) > 0:
    print("Getting latest DPI event. Reason:[{}] Action:[{}]  at [{}] ".format(dpi_events[-1].reason, dpi_events[-1].action, dpi_events[-1].startTime))
else:
    print('No DPI events found. X-Forwarded-For may contain multiple ips.')


dsm.end_session()


