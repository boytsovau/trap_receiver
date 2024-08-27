import os
import glob
from pysnmp.smi import builder, view, compiler, rfc1902
from pysnmp.hlapi.asyncio import SnmpEngine, CommunityData, ContextData
from pysnmp.entity import config
from pysnmp.carrier.asyncio.dgram import udp
from pysnmp.entity.rfc3413 import ntfrcv
import logging
import asyncio
import smtplib
from email.mime.text import MIMEText

# Настройка логирования
logging.basicConfig(
    filename='snmp_traps.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

# Загрузка и компиляция всех MIB файлов из директории
mibBuilder = builder.MibBuilder()

# Определяем директорию с MIB-файлами
mib_sources_dir = 'mibs/huawei/'

# Добавляем MIB компилятор с источником файлов
compiler.addMibCompiler(mibBuilder, sources=[f'file://{mib_sources_dir}'])

# Загружаем все MIB файлы из директории
for mib_file in glob.glob(os.path.join(mib_sources_dir, '*.mib')):
    mib_name = os.path.splitext(os.path.basename(mib_file))[0]
    try:
        mibBuilder.loadModules(mib_name)
        logging.info(f'MIB {mib_name} successfully loaded.')
    except Exception as e:
        logging.error(f'Error loading MIB {mib_name}: {e}')

mibViewController = view.MibViewController(mibBuilder)

# Функция для отправки email
def send_email(subject, message):
    sender = "your_email@example.com"
    receiver = "recipient@example.com"
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    try:
        with smtplib.SMTP('smtp.example.com', 25) as server:
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
        try:
            oid, val_str = name.prettyPrint(), val.prettyPrint()
            mibName, mibSym = mibViewController.mibBuilder.importSymbols(
                name.getMibSymbol()[0],  # Имя MIB
                name.getMibSymbol()[1]   # Имя объекта внутри MIB
            )
            resolvedName = f"{mibName.getName()}::{mibSym.getLabel()}"
            log_message += f'{resolvedName} = {val_str}\n'
        except Exception as e:
            log_message += f'{oid} = {val_str}\n'
            logging.error(f"Error resolving OID {oid}: {e}")

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
            udp.UdpTransport().openServerMode(('0.0.0.0', 10162))
        )

        # Настройка SNMPv2c
        config.addV1System(snmpEngine, 'my-area', 'public')

        # Привязка функции обработки сообщений
        ntfrcv.NotificationReceiver(snmpEngine, cbFun)

        logging.info("SNMP Trap Receiver is running and logging to 'snmp_traps.log'...")
        print("SNMP Trap Receiver is running and logging to 'snmp_traps.log'...")

        # Запуск обработчика asyncio
        snmpEngine.transportDispatcher.jobStarted(1)
        await snmpEngine.transportDispatcher.runDispatcher()
    except Exception as e:
        logging.error("Error in SNMP Trap Receiver: %s", str(e))
        raise

# Запуск asyncio loop
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.run_forever()
