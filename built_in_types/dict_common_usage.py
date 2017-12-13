# loop over the keys in sorted order,
demo = { 'height': 170, 'weight': 58, 'age': 20 }
for key in sorted(demo.keys()):
    print (key, demo[key])

# filter
demo2 = dict(Mary=80, Jack=90, Smith=60, John=58, Tom=95, Jane=88, Tina=46)
greater_than_ninety = dict((key, value) for key, value in demo2.items() if value >= 90)
less_than_sixty = dict((key, value) for key, value in demo2.items() if value <= 60)
print( "greater_than_ninety: {}".format(greater_than_ninety) )
print( "less_than_sixty: {}".format(less_than_sixty) )


