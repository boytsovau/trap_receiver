from load_file import (
    get_path,
    open_file
)
from mib_loader import load_mib_modules


RULES = open_file('configs', 'notification_rules.json')
RECEPIENTS = open_file('configs', 'recipients.json')
DEVICE = open_file('configs', 'device.json')
MIB = get_path('mibs')

mib = load_mib_modules(MIB, ['py'])
