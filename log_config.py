import logging
from logging.handlers import TimedRotatingFileHandler
import os


def setup_logger(name, log_file, level=logging.DEBUG):
    """Создание и настройка логгера с заданным именем и файлом лога."""

    # Если логгер уже существует, просто возвращаем его
    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        # Создаем директорию для логов, если ее нет
        os.makedirs(os.path.dirname(f'logs/{log_file}'), exist_ok=True)

        handler = TimedRotatingFileHandler(f'logs/{log_file}', when="midnight", interval=1, backupCount=31)
        handler.suffix = "%Y-%m-%d"
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        logger.setLevel(level)
        logger.addHandler(handler)

    return logger
