import datetime


datetime_now = datetime.datetime.now()
print('datetime_now: {}'.format(datetime_now))
print('type of datetime_now: {}'.format(type(datetime_now)))

datetime_now_utc = datetime.datetime.utcnow()
print('datetime_now_utc: {}'.format(datetime_now_utc))
print('type of datetime_now_utc: {}'.format(type(datetime_now_utc)))

today = datetime.date.today()
print('today: {}'.format(today))
print('type of today: {}'.format(type(today)))

datetime_now_20180101 = datetime.datetime.strptime('2018-01-01', '%Y-%m-%d')
print('datetime_now_20180101: {}'.format(datetime_now_20180101))
print('type of datetime_now_20180101: {}'.format(type(datetime_now_20180101)))

if datetime_now > datetime_now_20180101:
    print('latest:{}'.format(datetime_now))
else:
    print('latest:{}'.format(datetime_now_20180101))

time_difference = datetime_now - datetime_now_20180101
print('time_difference: {}'.format(time_difference))
print('total seconds:{}'.format(time_difference.total_seconds()))
print('type of time_difference: {}'.format(type(time_difference)))