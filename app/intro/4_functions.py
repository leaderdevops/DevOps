from dsp3.models.manager import Manager
from ..utils import utils


username, password, tenant = utils.parse_dsas_crendentials()
dsm = Manager(username=username, password=password, tenant=tenant)


def get_events_by_type(event_type):
    events = []
    if event_type == 'dpi':
        events = dsm.dpi_event_retrieve(time_type='LAST_7_DAYS')
    elif event_type == 'am':
        events = dsm.antimalware_event_retrieve(time_type='LAST_HOUR')
    else:
        events = ['I can\'t help you']

    return events


print(len(get_events_by_type('dpi')))
print(len(get_events_by_type('ML')))
