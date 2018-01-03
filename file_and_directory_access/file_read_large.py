import resource
import gc
gc.collect()  # don't care about stuff that would be garbage collected properly
import objgraph


file_name_100 = '100mb_file.txt'
file_name_200 = '200mb_file.txt'


def process(line):
    line.upper()

objgraph.show_most_common_types()
line_no = 0
with open(file_name_100, 'rb') as f:
    for line in f:
        process(line)
        line_no += 1

print('how many lines:{:,}'.format(line_no))
print('Memory usage: {:,} (kb)'.format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))
objgraph.show_most_common_types()

line_no = 0
with open(file_name_200, 'rb') as f:
    lines = f.readlines()
    for line in lines:
        process(line)
        line_no += 1

print('how many lines:{:,}'.format(line_no))
print('Memory usage: {:,} (kb)'.format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))
objgraph.show_most_common_types()
