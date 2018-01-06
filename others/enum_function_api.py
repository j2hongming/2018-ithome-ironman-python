from enum import Enum


Model = Enum('Model', 'IRON SPIDER FLASH SUPER')
for m in Model:
    print('Model:{}, name:{}, value:{}'.format(m, m.name, m.value))
    print('type of value:{}'.format(type(m.value)))
