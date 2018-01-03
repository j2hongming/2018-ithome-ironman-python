import re

# greedy
s1 = '<div class="qa-list__tags">sbc</div>'
match_greedy = re.match(r'<.*>', s1)
if match_greedy:
    print('greedy reslut: {}'.format(match_greedy.group()))
else:
    print('Not match')

# non-greedy
match_non_greedy = re.match(r'<.*?>', s1)
if match_non_greedy:
    print('non-greedy reslut: {}'.format(match_non_greedy.group()))
else:
    print('Not match')

html_tags = re.findall(r'<.*?>', s1)
for idx, html_tag in enumerate(html_tags):
    print("{}:{}".format(idx, html_tag))