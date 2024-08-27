import socket
import logging
import asyncio
import smtplib
from pysnmp.hlapi.asyncio import SnmpEngine
from pysnmp.entity import config
from pysnmp.carrier.asyncio.dgram import udp
from pysnmp.entity.rfc3413 import ntfrcv
from email.mime.text import MIMEText

# Настройка логирования
logging.basicConfig(
    filename='snmp_traps.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
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
        with smtplib.SMTP('smtp.example.com', 587) as server:  # Укажите правильный SMTP сервер и порт
            server.starttls()
            server.login("your_email@example.com", "your_password")
            server.sendmail(sender, receiver, msg.as_string())
            logging.info("Email sent to %s", receiver)
    except Exception as e:
        logging.error("Failed to send email: %s", str(e))


# Callback функция для обработки Trap сообщений
def cbFun(snmpEngine, stateReference, varBinds):
    # Извлечение информации о транспортном соединении
    transportInfo = snmpEngine.transportDispatcher.getTransportInfo(stateReference)
    src_ip = transportInfo[1][0]  # IP-адрес отправителя

    try:
        # Преобразование IP-адреса в hostname
        src_hostname = socket.gethostbyaddr(src_ip)[0]
    except socket.herror:
        src_hostname = "Unknown Host"

    log_message = f'Received new Trap from {src_hostname} ({src_ip}):\n'

    for name, val in varBinds:
        oid = name.prettyPrint()  # OID в текстовом виде
        value = val.prettyPrint()  # Значение в текстовом виде
        log_message += f'{oid} = {value}\n'

    logging.info(log_message)
    print(log_message)

    # Проверка на конкретное значение Trap и отправка email
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
        snmpEngine.transportDispatcher.jobStarted(1)
        snmpEngine.transportDispatcher.runDispatcher()
    except Exception as e:
        logging.error("Error in SNMP Trap Receiver: %s", str(e))
        raise

# Запуск asyncio loop
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.run_forever()
