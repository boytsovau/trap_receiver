from load_file import (
    get_path,
    open_file
)


RULES = open_file('configs', 'notification_rules.json')
RECEPIENTS = open_file('configs', 'recipients.json')
DEVICE = open_file('configs', 'device.json')
MIB = get_path('mibs')
