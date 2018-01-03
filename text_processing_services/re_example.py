import re


s = 'Ray\'s birthday is 2018-1-3, and John\'s birthday is 2018-01-03'
dates = re.findall(r'\d{4}-\d{1,2}-\d{1,2}', s)
if dates:
    for idx, date in enumerate(dates):
        print("{}:{}".format(idx, date))
else:
    print('Not match')
