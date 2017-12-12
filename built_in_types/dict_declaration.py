from pprint import pprint

# brackets
demo = { 'height': 170, 'weight': 58, 'age': 20 }
pprint(demo)
print( "type of demo: {}".format( type(demo) ) )

# dict
demo2 = dict( [('height', 180), ('weight', 68),  ('age', 22)] )
pprint(demo2)
print( "type of demo2: {}".format( type(demo2) ) )

demo3 = dict(height=190, weight=90, age=25)
pprint(demo3)
print( "type of demo3: {}".format( type(demo3) ) )

# dictionary comprehension
generator = [x for x in range(10)]
demo4 = {x: x**2 for x in generator}
pprint(demo4)
print( "type of demo4: {}".format( type(demo4) ) )