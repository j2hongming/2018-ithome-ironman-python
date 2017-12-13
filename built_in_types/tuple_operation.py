demo = ('name', 'age', 'height', 'weight')

# indexed
try:
    print(demo[0])
    print(demo[3])
    print(demo[4])
except IndexError as e:
    print( "Index Error: {0}".format(e) )


# unpacking
name, age, height, weight = demo
print( "{}, {}, {}, {}".format(name, age, height, weight ) )


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
for ele in demo:
    print(ele)

idx = 0
while idx < len(demo):  
    print(demo[idx])
    idx += 1
