demo = [x for x in range(10)]
print( "demo data:{}".format(demo) )


# indexed
print( "first data:{}".format(demo[0]) )
print( "last data:{}".format(demo[-1]) )

try:
    print(demo[10])
except IndexError as e:
    print( "Index Error: {0}".format(e) )

try:
    print(demo["10"])
except TypeError as e:
    print( "Type Error: {0}".format(e) )

# sliced
s1 = demo[:]
print( "sliced 1:{}".format(s1) )

s2 = demo[2:]
print( "sliced 2:{}".format(s2) )

s3 = demo[2:5]
print( "sliced 3:{}".format(s3) )

s4 = demo[:5]
print( "sliced 4:{}".format(s4) )

s5 = demo[-3:]
print( "sliced 5:{}".format(s5) )

s6 = demo[::2]
print( "sliced 6:{}".format(s6) )

s7 = demo[1::2]
print( "sliced 7:{}".format(s7) )


# iteration
summay = 0
for number in demo:
    print(number)
    summay += number
print( "summay:{}".format(summay) )

summay2 = 0
idx = 0
while idx < len(demo):  
    print(demo[idx])
    summay2 += demo[idx]
    idx += 1
print( "summay2:{}".format(summay2) )


# modification
demo.append(11)
print( "demo data after append:{}".format(demo) )

demo.insert(-1 ,10)
print( "demo data after insert:{}".format(demo) )

demo.extend( list(range(12, 21)) )
print( "demo data after extend:{}".format(demo) )

demo.extend( [1, 20, 5, 20] )
demo.remove(20)
demo.remove(5)
print( "demo data after remove:{}".format(demo) )

demo[1:5] = [9, 9, 9, 9]
print( "demo data after slice replace:{}".format(demo) )

demo[2:6] = []
print( "demo data after slice remove:{}".format(demo) )