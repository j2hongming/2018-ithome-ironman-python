# list is mutable ,string is immutable
demo = [x for x in range(10)]
print( "demo data:{}".format(demo) )
print( "id of demo data:{}".format(id(demo)) )

demo.append(11)
print( "demo data after appending:{}".format(demo) )
print( "id of demo data after appending:{}".format(id(demo)) )

s1 = demo[:]
print( "sliced 1:{}".format(s1) )
print( "id of demo data after slicing:{}".format(id(demo)) )
print( "id of s1 data:{}".format(id(s1)) )

str1 = 'ironman'
str2 = 'ironman'
print( "id of str1:{0} ; id of str2:{1}".format(id(str1), id(str2)) )


# build str
source_str = ['i', 'r', 'o', 'n', 'm', 'a', 'n']

final_str = ""
print( "id of final_str:{}".format(id(final_str)) )
for x in source_str:
    final_str += x
    print( "final str after +:{}".format(final_str) )
    print( "id of final_str after +:{}".format(id(final_str)) )
print( "final str:{}".format(final_str) )


str_list = []
print( "str_list:{}".format(str_list) )
for x in source_str:
    str_list.append(str(x))
    print( "str_list after appending:{}".format(str_list) )
    print( "id of str_list after appending:{}".format(id(str_list)) )
print( "str_list with join:{}".format("".join(str_list)) )

# assign
demo2 = [x for x in range(20)]
print( "demo2 data:{}".format(demo2) )
print( "id of demo2 data:{}".format(id(demo2)) )
demo3 = demo2
print( "demo3 data:{}".format(demo3) )
print( "id of demo3 data:{}".format(id(demo3)) )
