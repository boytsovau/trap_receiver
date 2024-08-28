import asyncio
from log_config import setup_logger
from mailer import send_email
from pysnmp.hlapi.asyncio import SnmpEngine, CommunityData, ContextData
from pysnmp.entity import config
from pysnmp.carrier.asyncio.dgram import udp
from pysnmp.entity.rfc3413 import ntfrcv


logger = setup_logger('trap_log', 'traplog.log')


# Callback функция для обработки Trap сообщений
def cbFun(snmpEngine, stateReference, contextEngineId, contextName, varBinds, cbCtx):
    # Извлечение информации о транспортном соединении из stateReference
    transportDomain, transportAddress = snmpEngine.msgAndPduDsp.getTransportInfo(stateReference)
    src_ip = transportAddress[0]  # IP-адрес отправителя

    log_message = f'Received new Trap from {transportDomain} {transportAddress} ({src_ip}):\n'

    for name, val in varBinds:
        oid = name.prettyPrint()  # OID в текстовом виде
        value = val.prettyPrint()  # Значение в текстовом виде
        log_message += f'{oid} = {value}\n'

    logger.info(log_message)
    # print(log_message)

    # Проверка на конкретное значение Trap и отправка email
    for name, val in varBinds:
        if 'linkDown' in val.prettyPrint():
            logger.debug("Detected 'linkDown', sending email...")
            send_email("SNMP Trap Alert", log_message)
            break


# Основная функция
async def main():
    try:
        snmpEngine = SnmpEngine()

        # Настройка транспорта для получения SNMP TRAP сообщений
        config.addTransport(
            snmpEngine,
            udp.domainName,
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


# Запуск asyncio loop
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.run_forever()
