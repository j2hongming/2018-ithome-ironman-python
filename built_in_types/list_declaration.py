# square brackets - empty list with append
d1 = []
d1.append(0)
d1.append(1)
d1.append(1)
d1.append(2)
d1.append(3)
d1.append(5)
print(d1)

# square brackets - [] directly
d2 = [0, 1, 1, 2 ,3 ,5]
print(d2)

# list comprehensions
d3 = [x**2 for x in range(10)]
print(d3)
d4 = [y for y in d3 if y % 2 == 0]
print(d4)

# type constructor
d5 = list()
d5.append(0)
d5.append(1)
d5.append(1)
d5.append(2)
d5.append(3)
d5.append(5)
print(d5)

d6 = list("011235")
print(d6)

d7 = [int(x) for x in d6]
print(d7)