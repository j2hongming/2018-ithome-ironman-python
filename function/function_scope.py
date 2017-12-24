import builtins

var1 = 10


def demo(para1):
    var2 = 100
    print('var1 is {}, it\'s global in demo module(file)'.format(var1))
    print('para1 is {}, it\' lobal in demo function'.format(para1))
    print('var2 is {}, it\' lobal in demo function'.format(var2))


demo(50)
try:
    print('para1 is {}'.format(para1))
except NameError as e:
    print('Name Error: {0}'.format(e))

try:
    print('var2 is {}'.format(var2))
except NameError as e:
    print('Name Error: {0}'.format(e))


def demo2(para2):
    var3 = 66
    global var5
    var5 = 33

    def demo3():
        var3 = 22
        var4 = 88
        print('var3: {}'.format(var3))
        print('var4: {}'.format(var4))
        print('sum of var3 and var4: {}'.format(var3 + var4))

    demo3()

demo2(10)
print('var5: {}'.format(var5))
try:
    demo3()
except NameError as e:
    print('Name Error: {0}'.format(e))

builtins_name = dir(builtins)
print('{}'.format(builtins_name))
print('len of builtins_name is {}'.format(len(builtins_name)))
print('{}'.format('NameError' in builtins_name))