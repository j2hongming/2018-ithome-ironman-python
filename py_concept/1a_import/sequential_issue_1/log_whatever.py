import logging
from logging.config import fileConfig

LOGGER_NAME = 'test'

print('custom log whatever')

def get_whatever(name=None, who=''):
    print('custom get whatever from {}'.format(who))
    if name:
        logger = logging.getLogger(name)
    else:
        logger = logging.getLogger()

    if not logger.handlers:
        print('load file "logging_config.ini" ')
        fileConfig('logging_config.ini', disable_existing_loggers=True)

    return logger
