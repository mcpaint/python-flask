import copy
import logging
import logging.config
import os
import yaml
from config import BASE_DIR

from app.log.colors import yellow, red, green


class ConsoleHandler(logging.StreamHandler):
    """Logging to console handler."""

    def emit(self, record):
        colored = copy.copy(record)
        if record.levelname == "INFO":
            colored.msg = yellow(record.msg)
        elif record.levelname == "ERROR" or record.levelname == "CRITICAL":
            colored.msg = red(record.msg)
        elif record.levelname == "DEBUG":
            colored.msg = green(record.msg)

        logging.StreamHandler.emit(self, colored)


def setup_logging(
        default_path='app/log/config/logging-dev.yml',
        default_level=logging.INFO,
        env_key='FLASK_CONFIGURATION'
):
    """Setup logging configuration"""
    # 로그 디렉토리 생성. 자동으로 생성을 안해줘서 수동으로 생성해 준다.
    os.system('mkdir -p {}/logs'.format(BASE_DIR))

    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = 'app/log/config/logging-{}.yml'.format(value)

    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level, format=' %(asctime)s - %(name)s -%(levelname)s - %(message)s')