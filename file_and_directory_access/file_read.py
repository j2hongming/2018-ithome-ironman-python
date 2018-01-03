file_name = 'sample.txt'
f = open(file_name, 'r')
print('type of f:{}'.format(type(f)))

for line in f:
    print(line)
print('close:{}'.format(f.closed))
f.close()
print('close:{}'.format(f.closed))


with open(file_name) as f:
    print(f.readline())
print('close:{}'.format(f.closed))

with open(file_name) as f:
    lines = f.readlines()
    print(lines)
    print('len of lines:{}'.format(len(lines)))