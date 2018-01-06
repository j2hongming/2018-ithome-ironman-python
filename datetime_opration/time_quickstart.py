import time


# time stamp
print('time stamp: {}'.format(time.time()))

# struct_time
print('type of gmt time: {}'.format(type(time.time())))
print('local time: {}'.format(time.localtime()))
print('type of local time: {}'.format(type(time.localtime())))
print('gmt time: {}'.format(time.gmtime()))

# string
print('type of gmt time: {}'.format(type(time.gmtime())))
print(time.ctime(time.time()))
# custom string
print(time.strftime("%Y-%m-%d, %H:%M:%S, %w", time.gmtime()))