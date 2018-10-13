import sys
import commons.dao.log_whatever as log_whatever
import a
logger = log_whatever.get_whatever(log_whatever.LOGGER_NAME, 'entry_point_3.py')

def main_entry():
    print(sys.path)
    #print(sys.modules['log_whatever'])
    for name, module in sys.modules.items():
        if 'log_whateve' in name:
            print('name: {}, what:{}'.format(name, module))
    print(sys.modules['commons.dao.user'])
    #for key, modules in sys.modules.items():
    #    print('{} {}'.format(key, modules))

if __name__ == '__main__':
    print('common log_whatever first, and get logger from commons log_whatever')
    main_entry()
