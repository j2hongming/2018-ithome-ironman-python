import sys
import log_whatever
import a
logger = log_whatever.get_whatever(log_whatever.LOGGER_NAME, 'entry_point.py')

def main_entry():
    print(sys.path)
    print(sys.modules['log_whatever'])
    print(sys.modules['commons.dao.user'])
    #for key, modules in sys.modules.items():
    #    print('{} {}'.format(key, modules))

if __name__ == '__main__':
    print('current directory log_whatever first, but get logger from commons log_whatever')
    main_entry()
