import os
import traceback
from pysnmp.smi import builder, view
from log_config import setup_logger

logger = setup_logger('mib_log', 'mib.log')


def load_mib_modules(mib_dir, mib_modules: list):

    # Создание MIB Builder
    mibBuilder = builder.MibBuilder()
    mibBuilder.addMibSources(builder.DirMibSource(mib_dir))

    # Получение списка всех .py файлов в директории
    mib_files = [f for f in os.listdir(mib_dir) if any(mib in f for mib in mib_modules)]

    # Извлечение имен модулей (без .py)
    mib_modules = [os.path.splitext(f)[0] for f in mib_files]

    loaded_modules = []
    for module in mib_modules:
        try:
            mibBuilder.loadModules(module)
            logger.info(f"Модуль успешно загружен: {module}")
            loaded_modules.append(module)
        except Exception as e:
            logger.error(f"Ошибка при загрузке модуля {module}: {str(e)}")
            traceback.print_exc()

    mibViewController = view.MibViewController(mibBuilder)

    return mibViewController



if __name__ == '__main__':
    from pysnmp.smi import rfc1902
    current_dir = os.path.dirname(os.path.abspath(__file__))
    mib_path = os.path.join(current_dir, 'mibs')
    mib = load_mib_modules(mib_path, ['HUAWEI', 'CISCO', 'SNMPv2', 'BGP4-MIB'])
    name = "1.3.6.1.4.1.2011.6.122.26.6.1"
    resolved_oid = rfc1902.ObjectIdentity(name).resolveWithMib(mib)
    print(resolved_oid.prettyPrint())

    print(resolved_oid.getMibSymbol())