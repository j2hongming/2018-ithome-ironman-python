import logging
import os

LOGGER_NAME = 'test'

print('commons log whatever')


def get_whatever(name=None, who=''):
    print('commons get whatever from {}'.format(who))
    if name:
        logger = logging.getLogger(name)
        if not logger.handlers:
            print('get logger from commons setting')
            print('log level from os environ:{}'.format(os.environ.get(logging.DEBUG)))
            logger.setLevel(os.environ.get(logging.DEBUG, 'DEBUG'))
            logger.propagate = False
            formatter = logging.Formatter('%(asctime)s [%(thread)d][%(levelname)s][%(module)s:%(lineno)d] %(message)s')
            ch = logging.StreamHandler()
            ch.setFormatter(formatter)
            logger.addHandler(ch)
    else:
        logger = logging.getLogger()

    return logger
