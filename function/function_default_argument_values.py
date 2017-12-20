# The default values are evaluated at the point of function definition in the defining scope
default_score = 100
def re_score(s=default_score):
    print( "score before: {}".format(s) )
    s = s * 10
    print( "score after: {}".format(s) )

default_score = 120
re_score()

# The default value is evaluated only once. This makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes.
# default to be shared between subsequent calls
def add_score(s, class_sroces=[]):
    class_sroces.append(s)
    return class_sroces

print(add_score(60))
print(add_score(84))
print(add_score(99))

# don’t want the default to be shared between subsequent calls
def add_score_independent(s, class_sroces=None):
    if class_sroces is None:
        class_sroces = []
    class_sroces.append(s)
    return class_sroces

print(add_score_independent(60))
print(add_score_independent(84))
print(add_score_independent(99))