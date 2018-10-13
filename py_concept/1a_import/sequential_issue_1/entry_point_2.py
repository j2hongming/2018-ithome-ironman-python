import sys
import log_whatever
log_whatever.get_whatever(log_whatever.LOGGER_NAME, 'entry_point_2.py')
import a

def main_entry():
    print('custom log_whatever get logger first, and get logger from custom log_whatever first. It will create log file')
    print(sys.path)
    print(sys.modules['log_whatever'])
    print(sys.modules['commons.dao.user'])
    #for key, modules in sys.modules.items():
    #    print('{} {}'.format(key, modules))

if __name__ == '__main__':
    main_entry()
