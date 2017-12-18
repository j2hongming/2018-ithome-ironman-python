# empty tuple
demo = {}  # it will be dictionary
print(demo)
print( "type of demo: {}".format( type(demo) ) )
print( "len of demo: {}".format( len(demo) ) )
print( "id of demo: {}".format( id(demo) ) )

demo2 = set()
print(demo2)
print( "type of demo2: {}".format( type(demo2) ) )
print( "len of demo2: {}".format( len(demo2) ) )
print( "id of demo2: {}".format( id(demo2) ) )

# multiple elements
demo3 = {'python', 'java', 'c', 'c++', 'c#', 'go', 'php', 'python', 'java'}
print(demo3)
print( "type of demo3: {}".format( type(demo3) ) )
print( "len of demo3: {}".format( len(demo3) ) )

# set comprehension
d_list = [0, 1, 1, 2 ,3 ,5, 8, 13, 21]
demo4 = {x for x in d_list if x % 3 == 0}
print(demo4)
print( "type of demo4: {}".format( type(demo4) ) )