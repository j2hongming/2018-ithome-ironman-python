from enum import Enum


class Model(Enum):
    IRON = 'iron man'
    FLASH = 'flash man'
    SPIDER = 'spider man'


print('enum member:{}'.format(Model.IRON))
print('name of enum member:{}'.format(Model.IRON.name))
print('value of enum member:{}'.format(Model.IRON.value))
print('type of enum member:{}'.format(type(Model.IRON)))
print('type of enum member name:{}'.format(type(Model.IRON.name)))
print('type of enum member value:{}'.format(type(Model.IRON.value)))


def welcome_controller(request_type):
    welcome_msg = 'Hi, I\'m {}'
    print(welcome_msg.format(request_type.value))

welcome_controller(Model.IRON)
try:
    welcome_controller(Model('flash man'))
    welcome_controller(Model('super man'))
except ValueError as e:
    print(e)
