import logging
import asyncio
from pysnmp.hlapi.asyncio import SnmpEngine, CommunityData, ContextData
from pysnmp.entity import config
from pysnmp.carrier.asyncio.dgram import udp
from pysnmp.entity.rfc3413 import ntfrcv
import smtplib
from email.mime.text import MIMEText

# Настройка логирования
logging.basicConfig(
    filename='snmp_traps.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG  # Установите на DEBUG для получения полной информации
)

# Функция для отправки email
def send_email(subject, message):
    sender = "your_email@example.com"
    receiver = "recipient@example.com"
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login("your_email@example.com", "your_password")
            server.sendmail(sender, receiver, msg.as_string())
            logging.info("Email sent to %s", receiver)
    except Exception as e:
        logging.error("Failed to send email: %s", str(e))

# Callback функция для обработки Trap сообщений
def cbFun(snmpEngine, stateReference, contextEngineId, contextName, varBinds, cbCtx):
    log_message = 'Received new Trap message:\n'
    for name, val in varBinds:
        log_message += '%s = %s\n' % (name.prettyPrint(), val.prettyPrint())

    logging.info(log_message)
    print(log_message)

    for name, val in varBinds:
        if 'linkDown' in val.prettyPrint():
            logging.debug("Detected 'linkDown', sending email...")
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
            udp.UdpTransport().openServerMode(('0.0.0.0', 162))
        )

        # Настройка SNMPv2c
        config.addV1System(snmpEngine, 'my-area', 'public')

        # Привязка функции обработки сообщений
        ntfrcv.NotificationReceiver(snmpEngine, cbFun)

        logging.info("SNMP Trap Receiver is running and logging to 'snmp_traps.log'...")
        print("SNMP Trap Receiver is running and logging to 'snmp_traps.log'...")

        # Запуск обработчика asyncio
        snmpEngine.transportDispatcher.jobStarted(1)  # Эта строка важна для корректной работы
        snmpEngine.transportDispatcher.runDispatcher()
    except Exception as e:
        logging.error("Error in SNMP Trap Receiver: %s", str(e))
        raise

# Запуск asyncio loop
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.run_forever()
