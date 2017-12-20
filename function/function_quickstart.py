def fib(n):
    """Print a Fibonacci series up to n."""
    output, next_result = 0, 1
    while output < n:
        print(output, end=' ')
        output, next_result = next_result, output+next_result
    print()

fib(500)

try:
    print(output)
except NameError as e:
    print( "Name Error:: {0}".format(e) )

try:
    print(n)
except NameError as e:
    print( "Name Error:: {0}".format(e) )

print( "type of fib: {}".format(type(fib)) )

# rename
my_fib = fib
my_fib(1000)

# if no return syntax
print( "return value:{}".format(fib(500)) )