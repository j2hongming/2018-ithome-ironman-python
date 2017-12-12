demo = { 'height': 170, 'weight': 58, 'age': 20 }

# square brackets
print( "height is {}".format(demo['height']) )
try:
    name = demo['name']
    print( "name is {}".format(name) )
except KeyError as e:
    print( "KeyError: {} does not exist".format(e) )


# dict.get(key)
print( "height is {}".format(demo.get('height')) )
name = demo.get('name')
print( "name: {}".format(name) )
name = demo.get('name', 'Tom')
print( "name: {}".format(name) )

# check key if exist
if 'height' in demo:
    print( "height is {}".format(demo['height']) )
else:
    print( "height not found" )

if 'name' in demo:
    print( "name is {}".format(demo['name']) )
else:
    print( "name not found" )

# iteration
for what in demo:
    print( "what is {}".format(what) )

for key in demo.keys():
    print( "key is {}".format(key) )
    print( "type of key is {}".format(type(key)) )

for value in demo.values():
    print( "value is {}".format(value) )
    print( "type of value is {}".format(type(value)) )

for key, value in demo.items():
    print( "key is {}".format(key) )
    print( "value is {}".format(value) )

# modification
print( "demo data before modification:{}".format(demo) )
demo['height'] = 180
demo['name'] = 'Tom'
del demo['age']
print( "demo data after modification:{}".format(demo) )

