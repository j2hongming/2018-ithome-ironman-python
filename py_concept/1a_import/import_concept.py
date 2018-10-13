import os
import sys
print('sys.path data({}):'.format(type(sys.path)))
for path in sys.path:
    print(path)

print('first element in sys.path:')
print(sys.path[0])

print('sys.modules data({}):'.format(type(sys.modules)))
for name, module in sys.modules.items():
    print('name:{}'.format(name))
    print(module)
    print('='*10)
