def re_score(cal_base ,default_score=100, who='ming', clazz='A'):
    output = '{who} score before in class {clazz}: {score}'
    print( output.format(who=who, clazz=clazz, score=default_score) )
    score = default_score * cal_base
    print( output.format(who=who, clazz=clazz, score=score) )

try:
    re_score()
except TypeError as e:
    print( "Type Error:: {0}".format(e) )

re_score(20)
re_score(cal_base=20)

# re_score(cal_base=20, 20)
# SyntaxError: positional argument follows keyword argument

re_score(20, 20)
re_score(20, 30, 'john')
re_score(20, clazz="B")
try:
    re_score(20, name='tom')
except TypeError as e:
    print( "Type Error:: {0}".format(e) )

# passed as a value in a dictionary preceded by **
info = {'default_score':80, 'who':'tom', 'clazz':'B'}
re_score(20, **info)