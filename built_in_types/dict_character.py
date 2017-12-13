# dict key : Uniqueness, immutable type
demo = { 'height': 170, 'weight': 58, 'height': 20 }
print( "demo data:{}".format(demo) )

demo2 = { 'height': 170, 'weight': 58, 'Height': 20 }
print( "demo2 data:{}".format(demo2) )

demo3 = { 5: '170', 6: '58' }
print( "demo3 data:{}".format(demo3) )

demo4 = {}
list_as_key = [0, 1, 2 ,3 ,4]
tuple_as_key = ('0', 1, '2' ,3 ,4)
tuple_as_key_with_list = (0, 1, 2 ,3 ,4, list_as_key)
try:
    
    demo4[list_as_key] = 5
    print( "Type Error: {0}".format(e) )
except TypeError as e:
    print( "Type Error: {0}".format(e) )

try:
    demo4[tuple_as_key] = 5
    print( "demo4 data:{}".format(demo4) )
except TypeError as e:
    print( "Type Error: {0}".format(e) )

try:
    demo4[tuple_as_key_with_list] = 5
    print( "demo4 data:{}".format(demo4) )
except TypeError as e:
    print( "Type Error: {0}".format(e) )

# dict is mutable
demo = { 'height': 170, 'weight': 58, 'age': 20 }
print( "demo data:{}".format(demo) )
print( "id of demo data:{}".format(id(demo)) )

demo['height'] = 180
print( "demo data:{}".format(demo) )
print( "id of demo data:{}".format(id(demo)) )

demo['name'] = 'Tom'
print( "demo data:{}".format(demo) )
print( "id of demo data:{}".format(id(demo)) )

del demo['age']
print( "demo data:{}".format(demo) )
print( "id of demo data:{}".format(id(demo)) )
