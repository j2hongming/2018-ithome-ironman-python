# empty tuple
demo = ()
print(demo)
print( "type of demo: {}".format( type(demo) ) )
print( "len of demo: {}".format( len(demo) ) )
print( "id of demo: {}".format( id(demo) ) )

try:
    demo[0] = 1
except TypeError as e:
    print( "Type Error: {0}".format(e) )

demo2 = tuple()
print(demo2)
print( "type of demo2: {}".format( type(demo2) ) )
print( "len of demo2: {}".format( len(demo2) ) )
print( "id of demo2: {}".format( id(demo2) ) )

# single element tuple
demo3 = 1,
print(demo3)
print( "type of demo3: {}".format( type(demo3) ) )
print( "len of demo3: {}".format( len(demo3) ) )
print( "id of demo3: {}".format( id(demo3) ) )

demo4 = (2,)
print(demo4)
print( "type of demo4: {}".format( type(demo4) ) )
print( "len of demo4: {}".format( len(demo4) ) )
print( "id of demo4: {}".format( id(demo4) ) )

# multiple elements
demo5 = 1, 3, 5, 7, 9
print(demo5)
print( "type of demo5: {}".format( type(demo5) ) )

demo6 = (2, 4, 6, 8, 10)
print(demo6)
print( "type of demo6: {}".format( type(demo6) ) )

# with mutable object
squre = [x**2 for x in range(10)]
demo7 = ('squre result', squre)
print(demo7)
print( "type of demo7: {}".format( type(demo7) ) )