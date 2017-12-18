zoo_taipei = {'bear', 'fish', 'wolf', 'deer', 'tiger'}
zoo_kaohsiung = {'lion', 'tiger', 'bear', 'hipo', 'giraffe'}

# intersection
common_animals = zoo_taipei & zoo_kaohsiung
print(common_animals)

# union
all_animals = zoo_taipei | zoo_kaohsiung
print(all_animals)

# difference
taipei_uniq_animals = zoo_taipei - zoo_kaohsiung
print(taipei_uniq_animals)

kaohsiung_uniq_animals = zoo_kaohsiung - zoo_taipei
print(kaohsiung_uniq_animals)

# symmetric difference
# animals in taipei or kaohsiung but not both
new_animals = zoo_taipei ^ zoo_kaohsiung
print(new_animals)

# NOT support indexed
try:
    print(zoo_taipei[0])
except TypeError as e:
    print( "Type Error: {0}".format(e) )

# iteration
for animal in zoo_taipei:
    print( "animal:{}".format(animal) )

# include membership testing
if 'tiger' in zoo_kaohsiung:
    print( "tiger in kaohsiung" )

if 'lion' in zoo_taipei:
    print( "lion in taipei" )
else:
    print( "lion NOT in taipei" )