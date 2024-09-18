import asyncio
from log_config import setup_logger
from handlers import IpParser, MIBEntry, Resolve, GetUptime
from config import (
    RULES,
    DEVICE,
    RECEPIENTS
)

from mailer import send_email
from pysnmp.hlapi.asyncio import (
    SnmpEngine,
    CommunityData,
    ContextData
    )
from pysnmp.entity import config
from pysnmp.carrier.asyncio.dgram import udp
from pysnmp.entity.rfc3413 import ntfrcv


logger = setup_logger('trap_log', 'traplog.log')


# Callback функция для обработки Trap сообщений
def cbFun(snmpEngine, stateReference, contextEngineId, contextName, varBinds, cbCtx):
    # Извлечение информации о транспортном соединении из stateReference
    transportDomain, transportAddress = snmpEngine.msgAndPduDsp.getTransportInfo(stateReference)
    src_ip = transportAddress[0]  # IP-адрес отправителя
    hostname = DEVICE.get(src_ip)
    log_message = f'Received new Trap from {hostname} {src_ip}:\n'

    for name, val in varBinds:
        value = Resolve(val).get_resolve()
        oid = Resolve(name).get_resolve()
        log_message += f'{MIBEntry(oid).get_name()} = {MIBEntry(value).get_name()}\n'
    logger.info(log_message)

    # Проверка на конкретное значение Trap и отправка email
    email_sent = False

    for name, val in varBinds:
        if email_sent:
            break
        oid = Resolve(name).get_resolve()
        for rule in RULES["notifications"]:
            sensitivity = rule['sensitivity']
            mail_to = RECEPIENTS.get(sensitivity)

            if rule["oid"] in oid:

                # Формируем сообщение с информацией обо всех OID в Trap
                message = f"Trap received for {MIBEntry(oid).get_name()} from {hostname}: {src_ip}:\n\n"

                for name, val in varBinds:
                    value = Resolve(val).get_resolve()
                    oid = Resolve(name).get_resolve()
                    if MIBEntry(oid).get_name() == "ipCidrRouteNextHop":
                        message += f'route change {IpParser(MIBEntry(oid).get_numbers).get_route()}: Value {MIBEntry(value).get_name()}\n'
                    if MIBEntry(oid).get_name() == "sysUpTime":
                        message += f'{MIBEntry(oid).get_name()} = {GetUptime(int(MIBEntry(value).get_name()))}\n'
                    message += f'{MIBEntry(oid).get_name()} = {MIBEntry(value).get_name()}\n'

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
