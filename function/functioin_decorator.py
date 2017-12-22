from functools import wraps


# basic decorator
def my_log(func):
    def new_func(*args, **kwargs):
        name = func.__name__
        print('log about {}'.format(name))
        result = func(*args, **kwargs)
        return result
    return new_func


def wraps_my_log(func):
    @wraps(func)
    def new_func(*args, **kwargs):
        name = func.__name__
        print('log about {}'.format(name))
        result = func(*args, **kwargs)
        return result
    return new_func


def my_sum(a, b):
    return a + b


def my_sub(a, b):
    return a - b


@wraps_my_log
def my_sub_decorator(a, b):
    return a - b


print('sum is {}'.format(my_sum(8, 7)))
print('name of function is {}'.format(my_sum.__name__))

my_sum = my_log(my_sum)
print('sum is {}'.format(my_sum(9, 10)))
print('name of function is {}'.format(my_sum.__name__))

my_sub = wraps_my_log(my_sub)
print('sub is {}'.format(my_sub(66, 88)))
print('name of function is {}'.format(my_sub.__name__))

print('sub is {}'.format(my_sub_decorator(30, 20)))


# decorator with parameter
def my_log(level):
    def decorator(func):
        @wraps(func)
        def new_func(*args, **kwargs):
            name = func.__name__
            print('[{level}]log about {name}'.format(level=level, name=name))
            result = func(*args, **kwargs)
            return result
        return new_func
    return decorator


@my_log('INFO')
def my_mul(a, b):
    return a * b


print('mul is {}'.format(my_mul(30, 20)))
