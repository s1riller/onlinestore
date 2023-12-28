import logging
from apscheduler.schedulers.background import BackgroundScheduler
from django.core.management import call_command

# Настройка логгера
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Создание файла логирования
handler = logging.FileHandler('scheduler.log')
handler.setLevel(logging.DEBUG)

# Формат записей лога
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Добавление обработчика к логгеру
logger.addHandler(handler)


def run_take_med_command():
    logger.info("Starting take med processor command...")
    try:
        call_command("take_med")
        logger.info("Take med processor command finished.")
    except Exception as e:
        logger.error(f"Error in take med processor command: {str(e)}")


scheduler = BackgroundScheduler()
scheduler.add_job(run_take_med_command, 'interval', seconds=10)
scheduler.start()
