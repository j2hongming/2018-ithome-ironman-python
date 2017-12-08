s1 = "single line's \"declaration\""
s2 = 'another single line\'s "declaration"'
print(s1)
print(s2)

m1 = """\
first line
second line \
,follow by second line
"""
print(m1)

# immutable
wrong_str = "irenman"
print(wrong_str)
print("id of wrong_str: {}".format( id(wrong_str) ))
print("error char is index 2 \"{}\"".format(wrong_str[2]))

wrong_str_2 = "irenman"
print(wrong_str_2)
print("id of wrong_str_2: {}".format( id(wrong_str_2) ))

# edit
wrong_str[2] = "o"