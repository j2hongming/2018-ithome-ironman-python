import re


s = 'purple abc.lin@google.com monkey dishwasher'
match = re.search(r'\w+@\w+', s)
if match:
    print(match.group())
else:
    print('Not match')

match2 = re.search(r'[\w.-]+@[\w.-]+', s)
if match2:
    print(match2.group())
else:
    print('match2 Not match')

s2 = 'red abc.lin@google.com monkey dishwasher cde.chen@google.com'
match3 = re.match(r'[\w.-]+@[\w.-]+', s2)
if match3:
    print(match3.group())
else:
    print('match3 Not match')

match4 = re.search(r'[\w.-]+@[\w.-]+', s2)
if match4:
    print(match4.group())
else:
    print('Not match')

match5 = re.findall(r'[\w.-]+@[\w.-]+', s2)
for idx, mail in enumerate(match5):
    print("{}:{}".format(idx, mail))