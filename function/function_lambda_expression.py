add_five = lambda x: x + 5
print( "{}".format(add_five(10)) )
print( "type of lambda expression: {}".format(lambda x: x + 5) )

def make_adder(n):
    return lambda x: x + n

add_three = make_adder(3)
add_thirty = make_adder(30)

print( "{}".format(add_three(10)) )
print( "type of lambda expression add_three: {}".format(add_three) )

print( "{}".format(add_thirty(10)) )
print( "type of lambda expression add_thirty: {}".format(add_thirty) )