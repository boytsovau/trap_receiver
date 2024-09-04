import asyncio
import json
import os
from log_config import setup_logger
from mib_loader import load_mib_modules
from mailer import send_email
from pysnmp.hlapi.asyncio import SnmpEngine, CommunityData, ContextData # noqa: F401
from pysnmp.entity import config
from pysnmp.carrier.asyncio.dgram import udp
from pysnmp.entity.rfc3413 import ntfrcv
from pysnmp.smi import rfc1902


logger = setup_logger('trap_log', 'traplog.log')

current_dir = os.path.dirname(os.path.abspath(__file__))

# Определяем полный путь к файлам
notification_rules_path = os.path.join(current_dir, 'configs', 'notification_rules.json')
recipients_path = os.path.join(current_dir, 'configs', 'recipients.json')
device_path = os.path.join(current_dir, 'configs', 'device.json')
mib_path = os.path.join(current_dir, 'mibs')

try:
    with open(notification_rules_path, 'r') as rules:
        notification_rules = json.load(rules)
except FileNotFoundError:
    print(f"File {notification_rules_path} not found.")
    notification_rules = {}

try:
    with open(recipients_path, 'r') as r:
        recipients = json.load(r)
except FileNotFoundError:
    print(f"File {recipients_path} not found.")
    recipients = {}

try:
    with open(device_path, 'r') as d:
        device = json.load(d)
except FileNotFoundError:
    print(f"File {device_path} not found.")
    device = {}

mib = load_mib_modules(mib_path, ['HUAWEI', 'CISCO'])



# Callback функция для обработки Trap сообщений
def cbFun(snmpEngine, stateReference, contextEngineId, contextName, varBinds, cbCtx):
    # Извлечение информации о транспортном соединении из stateReference
    transportDomain, transportAddress = snmpEngine.msgAndPduDsp.getTransportInfo(stateReference)
    src_ip = transportAddress[0]  # IP-адрес отправителя
    hostname = device.get(src_ip)
    log_message = f'Received new Trap from {hostname} {src_ip}:\n'

    for name, val in varBinds:
        oid = name.prettyPrint()  # OID в текстовом виде
        value = val.prettyPrint()  # Значение в текстовом виде
        log_message += f'{oid} = {value}\n'

    logger.info(log_message)
    # print(log_message)

    # Проверка на конкретное значение Trap и отправка email
    email_sent = False

    for name, val in varBinds:
        oid = name.prettyPrint()
        resolved_oid = rfc1902.ObjectIdentity(name).resolveWithMib(mib)
        for rule in notification_rules["notifications"]:
            sensitivity = rule['sensitivity']
            mail_to = recipients.get(sensitivity)

            if rule["oid"] in oid:

                # Формируем сообщение с информацией обо всех OID в Trap
                message = f"Trap received for {rule['description']} from {hostname}: {src_ip}:\n\n"

                for name, val in varBinds:
                    try:
                        if name == "1.3.6.1.6.3.1.1.4.1.0 ":
                            resolved_oid = rfc1902.ObjectIdentity(name).resolveWithMib(mib)
                            resolved_val = rfc1902.ObjectIdentity(val).resolveWithMib(mib)
                            message += f"OID: {resolved_oid.prettyPrint()} = {resolved_val.prettyPrint()}\n"
                        resolved_oid = rfc1902.ObjectIdentity(name).resolveWithMib(mib)
                        message += f"OID: {resolved_oid.prettyPrint()} = {val.prettyPrint()}\n"
                    except Exception as e:
                        log_message += f'{name} = {val.prettyPrint()} (Could not resolve OID: {e})\n'

                send_email(rule["email_subject"], message, mail_to)
                email_sent = True
                break

    if not email_sent:
        logger.info("No matching OID found in the notification rules.")


# Основная функция
async def main():
    try:
        snmpEngine = SnmpEngine()

        # Настройка транспорта для получения SNMP TRAP сообщений
        config.addTransport(
            snmpEngine,
            udp.DOMAIN_NAME,
            udp.UdpTransport().openServerMode(('0.0.0.0', 10162))
        )

        # Настройка SNMPv2c
        config.addV1System(snmpEngine, 'my-area', 'public')

        # Привязка функции обработки сообщений
        ntfrcv.NotificationReceiver(snmpEngine, cbFun)

        logger.info("SNMP Trap Receiver is running")
        # print("SNMP Trap Receiver is running and logging to 'snmp_traps.log'...")

        # Запуск обработчика asyncio
        snmpEngine.transportDispatcher.jobStarted(1)
        snmpEngine.transportDispatcher.runDispatcher()
    except Exception as e:
        logger.error("Error in SNMP Trap Receiver: %s", str(e))
        raise


if __name__ == "__main__":
    # Запуск asyncio loop
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.run_forever()
